from .chart import BaseChart
import polars as pl
import plotly.express as px


class LineChart(BaseChart):
    def build(self, chart_name: str, df: pl.DataFrame, x, y):
        return px.line(df, x=x, y=y)
