from dashi.datasources.base_datasource import BaseDatasource
import polars as pl


# TODO: move stuff that is specific to csv from BaseDatasource here
class CsvDatasource(BaseDatasource):
    def load_data(self) -> pl.DataFrame:
        schema: dict = self.load_schema()
        data: pl.DataFrame = pl.read_csv(self.path, schema=schema)
        return data
