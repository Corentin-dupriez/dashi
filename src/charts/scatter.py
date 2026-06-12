import plotly.express as px
import polars as pl

from dashi.charts.chart import BaseChart


class ScatterChart(BaseChart):
    def build(
        self,
        chart_name: str,
        df: pl.DataFrame,
        x: str,
        y: str,
        options: dict[str, str] | None,
    ):
        fig = px.scatter(df, x=x, y=y, title=chart_name)
        if options is not None:
            self.update_layout(fig, options)
        return fig
