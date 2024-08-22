#Command to create the tabe stations
CREATE_STATIONS_TABLE = """
CREATE TABLE IF NOT EXISTS stations (
    id_estacao INTEGER PRIMARY KEY,
    longitude REAL,
    latitude REAL,
    local_estacao TEXT
);
"""


#Command to create the stations table
CREATE_OBSERVATIONS_TABLE = """
CREATE TABLE IF NOT EXISTS observations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    id_estacao INTEGER,
    intensidade_de_vento_km REAL,
    temperatura REAL,
    radiacao REAL,
    id_direcc_vento REAL,
    prec_acumulada REAL,
    intensidade_de_vento REAL,
    humidade REAL,
    pressao REAL,
    FOREIGN KEY (id_estacao) REFERENCES stations(id_estacao)
);
"""


#Command to insert data into stations table
INSERT_STATIONS_DATA = """
INSERT OR REPLACE INTO stations(id_estacao, longitude, latitude, local_estacao)
VALUES (?, ?, ?, ?)
"""


#Command to insert data into observations table
INSERT_OBSERVATIONS_TABLE = """
INSERT INTO observations(date, id_estacao, intensidade_de_vento_km, temperatura, radiacao, id_direcc_vento, prec_acumulada, intensidade_de_vento, humidade, pressao)
VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

#Command to retrieve all data inside 'stations' table
GET_STATIONS_DATA = """
SELECT *
FROM stations;
"""

#Command to add a column 'dicofre' into the stations table
ADD_DICOFRE_COLUMN = """
ALTER TABLE stations
ADD COLUMN dicofre REAL;
"""


#Command to add a column 'dicofre' into the stations table
ADD_CONCELHO_COLUMN = """
ALTER TABLE stations
ADD COLUMN concelho TEXT;
"""


#Command to remove a column 'dicofre' into the stations table
DROP_DICOFRE_COLUMN = """
ALTER TABLE stations
DROP COLUMN dicofre;
"""


#Command to remove a column 'dicofre' into the stations table
DROP_CONCELHO_COLUMN = """
ALTER TABLE stations
DROP COLUMN concelho;
"""


#Query to get yearly windspeed and direction data
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


#Query to get monthly windspeed and direction data
MONTHLY_WINDSPEED_DIRECTION = """
SELECT strftime('%m', o.date) as month,
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
GROUP BY month, dicofre, direcc_vento;
"""


#Query to get yearly+monthly windspeed and direction data
YEAR_MONTH_WINDSPEED_DIRECTION = """
SELECT strftime('%m', o.date) as month,
    strftime('%Y', o.date) as year,
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
GROUP BY month, year, dicofre, direcc_vento;
"""
