from pathlib import Path
from typing import List, Any
from dashi.config.yaml_parser import parse_yaml, NoConfigFile
from dashi.datasources.registry import DATASOURCES
from .base_datasource import BaseDatasource


class Datasources:
    DATA_SOURCES_PATH = Path.cwd() / "data_sources"

    def __init__(self) -> None:
        self.sources: List[BaseDatasource] = self.load_sources()

    def load_sources(self):
        sources = []

        try:
            data: dict[Any, Any] = parse_yaml(self.DATA_SOURCES_PATH, "datasources")

            for ds_settings in data:
                sources.append(DATASOURCES[ds_settings["type"]](ds_settings))

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
