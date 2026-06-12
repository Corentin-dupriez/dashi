from pathlib import Path


def clean_builds() -> None:
    """
    Deletes the existing files in the builds directory.
    """
    builds_path = Path.cwd() / "builds"
    for file in builds_path.glob("*.html"):
        file.unlink()
