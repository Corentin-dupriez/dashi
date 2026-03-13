from .chart import BaseChart
import plotly.express as px
import polars as pl


class BarChart(BaseChart):
    def build(
        self,
        chart_name: str,
        df: pl.DataFrame,
        x: str,
        y: str,
        options: dict | None = None,
    ):
        fig = px.bar(data_frame=df, x=x, y=y, title=chart_name)
        print(options)
        if options is not None:
            fig.update_layout(**options)
        print(fig.layout)
        return fig
