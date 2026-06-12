from pathlib import Path
from typing import List, Union
from dashi.datasources.base_datasource import BaseDatasource
from polars.datatypes import String, Float32, Int32, Date, Unknown


class FileDatasource(BaseDatasource):
    STAGING_DATA_PATH = Path.cwd() / "staging_data"

    def __init__(
        self,
        source_def: dict,
    ) -> None:
        super().__init__(source_def)
        self.columns: List[dict] = source_def["columns"]
        if source_def.get("path") is None:
            self.path: Path = (
                self.STAGING_DATA_PATH / f"{source_def['name']}.{source_def['type']}"
            )
        else:
            self.path = source_def["path"]

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
