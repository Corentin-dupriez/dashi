from pathlib import Path
import polars as pl
from typing import List, Union
from polars.datatypes import String, Float32, Int32, Date, Unknown


class BaseDatasource:
    STAGING_DATA_PATH = Path.cwd() / "staging_data"

    def __init__(
        self, name: str, data_type: str, columns: List[dict], path: str | None = None
    ) -> None:
        self.name: str = name
        self.data_type: str = data_type
        self.columns: List[dict] = columns
        if path is None:
            self.path: Path = self.STAGING_DATA_PATH / f"{self.name}.{self.data_type}"
        else:
            self.path = Path(path)
        self.data: pl.DataFrame = self.load_data()

    def __repr__(self) -> str:
        return f"Datasource {self.name}, from {self.data_type}, with columns\n{'\n'.join(f' - {col["name"]}: {col["type"]}' for col in self.columns)}"

    def load_data(self) -> pl.DataFrame:
        raise NotImplementedError

    def load_schema(self) -> dict:
        schema: dict = {
            col["name"]: self.convert_type_to_pl_datatype(col["type"])
            for col in self.columns
        }
        return schema

    @staticmethod
    def convert_type_to_pl_datatype(
        datatype: str,
    ) -> dict[
        str, Union[type[String], type[Int32], type[Float32], type[Date], type[Unknown]]
    ]:
        datatypes_dict = {
            "string": String,
            "integer": Int32,
            "int32": Int32,
            "float32": Float32,
            "float": Float32,
            "date": Date,
        }
        return datatypes_dict.get(datatype, Unknown)
