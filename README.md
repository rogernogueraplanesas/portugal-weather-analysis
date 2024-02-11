# Portugal Weather Analysis
Wind Roses per municipality for Historical Hourly Wind Records of Mainland Portugal, Açores, and Madeira (2018–2023)

## Objective Summary
For this project, multiple files in **JSON** format (1.42 GB) containing climate data from different weather stations in Portugal (Mainland and Islands) were cleaned, formatted, and transformed into **CSV** files in order to create proper wind roses per municipality on a yearly, monthly, and yearly + monthly basis.

> An SQLite database is created in order to store all the processed data in a practical way to check and re-use it.

> QGIS takes part in several steps, such as providing complementary data in function of the geolocation of each weather station as well as creating the final Atlas maps from the resulting wind roses.

## Project Assumptions
- All partially incomplete records are treated as corrupt and disregarded.

- Data from 2018 and 2023 is not complete for the entire year, given the project's duration. Therefore, while it was utilized for monthly historical analysis, it was not represented on a yearly basis.

## Project Organization
The project has been divided into seven distinct steps.

### Database structuring, and preliminary data insertion
The datasource consists of several JSON files divided into two main groups: one containing data related to the involved Portuguese weather stations, and the other containing data related to hourly observations made by the weather stations between 2018 and 2022.

The first step of the project consisted of the creation of two different tables inside a new SQLite database named `weather.db`.
The table containing stations' data was named `stations` and the one containing records from each station was named `observations`.

All the JSON files were processed, and the main data extracted from them was inserted into each corresponding table.


<br>
<div align="center">
  <img src="sample_images/stations_table.png" width="35%" height="35%" alt="Stations table">
  <br>
  <sub>Stations table structure</sub>
</div>
<br> 
<div align="center">
  <img src="sample_images/observations_table.png" width="75%" height="75" alt="Observations table">
  <br> 
  <sub>Observations table structure</sub>
</div>

