from .chart import BaseChart
import polars as pl
import plotly.express as px


class LineChart(BaseChart):
    def build(
        self,
        chart_name: str,
        df: pl.DataFrame,
        x: str,
        y: str,
        options: dict[str, str] | None,
    ):
        fig = px.line(df, x=x, y=y, title=chart_name)
        if options is not None:
            self.update_layout(fig, options)
        return fig
