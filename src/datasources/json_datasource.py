from dashi.datasources.base_datasource import BaseDatasource
from dashi.datasources.file_datasource import FileDatasource
import polars as pl


class JsonDatasource(FileDatasource):
    def load_data(self) -> pl.DataFrame:
        schema: dict = self.load_schema()
        return pl.read_json(self.path, schema=schema)
