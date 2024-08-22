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
def insert_stations_data(database, raw_data_path):
    for filename in os.listdir(raw_data_path):
        if "stations" in filename.lower() and filename.endswith(".json"):
            with open(os.path.join(raw_data_path, filename), "r") as file:

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
def insert_observations_data(database, raw_data_path):
    for filename in os.listdir(raw_data_path):
        if "observations" in filename.lower() and filename.endswith(".json"):
            with open(os.path.join(raw_data_path, filename), "r") as file:

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
    cursor.execute(tq.GET_STATIONS_DATA)
    return cursor.fetchall()


#Save stations data into a CSV file to import it into QGIS
def save_to_csv(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_estacao', 'latitude', 'longitude', 'local_estacao'])
        writer.writerows(data)