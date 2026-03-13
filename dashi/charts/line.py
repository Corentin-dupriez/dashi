from .chart import BaseChart
import polars as pl
import plotly.express as px


class LineChart(BaseChart):
    def build(self, chart_name: str, df: pl.DataFrame, x, y, options):
        fig = px.line(df, x=x, y=y, title=chart_name)
        if options is not None:
            try:
                fig.update_layout(**options)
            except ValueError:
                raise ValueError(
                    "One of the options provided in the chart definition is incorrect"
                )
        return fig
