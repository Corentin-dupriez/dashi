from dashi.datasources.postgres_datasource import PostgresDatasource
from .csv_datasource import CsvDatasource
from .json_datasource import JsonDatasource
from .sql_datasource import SqlDatasource
from .duckdb_datasource import DuckDBDatasource

DATASOURCES = {
    "csv": CsvDatasource,
    "json": JsonDatasource,
    "duckdb": DuckDBDatasource,
    "postgres": PostgresDatasource,
}
