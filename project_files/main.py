import sqlite3
import functions as f
import settings as s
import qgis_data_cleaning as qgis
import windroses as wr


# Tables are created and filled with data from the original data source (JSON files)

def create_insert_tables():
    f.create_tables(database=database)
    f.insert_stations_data(database=database, json_path=s.JSON_PATH)
    f.insert_observations_data(database=database, json_path=s.JSON_PATH)

    
#Stations data is extracted in CSV format to import them into QGIS based on their coordinates
    
def export_stations_coordinates():
    stations_coordinates = f.get_coordinates(database=database)
    f.save_to_csv(stations_coordinates, "stations_csv.csv")
    

#After intersecting each weather station with a QGIS layer, each station gets 2 new values; 'dicofre' (zip code) and 'concelho' (municipality)

#The intersected (merged) data is exported as CSV files, divided into 5 different regions.

#The CSV files must be 'cleaned' leaving just the 'idestacao' (PRIMARY KEY), 'dicofre' (zip code) and 'concelho' (municipality) per station


def clean_imported_csv():
    qgis.clean_portugal_data()
    qgis.clean_madeira_data()
    qgis.clean_açores_central_data()
    qgis.clean_açores_occidental_data()
    qgis.clean_açores_oriental_data()


#New columns are added into the 'stations' table
#Values for dicofre and concelho columns are added per station in function of their primary key (idestacao)
    
def create_insert_dicofre_concelho():    
    f.add_columns(database=database)
    f.add_portugal_data(database=database)
    f.add_madeira_data(database=database)
    f.add_açores_central_data(database=database)
    f.add_açores_occidental_data(database=database)
    f.add_açores_oriental_data(database=database)
    

#With both tables filled, data is retrieved through ab inner join in order to create the final windroses per each concelho; grouped by year, month and year + month (from 2018 to 2023)
    
def get_wind_data():    
    yearly_data = f.yearly_windspeed_direction(database=database)
    f.yearly_data_to_csv(yearly_data, "wind_data_yearly.csv")
    monthly_data = f.monthly_windspeed_direction(database=database)
    f.monthly_data_to_csv(monthly_data, "wind_data_monthly.csv")
    year_month_data = f.year_month_windspeed_direction(database=database)
    f.year_month_data_to_csv(year_month_data, "wind_data_year_month.csv")
    

#The retrieved data written in different CSV files is used to create the windroses
    
def create_windroses():    
    wr.create_yearly_windrose()
    wr.create_monthly_windrose()
    wr.create_year_month_windrose()
    wr.create_test_windrose()

#______________________________________________________   MAIN   ______________________________________________________

if __name__=="__main__":
    database = sqlite3.connect("weather.db")
    
#Enable only the next 2 steps, previous to any QGIS transformation

    create_insert_tables()
    export_stations_coordinates()

#Comment the previous 2 steps after importing the QGIS CSV files

    clean_imported_csv()
    create_insert_dicofre_concelho()
    get_wind_data()
    create_windroses()
    database.close()