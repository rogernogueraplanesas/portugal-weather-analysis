import sqlite3
import first_stage as fs
import second_stage as ss
import third_stage as ts
import fourth_stage as fts
import windroses as wr
import settings as s



# Tables are created and filled with data from the original data source (JSON files)
def create_insert_tables():
    fs.create_tables(database=database)
    fs.insert_stations_data(database=database, raw_data_path=s.raw_json_data)
    fs.insert_observations_data(database=database, raw_data_path=s.raw_json_data)

    
# Stations data is extracted in CSV format to import them into QGIS based on their coordinates
def export_stations_coordinates():
    stations_coordinates = fs.get_coordinates(database=database)
    fs.save_to_csv(stations_coordinates, filename=s.stations_data_filename)
    

# After intersecting each weather station with a QGIS layer, each station dataset gets 2 new values; 'dicofre' (zip code) and 'concelho' (municipality)

# The intersected (merged) data is exported as CSV files, divided into 5 different regions.

# The only data needed from the merged files are 'idestacao' (PRIMARY KEY), 'dicofre' (zip code) and 'concelho' (municipality), to be included in the DB

# Cleaning process for each regional CSV
def clean_imported_csv():
    ss.clean_portugal_data(raw_file=s.intersect_cont_portugal, clean_file=s.clean_intersect_cont_portugal)
    ss.clean_madeira_data(raw_file=s.intersect_madeira, clean_file=s.clean_intersect_madeira)
    ss.clean_açores_central_data(raw_file=s.intersect_açores_cent, clean_file=s.clean_intersect_açores_cent)
    ss.clean_açores_occidental_data(raw_file=s.intersect_açores_occid, clean_file=s.clean_intersect_açores_occid)
    ss.clean_açores_oriental_data(raw_file=s.intersect_açores_orient, clean_file=s.clean_intersect_açores_orient)


# 'dicofre' and 'concelho' columns must be added into the 'stations' table
# Both columns are filled based on their id_estacao (which is a PK in 'stations')
    
def create_insert_dicofre_concelho():    
    ts.add_columns(database=database)
    ts.add_portugal_data(database=database, cleaned_file=s.clean_intersect_cont_portugal)
    ts.add_madeira_data(database=database, cleaned_file=s.clean_intersect_madeira)
    ts.add_açores_central_data(database=database, cleaned_file=s.clean_intersect_açores_cent)
    ts.add_açores_occidental_data(database=database, cleaned_file=s.clean_intersect_açores_occid)
    ts.add_açores_oriental_data(database=database, cleaned_file=s.clean_intersect_açores_orient)
    

# With the DB completed, some data must be retrieved in order to create the final windroses per each existing concelho
# Wind data (windroses) are grouped by year, month and year + month (from 2018 to 2023)

# Wind data retrieval based on the timespan    
def get_wind_data():    
    yearly_data = fts.yearly_windspeed_direction(database=database)
    fts.yearly_data_to_csv(yearly_data, filename=s.wind_data_yearly)
    monthly_data = fts.monthly_windspeed_direction(database=database)
    fts.monthly_data_to_csv(monthly_data, filename=s.wind_data_monthly)
    year_month_data = fts.year_month_windspeed_direction(database=database)
    fts.year_month_data_to_csv(year_month_data, filename=s.wind_data_year_month)
    
# Windroses generation    
def create_windroses():    
    wr.create_yearly_windrose()
    wr.create_monthly_windrose()
    wr.create_year_month_windrose()
    #wr.create_test_windrose() # Only for testing purposes


#______________________________________________________   MAIN   ______________________________________________________

if __name__=="__main__":

# SQLite DB connection
    database = sqlite3.connect("weather.db")

# PRE-QGIS/////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Enable only the next 2 steps, previous to any QGIS transformation
    create_insert_tables()
    export_stations_coordinates()

# POST-QGIS////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Comment the previous 2 steps after importing the QGIS CSV files
    clean_imported_csv()
    create_insert_dicofre_concelho()
    get_wind_data()
    create_windroses()
    database.close()