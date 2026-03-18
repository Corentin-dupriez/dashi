from dashi.datasources.base_datasource import BaseDatasource
from dashi.datasources.file_datasource import FileDatasource
import polars as pl


class CsvDatasource(FileDatasource):
    def __init__(self, source_def: dict) -> None:
        super().__init__(source_def)

    def load_data(self) -> pl.DataFrame:
        schema: dict = self.load_schema()
        data: pl.DataFrame = pl.read_csv(self.path, schema=schema)
        return data
