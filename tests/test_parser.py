from dashi.config.yaml_parser import NoConfigFile, parse_yaml
import pytest
from pathlib import Path


def test_parse_missing_yaml_raises():
    with pytest.raises(NoConfigFile):
        parse_yaml(Path.cwd() / "non_existing_file.yml", "test_file")
