from .csv_datasource import CsvDatasource
from .json_datasource import JsonDatasource
from .sql_datasource import SqlDatasource

DATASOURCES = {"csv": CsvDatasource, "json": JsonDatasource, "duckdb": SqlDatasource}
