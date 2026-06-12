def prettify_title(title: str) -> str:
    return " ".join(word.capitalize() for word in title.split("_"))
