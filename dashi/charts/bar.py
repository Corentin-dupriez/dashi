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
            try:
                fig.update_layout(**options)
            except ValueError:
                raise ValueError(
                    "One of the options provided in the chart definition is incorrect"
                )
        print(fig.layout)
        return fig
