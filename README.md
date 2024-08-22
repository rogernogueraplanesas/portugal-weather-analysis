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
For this project, multiple files in **JSON** format (1.42 GB) containing climate data from different weather stations in Portugal (Mainland and Islands) were cleaned, formatted, and transformed into **CSV** files in order to create proper wind roses per municipality on a yearly, monthly, and yearly + monthly basis. A set of Atlas maps was created using the resulting wind roses.

> SQLite for the database creation.

> QGIS is used throughout this project.<br>
> Also known as Quantum GIS, is a geographic information system (GIS) software. More information can be found [here](https://qgis.org/en/site/about/index.html).
<br>
<br>
<div align="center">
  <img src="sample_images/project_overlay.jpg" width="95%" height="100%" alt="Schematic process">
  <br>
  <sub>Schematic process</sub>
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
  <img src="sample_images/docs.jpg" width="25" height="25" alt="Icon" style="vertical-align: middle;"/> 
  <span style="vertical-align: middle;">Project Organization</span>
</h2>
The project can be divided into six distinct steps.
<br>

### 1. Database structuring, and preliminary data insertion
The raw data source consists of several JSON files divided into two main groups: one containing metadata related to the involved Portuguese weather stations, and the other containing data related to hourly observations made by the weather stations between 2018 and 2023.

The first step of the project consisted on the creation of two different tables inside a new locally stored SQLite database named `weather.db`.
The table containing stations' data was named `stations`, and the one containing records from each station was named `observations`.

All the raw data was processed and inserted into each corresponding table.

<br>
<div align="center">
  <img src="sample_images/stations_table.png" width="35%" height="35%" alt="Stations table">
  <br>
  <sub>Stations table structure</sub>
</div>
<br>
<br> 
<div align="center">
  <img src="sample_images/observations_table.png" width="80%" height="80%" alt="Observations table">
  <br style="margin-bottom: 0.25em;">
  <sub>Observations table structure</sub>
</div>


### 2. Exporting stations' data as a CSV
With both tables filled out with data, there were two more key parameters missing. Despite having data regarding the stations and their readings, there was no column assigned to the location of the weather stations, except for the coordinates themselves.

For this project, it was crucial to locate the stations in a specific *'concelho'* (municipality) with their respective *'dicofre'* code.<br>
The final windroses are created based on each concelho found in Portugal. The dicofre number is a key code representing a unique combination of *'distrito'* (district) + *'concelho'* (municipality) + *'freguesia'* (parish); moreover, it is useful for organizational purposes, as the resulting windroses will be easier to locate, group or filter.

All the data inside the `stations` table was retrieved and fetched into a CSV file that was imported into QGIS.

QGIS is involved in the relational part, where each station gets a concelho name and dicofre value as a result of their geocoordinates.
<br>

### 3. QGIS layers intersection
An already existing QGIS project was used as a base to import the stations' data.
The QGIS project had multipolygon layers delineating each of the concelhos found in Portugal (mainland and islands), covering the total area of the country (projected base map).
Each multipolygon contained a set of attributes with data related to the area covered, such as the concelho's name, the dicofre code, the area's size, height, etc.

The stations' data CSV file was imported into QGIS as a point layer.
For each station, one point would be represented on the map according to their geocoordinates (latitude and longitude columns), located somewhere over the already existing multipolygons.

<br>
<div align="center">
  <img src="sample_images/weather_stations.png" width="50%" height="50%" alt="Stations location in QGIS">
  <br>
  <sub>Weather stations location</sub>
</div>
<br>

Once imported, the new points layer (stations' data) and the QGIS project's multipolygon layer were merged by means of the 'intersection' tool from QGIS, which intersects two selected layers creating a new one containing all of their data combined. This new layer's information was then exported as a new CSV file to work with.

> [!NOTE]
> Both the multipolygonal layers and the imported points layer were using the `EPSG:4326 - WGS 84` Coordinate Reference System (CRS).


> [!WARNING]
> It is important to select UTF-8 as encoding type when importing and exporting the CSV files from QGIS.


### 4. Cleaning and inserting QGIS merged data into the db
The CSV file exported from QGIS had many new information appended related to the weather stations; not all of it had to be used. In fact, only the id_estacao (station id), the concelho's name, and the dicofre's code for each station were needed.
<br>
Although the id_estacao value was already present in the stations table, its condition of **PRIMARY KEY** was needed for the proper insertion of the concelho and dicofre values per station.
<br>
Two new columns were created, and the values for the concelho and dicofre per station were inserted based on each id_estacao. Now both tables in the database were totally complete.
<br>

### 5. Retrieving wind data and plotting the final windroses
By means of an inner join, data from both stations and observations table is retrieved in order to collect the required information needed to plot windroses per concelho on a yearly, monthly, and yearly + monthly basis.<br>
An example of a query written to obtain yearly wind data is shown next:

```ruby
YEARLY_WINDSPEED_DIRECTION = """
SELECT strftime('%Y', o.date) as year,
    s.id_estacao,
    CAST(s.dicofre AS INTEGER) as dicofre,
    s.concelho,
    CASE
                WHEN o.id_direcc_vento IN (1, 9) THEN 1.0
                ELSE o.id_direcc_vento
    END AS direcc_vento,
    MIN(o.intensidade_de_vento) as min_int_vento,
    MAX(o.intensidade_de_vento) as max_int_vento,
    ROUND(AVG(o.intensidade_de_vento), 2) as avg_int_vento
FROM observations o
INNER JOIN stations s ON o.id_estacao = s.id_estacao
WHERE o.intensidade_de_vento != -99 AND o.id_direcc_vento != 0
GROUP BY year, dicofre, direcc_vento;
"""
```

As seen in the code block above, the wind direction (id_direcc_vento) was represented with a specific code from 1.0 (N) to 8.0 (NW).<br>
Moreover, any windspeed (intensidade_de_vento) presenting a value of -99 was treated as an error and not taken into account.<br>
The windspeed bar per direction was supposed to contain the minimum, the maximum and the average values recorded in the concelho during specific the span of time represented.
<br>
For the final windroses, *_pandas_*, *_matplotlib_* and *_numpy_* were used.
The values for the wind direction were transformed into degrees (fractions of 45º).<br>
The resultant windroses presented the following appearance:<br>

<br>
<div align="center">
  <img src="sample_images/1106_Lisboa_2018.png" width="42%" height="42%" alt="Lisboa 2018 yearly windrose">
  <br>
  <sub>Lisboa 2018 windrose</sub>
</div>
<br>

> [!NOTE]
> Given the significant difference in windspeed values between the maximum and the minimum, there may be windroses where it can be difficult to distinguish the minimum wind speed value due to the scale.


### 6. Atlas maps
For company purposes, the final wind roses were included in a set of atlas maps that showed the monthly and annual variation of the wind in each municipality during the period of time studied. The final composition of the maps is seen in the following images:

<br>
<div align="center">
  <img src="sample_images/Lisboa-atlas-1.png" width="60%" height="60%" alt="Lisboa Atlas Map 1st page">
  <br>
  <sub>Lisboa Atlas Map 1st page</sub>
</div>
<br>

<br>
<div align="center">
  <img src="sample_images/Lisboa-atlas-2.png" width="60%" height="60%" alt="Lisboa Atlas Map 2nd page">
  <br>
  <sub>Lisboa Atlas Map 2nd page</sub>
</div>
<br>

<br>
<div align="center">
  <img src="sample_images/Lisboa-atlas-3.png" width="60%" height="60%" alt="Lisboa Atlas Map 3rd page">
  <br>
  <sub>Lisboa Atlas Map 3rd page</sub>
</div>
<br>

> The QGIS Atlas is a true open source technique to generate hundreds of maps in minutes. In the map-making business, this means being efficient without compromising art and intricacy. More information [here](https://gisgeography.com/how-to-create-qgis-atlas-mapbooks/).
