from .chart import BaseChart
import polars as pl
import plotly.express as px


class LineChart(BaseChart):
    def build(self, chart_name: str, df: pl.DataFrame, x, y, options):
        fig = px.line(df, x=x, y=y, title=chart_name)
        if options is not None:
            print(options)
            fig.update_layout(**options)
        return fig
