# Portugal Weather Analysis
![Static Badge](https://img.shields.io/badge/language-python-blue) ![GitHub repo size](https://img.shields.io/github/repo-size/:rogernogueraplanesas/:portugal-weather-analysis) ![GitHub last commit](https://img.shields.io/github/last-commit/:rogernogueraplanesas/:portugal-weather-analysis) <br>
Wind roses and Atlas maps generator per municipality for Historical Hourly Wind Records of Mainland Portugal, Açores, and Madeira (2018–2023).
<br>
<br>
<h2>
  <img src="sample_images/requisites.jpg" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Requirements</span>
</h2>

```
pip install -r requirements.txt
```
> It is recommended to set up a virtual environment (venv) first.
<br>

<h2>
  <img src="sample_images/toc.jpg" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Table of Contents</span>
</h2>

[Summary](#summary)

[Folders and files](#folders-and-files)

[Project Assumptions](#project-assumptions)

[Project Workflow](#project-workflow)

[Instructions](#instructions)

<br>

<h2 id="summary">
  <img src="sample_images/summary.jpg" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Summary</span>
</h2>

For this project, multiple **JSON files** (1.42 GB) containing raw climate data recorded by various weather stations across Portugal (Mainland and Islands) from **2018 to 2023** were processed by extracting the necessary data and inserting it into a new **database**.<br>
Additional geodata from **external sources** was then used to complete the database, from which final datasets were extracted as **CSV files** in order to create wind roses by month, year, and a combined (month + year) basis. These wind roses were later used to create sets of Atlas maps.

> SQLite for the database creation.

> QGIS is used throughout this project.<br>
> Also known as Quantum GIS, is a geographic information system (GIS) software. More information [here](https://qgis.org/en/site/about/index.html).


<br>
<div align="center">
  <img src="sample_images/project_overlay.jpg" width="100%" height="100%" alt="Project Workflow">
  <br>
  <sub>Project Workflow</sub>
</div>
<br>

<br>

<h2 id="folders-and-files">
  <img src="sample_images/docs.jpg" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Folders and files</span>
</h2>

**[csv_files](/csv_files)**: Folder containing sets of CSV files generated during the project.
  - **qgis_cleaned**: *AUTOMATICALLY GENERATED ALONG THE EXECUTION*. Folder containing a clean version of the CSV files imported from QGIS after the merging process.
  - **qgis_imported**: ***MANUALLY FILL BY THE USER***. Pre-existing folder used to contain the resulting CSV files generated after mergining the weather stations' metadata and the external geodata by means of QGIS. Key step before running the second phase of the execution.
  - **stations_pre_qgis**: *AUTOMATICALLY GENERATED ALONG THE EXECUTION*. Folder with a single CSV file containing all weather stations' metadata
  - **windrose_csv_data**: *AUTOMATICALLY GENERATED ALONG THE EXECUTION*. Folder containing clean prepared weather data to produce the final wind roses.

**[docs](/docs)**: Folder for documentation.
  - **[project-organisation.md](docs/project-organisation.md)**: Document describing step by step the process followed along the project. (Important to read)

**[sample_images](/sample_images)**: Folder containing images used in the repository.

**[source](/source)**: Includes all the .py files.
  - **fill_db_extract.py**: Script to create the db, extract important data from the data source (JSON files), fill the db, and extract specific metadata from the stations in a single CSV ('stations_pre_qgis' folder).
  - **main.py**: Script with the main code of the program. *Script to be executed by the user, as explained in [Instructions](#instructions).*
  - **qgis_data_clean.py**: Script to clean the raw CSV files obtained after the merging process by means of QGIS.
  - **qgis_data_insert.py**: Script to add new columns into the db and fill them with clean QGIS data for each station. Database completion.
  - **settings.py**: Script with the required utilities.
  - **table_queries.py**: Script containing all the SQL queries used along the project.
  - **wind_data_extract.py**: Script to retrieve data from the completed database and generate CSV files with data to produce the final wind roses (according to the required temporality).
  - **windroses.py**: Script to generate the final set of wind roses.

**month_windroses/**: *AUTOMATICALLY GENERATED ALONG THE EXECUTION*. Folder containing the resulting monthly based wind roses per concelho.

**year_windroses/**: *AUTOMATICALLY GENERATED ALONG THE EXECUTION*. Folder containing the resulting yearly based wind roses per concelho.

**year_month_windroses/**: *AUTOMATICALLY GENERATED ALONG THE EXECUTION*. Folder containing the resulting monthly+yearly based wind roses per concelho.

**Other files**:
- **.gitignore**: Specifies the files that are present in the local repository but not in the remote version.
- **requirements.txt**: Needed libraries to execute the program. *It is important to have them all installed.*
  
<br>

<h2 id="project-assumptions">
  <img src="sample_images/assumption.png" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Project Assumptions</span>
</h2>

- All partially incomplete records are treated as corrupt and disregarded.

- Data from 2018 and 2023 is not complete for the entire year, given the project's duration. Therefore, while it was utilized for monthly historical analysis, it was not represented on any Atlas map.
<br>


<h2 id="project-workflow">
  <img src="sample_images/postinstall.jpg" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Project Workflow</span>
</h2>

The specific workflow followed in this project can be found in the [documentation file](/docs/project-organisation.md).
<br><br>


<h2 id="instructions">
  <img src="sample_images/execution.png" width="25" height="26" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Instructions</span>
</h2>

> [!IMPORTANT]
> This repository contains **no real data** due to a non-disclosure agreement. Instead, it includes dummy files that replicate the real structure.
> Please ensure to remove the **'test_'** prefix from the folder names *test_data_20231002/* and *test_csv_files* folders.

> [!NOTE]
> The folder *data_20231002/* contains only two files, **representing one for each file type** (observation data and station metadata). As previously mentioned, in the actual scenario, there should be thousands of such files.
> The *test_csv_files* folder contains exactly **five files**, which are expected after the QGIS intersection process. Only a small portion of their information is visible.

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
- The resulting files must adhere to the structure defined in the [qgis imported folder](/csv_files/qgis_imported) to ensure smooth continuation of the process.<br>
- **IMPORTANT**: Move the new generated CSV files from QGIS into [qgis_imported](csv_files/qgis_imported/) in order to proceed with the execution of the program.
- Once the QGIS step is completed and the new files are placed into their corresponding folder, modify the main.py script again to activate the Post-QGIS functions:

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
