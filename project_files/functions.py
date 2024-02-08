import os
import json
import csv
import tables_queries as tq


#________________________Functions used in the main script________________________


#Create the tables in the database
def create_tables(database):
    cursor = database.cursor() 
    cursor.execute(tq.CREATE_STATIONS_TABLE)
    cursor.execute(tq.CREATE_OBSERVATIONS_TABLE)
    database.commit()


#Insert data from the JSON files into the stations table
def insert_stations_data(database, json_path):
    for filename in os.listdir(json_path):
        if "stations" in filename.lower() and filename.endswith(".json"):
            with open(os.path.join(json_path, filename), "r") as file:

                try:
                    data = json.load(file)
                
                except json.decoder.JSONDecodeError as e:
                    print(f"Error loading data from {file}: {e}")
                    continue

                cursor = database.cursor()
                for station in data:
                    cursor.execute(tq.INSERT_STATIONS_DATA,(
                        station["properties"]["idEstacao"],
                        station["geometry"]["coordinates"][0],
                        station["geometry"]["coordinates"][1],
                        station["properties"]["localEstacao"]
                        ))
                database.commit()
                

#Insert data from the JSON files into the observations table
def insert_observations_data(database, json_path):
    for filename in os.listdir(json_path):
        if "observations" in filename.lower() and filename.endswith(".json"):
            with open(os.path.join(json_path, filename), "r") as file:

                try:
                    data = json.load(file)
                
                except json.decoder.JSONDecodeError as e:
                    print(f"Error loading data from {file}: {e}")

                cursor = database.cursor()
                for date, station in data.items():
                    for id, observations in station.items():
                        if observations is not None:
                            cursor.execute(tq.INSERT_OBSERVATIONS_TABLE, (
                                date,
                                id,
                                observations["intensidadeVentoKM"],
                                observations["temperatura"],
                                observations["radiacao"],
                                observations["idDireccVento"],
                                observations["precAcumulada"],
                                observations["intensidadeVento"],
                                observations["humidade"],
                                observations["pressao"]
                                ))
                database.commit()


#Retrieve and fetch all the data from the 'stations' table 
def get_coordinates(database):
    cursor = database.cursor() 
    cursor.execute("""
    SELECT *
    FROM stations;
    """)
    return cursor.fetchall()


#Save fetched station data into a CSV file to then import it based on their coordinates into QGIS
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_estacao', 'latitude', 'longitude', 'local_estacao'])
        writer.writerows(data)



#>>>>>>>> In QGIS, each station will be placed according to their coordinates and intersected with layers to merge data. After the intersection, the stations data is imported in a new csv file grouped by are (qgis_imported folder).

#>>>>>>>> After importing the intersected data from QGIS, each station will present additional values such as dicofre (zip code) and a concelho (municipality) related to them that must be included in the database, new columns are created:
        
        
#Add dicofre and concelho columns in stations table
def add_columns(database):
    cursor = database.cursor()
    cursor.execute(tq.ADD_DICOFRE_COLUMN)
    cursor.execute(tq.ADD_CONCELHO_COLUMN)


#----------------------------------------------------------------------------------------------
#In case it is needed, both columns can be removed
def drop_columns(database):
    cursor = database.cursor()
    cursor.execute(tq.DROP_DICOFRE_COLUMN)
    cursor.execute(tq.DROP_CONCELHO_COLUMN)
#----------------------------------------------------------------------------------------------
    

#>>>>>>>> The data imported from QGIS has all the already known data for each weather station + 'dicofre' and 'concelho'.
    
#>>>>>>>> The CSV files from QGIS must be reduced to only 3 values per row: idestacao (station id // PRIMARY KEY), dicofre (zip code) and concelho (municipality).
    
#>>>>>>>> In the script 'qgis_data_cleaning.py', each imported CSV file from QGIS is cleaned to obtain a cleaned CSV to work with (qgis_cleaned folder). Now 'dicofre' and 'concelho' can be added to the db.
    

#Add 'dicofre' and 'concelho' values per each 'Portugal continental' station into the stations table
def add_portugal_data(database):
    cursor=database.cursor()
    with open("csv_files/qgis_cleaned/cleaned_Portugal_intersect.csv", 'r', encoding='utf-8') as csv_file:
        readed_file = csv.reader(csv_file)
        
        next(readed_file)  # Skip the header row
        
        for row in readed_file:
            id_estacao, dicofre, concelho = row[0], row[1], row[2]

            try:           
                cursor.execute("UPDATE stations SET dicofre = ?, concelho = ? WHERE id_estacao = ?", (dicofre, concelho, id_estacao))

            except Exception as e:
                print(f"There is an error for station {id_estacao}: {e}")
    database.commit()


#Add 'dicofre' and 'concelho' values per each 'Madeira Island' station into the stations table
def add_madeira_data(database):
    cursor = database.cursor()
    with open("csv_files/qgis_cleaned/cleaned_Madeira_intersect.csv", 'r', encoding='utf-8') as csv_file:
        readed_file = csv.reader(csv_file)
        
        next(readed_file)  # Skip the header row
        
        for row in readed_file:
            id_estacao, dicofre, concelho = row[0], row[1], row[2]

            try:           
                cursor.execute("UPDATE stations SET dicofre = ?, concelho = ? WHERE id_estacao = ?", (dicofre, concelho, id_estacao))

            except Exception as e:
                print(f"There is an error for station {id_estacao}: {e}")
    database.commit()

