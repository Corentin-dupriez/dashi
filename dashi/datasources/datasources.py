from pathlib import Path
from typing import List, Any
from config.yaml_parser import parse_yaml, NoConfigFile
from .base_datasource import BaseDatasource


class Datasources:
    DATA_SOURCES_PATH = Path.cwd() / "data_sources"

    def __init__(self) -> None:
        self.sources: List[BaseDatasource] = self.load_sources()

    def load_sources(self):
        sources = []

        try:
            data: dict[Any, Any] = parse_yaml(self.DATA_SOURCES_PATH, "datasources")

            for _, ds_settings in data.items():
                sources.append(
                    BaseDatasource(
                        ds_settings["name"],
                        ds_settings["type"],
                        ds_settings["columns"],
                    )
                )

        except NoConfigFile as e:
            print(e.message)

        return sources

    def find_datasource(self, source_name: str) -> BaseDatasource:
        try:
            return [source for source in self.sources if source.name == source_name][0]
        except IndexError:
            raise IndexError(
                "The name of the datasource in the dashboard configuration doesn't correspond to any existing datasource"
            )


if __name__ == "__main__":
    datasoures = Datasources()

    for source in datasoures.sources:
        print(source.data)
