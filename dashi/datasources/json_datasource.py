from dashi.datasources.base_datasource import BaseDatasource
import polars as pl


class JsonDatasource(BaseDatasource):
    def load_data(self) -> pl.DataFrame:
        schema: dict = self.load_schema()
        return pl.read_json(self.path, schema=schema)
