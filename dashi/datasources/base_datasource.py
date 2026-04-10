import polars as pl
from abc import ABC
from pathlib import Path


class BaseDatasource(ABC):
    STAGING_DATA_PATH = Path.cwd() / "staging_data"

    def __init__(self, source_def: dict, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name: str = source_def["name"]
        self.data_type: str = source_def["type"]

    def __repr__(self) -> str:
        return f"Datasource {self.name}, from {self.data_type}"

    def load_data(self) -> pl.DataFrame:
        raise NotImplementedError
