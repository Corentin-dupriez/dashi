from pathlib import Path
import yaml


class NoConfigFile(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__()


def parse_yaml(file_path: Path, file_type: str) -> dict | None:
    files = list(file_path.glob("*yml"))

    if not files:
        raise NoConfigFile(f"No YAML config found in {file_path}")

    file = files[0]
    with open(file, "r") as f:
        config = yaml.safe_load(f)
    if config is None:
        raise ValueError(f"{file} is empty")
    return config
