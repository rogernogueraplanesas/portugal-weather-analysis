import csv
import os
import tables_queries as tq

# From the completed db, a set of data is retrieved and fetched to create the windroses
# The data is written into new CSV files and stored in the folder 'windrose_csv_data', which contains the final data used to create the windroses.


#Retrieving and fetching data from tables in function of the year
def yearly_windspeed_direction(database):
    cursor = database.cursor()
    cursor.execute(tq.YEARLY_WINDSPEED_DIRECTION)
    return cursor.fetchall()


#Save fetched data into files
def yearly_data_to_csv(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
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
    os.makedirs(os.path.dirname(filename), exist_ok=True)
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
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['month', 'year', 'id_estacao', 'dicofre', 'concelho', 'id_direcc_vento', 'min_intensidade_vento', 'max_intensidade_vento', 'avg_intensidade_vento'])
        writer.writerows(data)
