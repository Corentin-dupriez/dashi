from dashi.datasources.base_datasource import BaseDatasource
import duckdb
import polars as pl


class SqlDatasource(BaseDatasource):
    def __init__(self, source_def: dict) -> None:
        super().__init__(source_def)
        self.query = source_def["query"]
        self.path = self.STAGING_DATA_PATH / f"{source_def['name']}.duckdb"

    def load_data(self) -> pl.DataFrame:
        con = duckdb.connect(database=self.path)
        df = con.sql(self.query).pl()
        return df
