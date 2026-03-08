from pathlib import Path
from typing import List
from config.yaml_parser import parse_yaml, NoConfigFile
import polars as pl


class Datasources:
    DATA_SOURCES_PATH = Path.cwd() / "data_sources"

    def __init__(self) -> None:
        self.sources = self.load_sources()

    def load_sources(self):
        sources = []

        try:
            data = parse_yaml(self.DATA_SOURCES_PATH, "datasource")

            ds = data["datasource"]
            sources.append(
                Datasource(
                    ds["name"],
                    ds["type"],
                    ds["columns"],
                )
            )

        except NoConfigFile as e:
            print(e.message)

        return sources


class Datasource:
    STAGING_DATA_PATH = Path.cwd() / "staging_data"

    def __init__(self, name: str, data_type: str, columns: List[dict]) -> None:
        self.name = name
        self.data_type = data_type
        self.columns = columns
        self.path = self.STAGING_DATA_PATH / f"{self.name}.{self.data_type}"
        self.data = self.load_data()

    def __str__(self) -> str:
        return f"Datasource {self.name}, from {self.data_type}, with columns\n{'\n'.join(f' - {col["name"]}: {col["type"]}' for col in self.columns)}"

    def load_data(self) -> pl.DataFrame:
        schema = {
            col["name"]: self.convert_type_to_pl_datatype(col["type"])
            for col in self.columns
        }
        data = pl.read_csv(self.path, schema=schema)
        return data

    @staticmethod
    def convert_type_to_pl_datatype(datatype: str) -> pl.datatypes:
        datatypes_dict = {
            "string": pl.datatypes.String,
            "integer": pl.datatypes.Int32,
            "float": pl.datatypes.Float16,
            "date": pl.datatypes.Date,
        }
        return datatypes_dict.get(datatype, pl.datatypes.Unknown)


if __name__ == "__main__":
    datasoures = Datasources()

    for source in datasoures.sources:
        print(source.data)
