# Portugal Weather Analysis
![Static Badge](https://img.shields.io/badge/language-python-blue) ![GitHub repo size](https://img.shields.io/github/repo-size/:rogernogueraplanesas/:portugal-weather-analysis) ![GitHub last commit](https://img.shields.io/github/last-commit/:rogernogueraplanesas/:portugal-weather-analysis) <br>
Creating wind roses and Atlas maps per municipality for Historical Hourly Wind Records of Mainland Portugal, Açores, and Madeira (2018–2023).
<br>
<br>
<h2>
  <img src="sample_images/requisites.jpg" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Requirements</span>
</h2>

```
pip install -r requirements.txt
```
<br>

<h2>
  <img src="sample_images/summary.jpg" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Summary</span>
</h2>

For this project, multiple JSON files (1.42 GB) containing climate data recorded by various weather stations across Portugal (Mainland and Islands) from 2018 to 2023 were processed by extracting the necessary data and inserting it into a database. Additional data from external sources was then used to complete the database, from which a final dataset was extracted to generate CSV files for wind roses by month, year, and a combined (month + year) basis. These CSV files were later used to create a set of Atlas maps.

> SQLite for the database creation.

> QGIS is used throughout this project.<br>
> Also known as Quantum GIS, is a geographic information system (GIS) software. More information can be found [here](https://qgis.org/en/site/about/index.html).


<br>
<div align="center">
  <img src="sample_images/project_overlay.jpg" width="100%" height="100%" alt="Schematic process">
  <br>
  <sub>Project Workflow</sub>
</div>
<br>


<h2>
  <img src="sample_images/assumption.png" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Project Assumptions</span>
</h2>

- All partially incomplete records are treated as corrupt and disregarded.

- Data from 2018 and 2023 is not complete for the entire year, given the project's duration. Therefore, while it was utilized for monthly historical analysis, it was not represented on any Atlas map.
<br>


<h2>
  <img src="sample_images/postinstall.jpg" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Project Workflow</span>
</h2>

The specific workflow followed in this project can be found in the [documentation file](/docs/project-organisation.md).
<br><br>


<h2>
  <img src="sample_images/execution.png" width="30" height="30" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Instructions</span>
</h2>

The execution of this program is divided into two phases: **before** the QGIS data transformation and **after** importing the merged data files.<br>
- First, navigate to the project's folder using the *cd* command.<br>
- Before running the script, ensure that only the Pre-QGIS functions are active in *'main.py'* script. Comment out the Post-QGIS functions.<br>
- In the main.py script, modify the code as follows:


```
if __name__=="__main__":

# SQLite DB connection
    database = sqlite3.connect("weather.db")

# PRE-QGIS__________________________________________________________
#Enable only the next 2 steps, previous to any QGIS transformation
    create_insert_tables()
    export_stations_coordinates()

# POST-QGIS_________________________________________________________
#Comment the previous 2 steps after importing the QGIS CSV files
    #clean_imported_csv()
    #create_insert_dicofre_concelho()
    #get_wind_data()
    #create_windroses()
#___________________________________________________________________
    database.close()
```
<br>

- Run the following command to execute the **Pre-QGIS phase**:


```
python source/main.py
```
<br>

- This step will insert selected data from the JSON files into a new SQLite database, from which specific stations' metadata will be exported in CSV format into the [stations' data pre-qgis folder](/csv_files/stations_pre_qgis).<br>
- An intersection process between the stations' data and external geographical information must be done by means of QGIS, as explained in the [documentation](/docs/project-organisation.md).<br>
- The resulting files must adhere to the structure defined in the [qgis imported folder](/csv_files/qgis_imported) to ensure smooth continuation of the process.<br><br>
- Once the QGIS transformation is completed, modify the main.py script again to activate the Post-QGIS functions:

```
if __name__=="__main__":

# SQLite DB connection
    database = sqlite3.connect("weather.db")

# PRE-QGIS__________________________________________________________
#Enable only the next 2 steps, previous to any QGIS transformation
    #create_insert_tables()
    #export_stations_coordinates()

# POST-QGIS_________________________________________________________
#Comment the previous 2 steps after importing the QGIS CSV files
    clean_imported_csv()
    create_insert_dicofre_concelho()
    get_wind_data()
    create_windroses()
#___________________________________________________________________
    database.close()
```
<br>

- Execute the script again using the same command:

```
python source/main.py
```
<br>

This will complete the **Post-QGIS phase** and finalize the process.
