import plotly.express as px
import polars as pl

from dashi.charts.chart import BaseChart


class PieChart(BaseChart):
    def build(
        self,
        chart_name: str,
        df: pl.DataFrame,
        x: str,
        y: str,
        options: dict[str, str] | None,
    ):
        fig = px.pie(data_frame=df, values=x, names=y, title=chart_name)
        if options is not None:
            fig = fig.update_layout(options)

        return fig
