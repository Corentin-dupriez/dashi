from pathlib import Path
import polars as pl


class BaseDatasource:
    STAGING_DATA_PATH = Path.cwd() / "staging_data"

    def __init__(self, source_def: dict) -> None:
        self.name: str = source_def["name"]
        self.data_type: str = source_def["type"]

    def __repr__(self) -> str:
        return f"Datasource {self.name}, from {self.data_type}, with columns\n{'\n'.join(f' - {col["name"]}: {col["type"]}' for col in self.columns)}"

    def load_data(self) -> pl.DataFrame:
        raise NotImplementedError
