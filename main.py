import sqlite3
import tables_queries as tq
import functions as f
import settings as s
import qgis_data_cleaning as qgis
import windroses as wr

def create_insert_tables():
    f.create_tables(database=database)
    f.insert_stations_data(database=database, json_path=s.JSON_PATH)
    f.insert_observations_data(database=database, json_path=s.JSON_PATH)
    
    #Stations coordinates are extracted in csv format to work with in qgis
    
def export_stations_coordinates():
    stations_coordinates = f.get_coordinates(database=database)
    f.save_to_csv(stations_coordinates, "stations_csv.csv")
    
    #Files are imported into qgis and intersected csv files are obtained from there
    #Next step is to extract the useful data from the intersected files (cleaning it)    


def clean_imported_csv():
    qgis.clean_portugal_data()
    qgis.clean_madeira_data()
    qgis.clean_açores_central_data()
    qgis.clean_açores_occidental_data()
    qgis.clean_açores_oriental_data()
   
    #The cleaned data has to be introduced in new columns regarding the dicofre number anc concelho for each station
    
def create_insert_dicofre_concelho():    
    tq.add_columns(database=database)
    f.add_portugal_data(database=database)
    f.add_madeira_data(database=database)
    f.add_açores_central_data(database=database)
    f.add_açores_occidental_data(database=database)
    f.add_açores_oriental_data(database=database)
    
    #Having the stations table completed, it is possible to retrieve data from both the stations and the observations table to usse it for the windroses
    
def get_wind_data():    
    yearly_data = tq.yearly_windspeed_direction(database=database)
    f.yearly_data_to_csv(yearly_data, "wind_data_yearly.csv")
    monthly_data = tq.monthly_windspeed_direction(database=database)
    f.monthly_data_to_csv(monthly_data, "wind_data_monthly.csv")
    year_month_data = tq.month_year_windspeed_direction(database=database)
    f.year_month_data_to_csv(year_month_data, "wind_data_year_month.csv")
    
    #The csv files are moved into the folder "windrose_csv_data"
    #The csv files are processed in order to create windroses in function of the month/year/month+year for each different concelho registered
    
def create_windroses():    
    wr.create_yearly_windrose()
    wr.create_monthly_windrose()
    wr.create_year_month_windrose()
    wr.create_test_windrose()


def empty_conc_dicofr(database):
    cursor = database.cursor()
    try:
        cursor.execute("UPDATE stations SET concelho = NULL, dicofre = NULL")
        database.commit()
        print("Columns 'concelho' and 'dicofre' are emptied successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__=="__main__":
    database = sqlite3.connect("weather.db")
    create_insert_tables()
    export_stations_coordinates()
    clean_imported_csv()
    create_insert_dicofre_concelho()
    get_wind_data()
    create_windroses()
    database.close()