#Add 'dicofre' and 'concelho' values per each 'Central Açores Island' station into the stations table
def add_açores_central_data(database):
    cursor = database.cursor()
    with open("csv_files/qgis_cleaned/cleaned_Açores_Central_intersect.csv", 'r', encoding='utf-8') as csv_file:
        readed_file = csv.reader(csv_file)
        
        next(readed_file)  # Skip the header row
        
        for row in readed_file:
            id_estacao, dicofre, concelho = row[0], row[1], row[2]

            try:           
                cursor.execute("UPDATE stations SET dicofre = ?, concelho = ? WHERE id_estacao = ?", (dicofre, concelho, id_estacao))

            except Exception as e:
                print(f"There is an error for station {id_estacao}: {e}")
    database.commit()


#Add 'dicofre' and 'concelho' values per each 'Occidental Açores Island' station into the stations table
def add_açores_occidental_data(database):
    cursor = database.cursor()
    with open("csv_files/qgis_cleaned/cleaned_Açores_Occidental_intersect.csv", 'r', encoding='utf-8') as csv_file:
        readed_file = csv.reader(csv_file)
        
        next(readed_file)  # Skip the header row
        
        for row in readed_file:
            id_estacao, dicofre, concelho = row[0], row[1], row[2]

            try:           
                cursor.execute("UPDATE stations SET dicofre = ?, concelho = ? WHERE id_estacao = ?", (dicofre, concelho, id_estacao))

            except Exception as e:
                print(f"There is an error for station {id_estacao}: {e}")
    database.commit()


#Add 'dicofre' and 'concelho' values per each 'Oriental Açores Island' station into the stations table
def add_açores_oriental_data(database):
    cursor = database.cursor()
    with open("csv_files/qgis_cleaned/cleaned_Açores_Oriental_intersect.csv", 'r', encoding='utf-8') as csv_file:
        readed_file = csv.reader(csv_file)
        
        next(readed_file)  # Skip the header row
        
        for row in readed_file:
            id_estacao, dicofre, concelho = row[0], row[1], row[2]

            try:           
                cursor.execute("UPDATE stations SET dicofre = ?, concelho = ? WHERE id_estacao = ?", (dicofre, concelho, id_estacao))

            except Exception as e:
                print(f"There is an error for station {id_estacao}: {e}")
    database.commit()


#----------------------------------------------------------------------------------------------
#In case that is needed, both the dicofre and concelho columns can be emptied again:
def empty_conc_dicofr(database):
    cursor = database.cursor()
    try:
        cursor.execute("UPDATE stations SET concelho = NULL, dicofre = NULL")
        database.commit()
        print("Columns 'concelho' and 'dicofre' are emptied successfully.")
    except Exception as e:
        print(f"Error: {e}")
#----------------------------------------------------------------------------------------------


#>>>>>>>> With the db filled, now is time to move on to the data retrieval step.
    
#>>>>>>>> Different queries will be made in order to obtain the required data to create windroses per concelho and year, concelho and month & concelho and year + month.

#>>>>>>>> After the retrieving and fetching, the data is written into new CSV files and stored in the folder 'windrose_csv_data', which contains the final data used to create the windroses.


#Retrieving and fetching data from tables in function of the year
def yearly_windspeed_direction(database):
    cursor = database.cursor()
    cursor.execute(tq.YEARLY_WINDSPEED_DIRECTION)
    return cursor.fetchall()


#Save fetched data into files
def yearly_data_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['year', 'id_estacao', 'dicofre', 'concelho', 'id_direcc_vento', 'min_intensidade_vento', 'max_intensidade_vento', 'avg_intensidade_vento'])
        writer.writerows(data)


#Retrieving and fetching data from tables in function of the month
def monthly_windspeed_direction(database):
    cursor = database.cursor()
    cursor.execute(tq.MONTHLY_WINDSPEED_DIRECTION)
    return cursor.fetchall()


#Save fetched data into files
def monthly_data_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['month', 'id_estacao', 'dicofre', 'concelho', 'id_direcc_vento', 'min_intensidade_vento', 'max_intensidade_vento', 'avg_intensidade_vento'])
        writer.writerows(data)


#Retrieving and fetching data from tables in function of the month and year
def year_month_windspeed_direction(database):
    cursor = database.cursor()
    cursor.execute(tq.YEAR_MONTH_WINDSPEED_DIRECTION)
    return cursor.fetchall()


#Save fetched data into files
def year_month_data_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['month', 'year', 'id_estacao', 'dicofre', 'concelho', 'id_direcc_vento', 'min_intensidade_vento', 'max_intensidade_vento', 'avg_intensidade_vento'])
        writer.writerows(data)


#_______________________The functions related to the windroses creation are written in a separate script (windroses.py)_______________________