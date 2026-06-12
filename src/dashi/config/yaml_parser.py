from pathlib import Path
from typing import Any
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class NoConfigFile(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__()


def parse_yaml(file_path: Path, file_type: str) -> dict:
    """
    Parses the yaml files in the provided file_path and returns their content as a dict
    Args:
        file_path: a Path object representing the folder to parse
        file_type: the type of file parsed, which is used for the function to
            return the sub-dictionnary with the actual content
    Returns:
        a dictionnary representing the content of the yaml file
    """
    files: list = list(file_path.glob("*.y*ml"))

    if not files:
        raise NoConfigFile(f"No YAML config found in {file_path}")

    file = files[0]
    with open(file, "r") as f:
        config: dict[Any, Any] | None = yaml.load(f, Loader=Loader)

    if config is None:
        raise ValueError(f"{file} is empty")
    try:
        return config[file_type]
    except KeyError:
        raise ValueError(
            "There is a problem with the datasource file (the format is incorrect)"
        )
