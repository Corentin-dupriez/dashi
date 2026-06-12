from pathlib import Path
from dashi.datasources.sql_datasource import SqlDatasource
import duckdb
import polars as pl


class DuckDBDatasource(SqlDatasource):
    def __init__(self, source_def: dict) -> None:
        super().__init__(source_def)
        self.path: Path = self.STAGING_DATA_PATH / f"{source_def['name']}.duckdb"

    def load_data(self) -> pl.DataFrame:
        con = duckdb.connect(database=self.path)
        df: pl.DataFrame = con.sql(self.query).pl()
        return df
