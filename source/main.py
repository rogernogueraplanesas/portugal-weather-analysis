import sqlite3
import create_fill_db as cf
import qgis_data_clean as qgis_c
import qgis_data_insert as qgis_i
import wind_data_extract as wd
import windroses as wr
import settings as s



# Tables are created and filled with data from the original data source (JSON files)
def create_insert_tables():
    cf.create_tables(database=database)
    cf.insert_stations_data(database=database, raw_data_path=s.raw_json_data)
    cf.insert_observations_data(database=database, raw_data_path=s.raw_json_data)

    
# Stations data is extracted in CSV format to import them into QGIS based on their coordinates
def export_stations_coordinates():
    stations_coordinates = cf.get_coordinates(database=database)
    cf.save_to_csv(stations_coordinates, filename=s.stations_data_filename)

# After intersecting each weather station with a QGIS layer, each station dataset gets 2 new values; 'dicofre' (zip code) and 'concelho' (municipality)

# The intersected (merged) data is exported as CSV files, divided into 5 different regions.

# The only data needed from the merged files are 'id_estacao' (PRIMARY KEY), 'dicofre' (zip code) and 'concelho' (municipality)

# Based on their id_estacao, the 'dicofre' and 'concelho' values are inserted into the stations table

# Cleaning process for each regional CSV
def clean_imported_csv():
    qgis_c.clean_portugal_data(raw_file=s.intersect_cont_portugal, clean_file=s.clean_intersect_cont_portugal)
    qgis_c.clean_madeira_data(raw_file=s.intersect_madeira, clean_file=s.clean_intersect_madeira)
    qgis_c.clean_açores_central_data(raw_file=s.intersect_açores_cent, clean_file=s.clean_intersect_açores_cent)
    qgis_c.clean_açores_occidental_data(raw_file=s.intersect_açores_occid, clean_file=s.clean_intersect_açores_occid)
    qgis_c.clean_açores_oriental_data(raw_file=s.intersect_açores_orient, clean_file=s.clean_intersect_açores_orient)

# Insertion process based on 'id_estacao'    
def create_insert_dicofre_concelho():    
    qgis_i.add_columns(database=database)
    qgis_i.add_portugal_data(database=database, cleaned_file=s.clean_intersect_cont_portugal)
    qgis_i.add_madeira_data(database=database, cleaned_file=s.clean_intersect_madeira)
    qgis_i.add_açores_central_data(database=database, cleaned_file=s.clean_intersect_açores_cent)
    qgis_i.add_açores_occidental_data(database=database, cleaned_file=s.clean_intersect_açores_occid)
    qgis_i.add_açores_oriental_data(database=database, cleaned_file=s.clean_intersect_açores_orient)
    

# With the DB completed, some data must be retrieved (as CSV) in order to create the final windroses per each existing concelho
# Wind data (windroses) are grouped by year, month and year + month (from 2018 to 2023)

# Wind data retrieval 
def get_wind_data():    
    yearly_data = wd.yearly_windspeed_direction(database=database)
    wd.yearly_data_to_csv(yearly_data, filename=s.wind_data_yearly)
    monthly_data = wd.monthly_windspeed_direction(database=database)
    wd.monthly_data_to_csv(monthly_data, filename=s.wind_data_monthly)
    year_month_data = wd.year_month_windspeed_direction(database=database)
    wd.year_month_data_to_csv(year_month_data, filename=s.wind_data_year_month)
    
# Windroses generation    
def create_windroses():    
    wr.create_yearly_windrose(csv_path=s.wind_data_yearly)
    wr.create_monthly_windrose(csv_path=s.wind_data_monthly)
    wr.create_year_month_windrose(csv_path=s.wind_data_year_month)
    #wr.create_test_windrose(csv_path=s.wind_data_test) # Only for testing purposes

#--------------------------------------------------------------------------------------------------------------------------------

if __name__=="__main__":

# SQLite DB connection
    database = sqlite3.connect("weather.db")

# PRE-QGIS__________________________________________________________
#Enable only the next 2 steps, previous to any QGIS transformation
    create_insert_tables()
    export_stations_coordinates()

# POST-QGIS_________________________________________________________
#Comment the previous 2 steps after importing the QGIS CSV files
    clean_imported_csv()
    create_insert_dicofre_concelho()
    get_wind_data()
    create_windroses()
#___________________________________________________________________
    database.close()