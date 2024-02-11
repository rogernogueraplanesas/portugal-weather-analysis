# Portugal Weather Analysis
Wind Roses per municipality for Historical Hourly Wind Records of Mainland Portugal, Açores, and Madeira (2018–2023)

## Objective Summary
For this project, multiple files in **JSON** format (1.42 GB) containing climate data from different weather stations in Portugal (Mainland and Islands) were cleaned, formatted, and transformed into **CSV** files in order to create proper wind roses per municipality on a yearly, monthly, and yearly + monthly basis.

> An SQLite database is created in order to store all the processed data in a practical way to check and re-use it.

> QGIS software is used in this project. <br>
> QGIS, also known as Quantum GIS, is a geographic information system (GIS) software that is free and open-source. It takes part in several steps, such as providing complementary data in function of the geolocation of each weather station as well as creating the final Atlas maps from the resulting wind roses.

## Project Assumptions
- All partially incomplete records are treated as corrupt and disregarded.

- Data from 2018 and 2023 is not complete for the entire year, given the project's duration. Therefore, while it was utilized for monthly historical analysis, it was not represented on a yearly basis.

## Project Organization
The project can be divided into seven distinct steps.

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
<br> 
<div align="center">
  <img src="sample_images/observations_table.png" width="80%" height="80%" alt="Observations table">
  <br style="margin-bottom: 0.25em;">
  <sub>Observations table structure</sub>
</div>
<br>

### Exporting station data into QGIS
With both tables filled out with data from the data source, there are two more key parameters missing. Despite having data regarding the stations and their readings, there is no column assigned to the location of the weather stations, except for the coordinates themselves.

For this project, it is crucial to locate the stations in a specific *'concelho'* (municipality) with their respective *'dicofre'* numbers (zip code numbers). The final windroses will be created based on each concelho found in Portugal. The dicofre number is a key value for organizational purposes, as the resulting windrose files must contain the dicofre value in their name.

QGIS is involved in the relational part where each station gets a concelho and dicofre value in function of the geocoordinates.
