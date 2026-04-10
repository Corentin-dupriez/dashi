import polars as pl
from abc import ABC


class BaseChart(ABC):
    def build(
        self,
        chart_name: str,
        df: pl.DataFrame,
        x: str,
        y: str,
        options: dict[str, str] | None,
    ):
        raise NotImplementedError

    def update_layout(self, fig, options: dict):
        try:
            fig.update_layout(**options)
            return fig
        except ValueError:
            raise ValueError(
                "One of the options provided in the chart definition is incorrect"
            )
