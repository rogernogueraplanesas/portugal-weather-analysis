import csv
import tables_queries as tq


#Add dicofre and concelho columns in stations table
def add_columns(database):
    cursor = database.cursor()
    cursor.execute(tq.ADD_DICOFRE_COLUMN)
    cursor.execute(tq.ADD_CONCELHO_COLUMN)
    database.commit()


#--------------------------------------------------
# IN CASE OF NEEDING TO REMOVE THE NEW COLUMNS:
#--------------------------------------------------
def drop_columns(database):
    cursor = database.cursor()
    cursor.execute(tq.DROP_DICOFRE_COLUMN)
    cursor.execute(tq.DROP_CONCELHO_COLUMN)
    database.commit()
#--------------------------------------------------
 

#Add 'dicofre' and 'concelho' values per each 'Portugal continental' station into the stations table
def add_portugal_data(database, cleaned_file):
    cursor=database.cursor()
    with open(cleaned_file, 'r', encoding='utf-8') as csv_file:
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
def add_madeira_data(database, cleaned_file):
    cursor = database.cursor()
    with open(cleaned_file, 'r', encoding='utf-8') as csv_file:
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
def add_açores_central_data(database, cleaned_file):
    cursor = database.cursor()
    with open(cleaned_file, 'r', encoding='utf-8') as csv_file:
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
def add_açores_occidental_data(database, cleaned_file):
    cursor = database.cursor()
    with open(cleaned_file, 'r', encoding='utf-8') as csv_file:
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
def add_açores_oriental_data(database, cleaned_file):
    cursor = database.cursor()
    with open(cleaned_file, 'r', encoding='utf-8') as csv_file:
        readed_file = csv.reader(csv_file)
        
        next(readed_file)  # Skip the header row
        
        for row in readed_file:
            id_estacao, dicofre, concelho = row[0], row[1], row[2]

            try:           
                cursor.execute("UPDATE stations SET dicofre = ?, concelho = ? WHERE id_estacao = ?", (dicofre, concelho, id_estacao))

            except Exception as e:
                print(f"There is an error for station {id_estacao}: {e}")
    database.commit()