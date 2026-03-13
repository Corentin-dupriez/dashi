import polars as pl


class BaseChart:
    def build(
        self, chart_name: str, df: pl.DataFrame, x: str, y: str, options: dict[str, str]
    ):
        raise NotImplementedError
