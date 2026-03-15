from pathlib import Path
from typing import List, Any, Union
from .config.yaml_parser import parse_yaml, NoConfigFile
import polars as pl
from polars.datatypes import String, Float32, Int32, Date, Unknown


class Datasources:
    DATA_SOURCES_PATH = Path.cwd() / "data_sources"

    def __init__(self) -> None:
        self.sources: List[Datasource] = self.load_sources()

    def load_sources(self):
        sources = []

        try:
            data: dict[Any, Any] = parse_yaml(self.DATA_SOURCES_PATH, "datasources")

            for key, ds_settings in data.items():
                sources.append(
                    Datasource(
                        ds_settings["name"],
                        ds_settings["type"],
                        ds_settings["columns"],
                    )
                )

        except NoConfigFile as e:
            print(e.message)

        return sources

    def find_datasource(self, source_name: str) -> "Datasource":
        try:
            return [source for source in self.sources if source.name == source_name][0]
        except IndexError:
            raise IndexError(
                "The name of the datasource in the dashboard configuration doesn't correspond to any existing datasource"
            )


class Datasource:
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
        schema: dict = {
            col["name"]: self.convert_type_to_pl_datatype(col["type"])
            for col in self.columns
        }
        data: pl.DataFrame = pl.read_csv(self.path, schema=schema)
        return data

    @staticmethod
    def convert_type_to_pl_datatype(
        datatype: str,
    ) -> dict[
        str, Union[type[String], type[Int32], type[Float32], type[Date], type[Unknown]]
    ]:
        datatypes_dict = {
            "string": String,
            "integer": Int32,
            "float": Float32,
            "date": Date,
        }
        return datatypes_dict.get(datatype, Unknown)


if __name__ == "__main__":
    datasoures = Datasources()

    for source in datasoures.sources:
        print(source.data)
