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

For this project, multiple files in **JSON** format (1.42 GB) containing climate data from 2018 to 2023 registered by different weather stations in Portugal (Mainland and Islands), were cleaned, formatted, and transformed into **CSV** files in order to create proper wind roses per municipality on a yearly, monthly, and yearly + monthly basis.<br> A set of Atlas maps was created using the resulting wind roses.

> SQLite for the database creation.

> QGIS is used throughout this project.<br>
> Also known as Quantum GIS, is a geographic information system (GIS) software. More information can be found [here](https://qgis.org/en/site/about/index.html).
<br>
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
  <span style="vertical-align: middle;">Project Organisation</span>
</h2>

The process followed in this project can be consulted in the [documentation file](/docs/project-organisation.md).
