from pathlib import Path

folders = ["data_sources", "staging_data", "dashboards"]


def structure_already_present() -> bool:
    if any([Path.exists(Path.cwd() / folder) for folder in folders]):
        return True
    return False


def create_structure() -> None:
    root = Path.cwd()
    for folder in folders:
        new_folder = Path(root / folder)
        new_folder.mkdir()
