import os
import json
import csv
import tables_queries as tq


#Method to create the tables in the database
def create_tables(database):
    cursor = database.cursor() 
    cursor.execute(tq.CREATE_STATIONS_TABLE)
    cursor.execute(tq.CREATE_OBSERVATIONS_TABLE)
    database.commit()


#Function to insert data from the json files into the stations table
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
                

#Functions to insert data from the json files into the observations table
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


#Get stations coordinates to import in QGIS
def get_coordinates(database):
    cursor = database.cursor() 
    cursor.execute("""
    SELECT *
    FROM stations;
    """)
    return cursor.fetchall()


#Save fetched station data into files
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_estacao', 'latitude', 'longitude', 'local_estacao'])
        writer.writerows(data)
        

#Add dicofre and concelho columns in stations table
def add_columns(database):
    cursor = database.cursor()
    cursor.execute("""
                ALTER TABLE stations
                ADD COLUMN dicofre REAL;
                """)
    cursor.execute("""
                   ALTER TABLE stations
                   ADD COLUMN concelho TEXT;
                   """)


#Add 'Portugal continental' data to dicofre and concelho new columns for stations table
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


#Add 'Madeira' data to dicofre and concelho new columns for stations table
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

#Add 'Açores Central' data to dicofre and concelho new columns for stations table
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


#Add 'Açores Occidental' data to dicofre and concelho new columns for stations table
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


#Add 'Açores Oriental' data to dicofre and concelho new columns for stations table
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


#Save fetched data into files
def yearly_data_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['year', 'id_estacao', 'dicofre', 'concelho', 'id_direcc_vento', 'min_intensidade_vento', 'max_intensidade_vento', 'avg_intensidade_vento'])
        writer.writerows(data)


#Save fetched data into files
def monthly_data_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['month', 'id_estacao', 'dicofre', 'concelho', 'id_direcc_vento', 'min_intensidade_vento', 'max_intensidade_vento', 'avg_intensidade_vento'])
        writer.writerows(data)

#Save fetched data into files
def year_month_data_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['month', 'year', 'id_estacao', 'dicofre', 'concelho', 'id_direcc_vento', 'min_intensidade_vento', 'max_intensidade_vento', 'avg_intensidade_vento'])
        writer.writerows(data)