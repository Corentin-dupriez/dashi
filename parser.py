from pathlib import Path
import os
import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def parse_yaml(file_path: Path, yaml_type: str):
    for file in os.listdir(file_path):
        file_path = file_path / file
        with open(file_path, "r") as f:
            data = yaml.load(f, Loader)
    return data if data is not None else None
