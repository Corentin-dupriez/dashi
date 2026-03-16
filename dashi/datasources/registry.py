from .csv_datasource import CsvDatasource
from .json_datasource import JsonDatasource

DATASOURCES = {"csv": CsvDatasource, "json": JsonDatasource}
