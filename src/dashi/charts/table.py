import polars as pl
from plotly import graph_objects as go
from typing import List


class Table:
    def build(self, title: str, df: pl.DataFrame, columns: List[str]) -> go.Figure:
        headers = [col for col in df.columns if col in columns]
        data = [col for col in df.select(headers).to_dict(as_series=False).values()]
        table = go.Figure(
            data=go.Table(header=dict(values=headers), cells=dict(values=data))
        )
        return table
