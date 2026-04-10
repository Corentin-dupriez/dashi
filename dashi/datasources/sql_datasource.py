import polars as pl
from dashi.datasources.base_datasource import BaseDatasource
from abc import ABC


class SqlDatasource(BaseDatasource, ABC):
    def __init__(self, source_def: dict, *args, **kwargs) -> None:
        super().__init__(source_def, *args, **kwargs)
        self.query: str = source_def["query"]

    def load_data(self) -> pl.DataFrame:
        raise NotImplementedError
