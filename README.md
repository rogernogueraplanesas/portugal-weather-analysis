# Portugal Weather Analysis
Wind Roses per municipality for Historical Hourly Wind Records of Mainland Portugal, Açores, and Madeira (2018–2023)

## Objective Summary
For this project, multiple files in **JSON** format (1.42 GB) containing climate data from different weather stations in Portugal (Mainland and Islands) were cleaned, formatted, and transformed into **CSV** files in order to create proper wind roses per municipality on a yearly, monthly, and yearly + monthly basis.

> An SQLite database is created in order to store all the processed data in a practical way to check and re-use it.

> QGIS takes part in several steps, such as providing complementary data in function of the geolocation of each weather station as well as creating the final Atlas maps from the resulting wind roses.

## Project Assumptions
All partially incomplete records will be treated as corrupt and disregarded.
Data from 2018 and 2023 is not complete for the entire year, given the project's duration. Therefore, while it will be utilized for monthly historical analysis, it will not be represented on a yearly basis.
