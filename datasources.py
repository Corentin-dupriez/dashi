from pathlib import Path
from typing import List
from parser import parse_yaml
import polars


class Datasources:
    DATA_SOURCES_PATH = Path(Path.cwd()) / "data_sources"

    def __init__(self) -> None:
        self.sources = self.load_sources()

    def load_sources(self):
        sources = []

        data = parse_yaml(self.DATA_SOURCES_PATH, "datasource")

        ds = data["datasource"]

        sources.append(
            Datasource(
                ds["name"],
                ds["type"],
                ds["columns"],
            )
        )
        return sources


class Datasource:
    STAGING_DATA_PATH = Path(Path.cwd()) / "staging_data"

    def __init__(self, name: str, data_type: str, columns: List[dict]) -> None:
        self.name = name
        self.data_type = data_type
        self.columns = columns
        self.path = self.STAGING_DATA_PATH / f"{self.name}.{self.data_type}"
        self.data = self.load_data()

    def __str__(self) -> str:
        return f"Datasource {self.name}, from {self.data_type}, with columns\n{'\n'.join(f' - {list(value)[0]}: {list(value)[1]}' for value in [el.values() for el in self.columns])}"

    def load_data(self) -> polars.DataFrame:
        schema = {
            list(value)[0]: self.convert_type_to_polars_datatype(list(value)[1])
            for value in [el.values() for el in self.columns]
        }
        print(schema)
        data = polars.read_csv(self.path, schema=schema)
        return data

    @staticmethod
    def convert_type_to_polars_datatype(datatype: str) -> polars.datatypes:
        datatypes_dict = {
            "string": polars.datatypes.String,
            "integer": polars.datatypes.Int32,
            "float": polars.datatypes.Float16,
            "date": polars.datatypes.Date,
        }
        return datatypes_dict[datatype]


datasoures = Datasources()

for source in datasoures.sources:
    print(source.data)
