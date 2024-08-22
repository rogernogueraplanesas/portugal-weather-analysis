import csv
import os

# The data imported from QGIS has all the already known data for each weather station + 'dicofre' and 'concelho'.
    
# The CSV files from QGIS must be reduced to only 3 values per row: idestacao (station id // PRIMARY KEY), dicofre (location code) and concelho (municipality).


#Cleaning qgis imported csv file with Portugal continental stations data
def clean_portugal_data(raw_file, clean_file):
    os.makedirs(os.path.dirname(clean_file), exist_ok=True)
    with open(raw_file, 'r', encoding='utf-8') as input_file, open(clean_file, 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            dicofre = row[5]
            
            # Check if the district number has 3 digits
            if len(dicofre) == 3:
                dicofre = '0' + dicofre
            
            writer.writerow([row[0], dicofre, row[6]])


#Cleaning qgis imported csv file with Madeira stations data
def clean_madeira_data(raw_file, clean_file):
    os.makedirs(os.path.dirname(clean_file), exist_ok=True)
    with open(raw_file, 'r', encoding='utf-8') as input_file, open(clean_file, 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            dicofre = row[5]
            
            # Check if the district number has 3 digits
            if len(dicofre) == 3:
                dicofre = '0' + dicofre
            
            writer.writerow([row[0], dicofre, row[6]])


#Cleaning qgis imported csv file with Açores Central stations data
def clean_açores_central_data(raw_file, clean_file):
    os.makedirs(os.path.dirname(clean_file), exist_ok=True)
    with open(raw_file, 'r', encoding='utf-8') as input_file, open(clean_file, 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            dicofre = row[5]
            
            # Check if the district number has 3 digits
            if len(dicofre) == 3:
                dicofre = '0' + dicofre
            
            writer.writerow([row[0], dicofre, row[6]])


#Cleaning qgis imported csv file with Açores Occidental stations data
def clean_açores_occidental_data(raw_file, clean_file):
    os.makedirs(os.path.dirname(clean_file), exist_ok=True)
    with open(raw_file, 'r', encoding='utf-8') as input_file, open(clean_file, 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            dicofre = row[5]
            
            # Check if the district number has 3 digits
            if len(dicofre) == 3:
                dicofre = '0' + dicofre
            
            writer.writerow([row[0], dicofre, row[6]])


#Cleaning qgis imported csv file with Açores Oriental stations data
def clean_açores_oriental_data(raw_file, clean_file):
    os.makedirs(os.path.dirname(clean_file), exist_ok=True)
    with open(raw_file, 'r', encoding='utf-8') as input_file, open(clean_file, 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            dicofre = row[5]
            
            # Check if the district number has 3 digits
            if len(dicofre) == 3:
                dicofre = '0' + dicofre
            
            writer.writerow([row[0], dicofre, row[6]])