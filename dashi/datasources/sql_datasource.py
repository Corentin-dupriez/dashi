from dashi.datasources.base_datasource import BaseDatasource
import polars as pl


class SqlDatasource(BaseDatasource):
    def __init__(self, source_def: dict) -> None:
        super().__init__(source_def)
        self.query: str = source_def["query"]

    def load_data(self) -> pl.DataFrame:
        raise NotImplementedError

