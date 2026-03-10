from .chart import BaseChart
import plotly.express as px
import polars as pl


class BarChart(BaseChart):
    def build(self, chart_name: str, df: pl.DataFrame, x, y):
        return px.bar(df, x, y)
