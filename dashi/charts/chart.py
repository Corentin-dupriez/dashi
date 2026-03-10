import polars as pl


class BaseChart:
    def build(self, chart_name: str, df: pl.DataFrame, x, y):
        raise NotImplementedError
