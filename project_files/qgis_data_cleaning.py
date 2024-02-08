import csv

#Cleaning imported csv file with Portugal continental stations data
def clean_portugal_data():
    with open("csv_files/qgis_imported/stations_intersected_portugal_continental.csv", 'r', encoding='utf-8') as input_file, open("csv_files/qgis_cleaned/cleaned_Portugal_intersect.csv", 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            dicofre = row[5]
            
            # Check if the district number has 3 digits
            if len(dicofre) == 3:
                dicofre = '0' + dicofre
            
            writer.writerow([row[0], dicofre, row[6]])


#Cleaning imported csv file with Madeira stations data
def clean_madeira_data():
    with open("csv_files/qgis_imported/stations_intersected_madeira.csv", 'r', encoding='utf-8') as input_file, open("csv_files/qgis_cleaned/cleaned_Madeira_intersect.csv", 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            dicofre = row[5]
            
            # Check if the district number has 3 digits
            if len(dicofre) == 3:
                dicofre = '0' + dicofre
            
            writer.writerow([row[0], dicofre, row[6]])


#Cleaning imported csv file with Açores Central stations data
def clean_açores_central_data():
    with open("csv_files/qgis_imported/stations_intersected_açores_central.csv", 'r', encoding='utf-8') as input_file, open("csv_files/qgis_cleaned/cleaned_Açores_Central_intersect.csv", 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            dicofre = row[5]
            
            # Check if the district number has 3 digits
            if len(dicofre) == 3:
                dicofre = '0' + dicofre
            
            writer.writerow([row[0], dicofre, row[6]])


#Cleaning imported csv file with Açores Occidental stations data
def clean_açores_occidental_data():
    with open("csv_files/qgis_imported/stations_intersected_açores_occidental.csv", 'r', encoding='utf-8') as input_file, open("csv_files/qgis_cleaned/cleaned_Açores_Occidental_intersect.csv", 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            dicofre = row[5]
            
            # Check if the district number has 3 digits
            if len(dicofre) == 3:
                dicofre = '0' + dicofre
            
            writer.writerow([row[0], dicofre, row[6]])


#Cleaning imported csv file with Açores Oriental stations data
def clean_açores_oriental_data():
    with open("csv_files/qgis_imported/stations_intersected_açores_oriental.csv", 'r', encoding='utf-8') as input_file, open("csv_files/qgis_cleaned/cleaned_Açores_Oriental_intersect.csv", 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            dicofre = row[5]
            
            # Check if the district number has 3 digits
            if len(dicofre) == 3:
                dicofre = '0' + dicofre
            
            writer.writerow([row[0], dicofre, row[6]])