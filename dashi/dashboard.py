from dashi.charts.chart import BaseChart
from .config.yaml_parser import parse_yaml
from .charts.registry import CHARTS
from pathlib import Path
from .datasources import Datasources
from plotly.graph_objs import Figure
from typing import List
import polars as pl


class NoChartType(ValueError):
    pass


class Dashboard:
    DASHBOARD_FOLDER = Path.cwd() / "dashboards"

    def __init__(self, data_sources: Datasources) -> None:
        self.dash_data: dict = self.load_dashboard()
        self.title: str = self.dash_data["title"]
        self.rows: int = self.dash_data["layout"].get("rows", 1)
        self.cols: int = self.dash_data["layout"].get("columns", 1)
        self.datasources: Datasources = data_sources
        self.charts: List[Figure | None] = [
            self.generate_chart(chart) for chart in self.dash_data["charts"]
        ]

    def load_dashboard(self) -> dict[str, str]:
        """Retrieve the yaml parametrization from the dashboard folder and return the parametrization as a dict.
        Returns:
            A dict mapping keys to a corresponding dashboard parameter, or chart.
            Example: {"title": "sample_dashboard"}
        """
        data: dict[str, str] = parse_yaml(self.DASHBOARD_FOLDER, "dashboard")
        return data

    def generate_chart(self, chart_data: dict[str, str]) -> Figure | None:
        """Create the Plotly figure based on chart data retrieved from the yaml.
        The chart data contains chart type, data source, values for x and y. The actual data has to be fetched from the datasource, which should be kept
        as an instance of the class Datasource.
        Args:
            chart_data: a dictionnary representing the chart parametrization
            Example: {"name": "example_chart", "type": "line", "datasource": "sample_datasource", "x": "x_data", "y": "y_data"}
        Returns:
            A Plotly figure, with its type corresponding to the value of the "type" key in the passed chart_data dict
        """
        chart_name: str = chart_data["name"]
        chart_type: str = chart_data["type"]
        chart_datasource: pl.DataFrame = self.datasources.find_datasource(
            chart_data["datasource"]
        ).load_data()
        chart_x: str = chart_data["x"]
        chart_y: str = chart_data["y"]
        options: dict = chart_data.get("options", None)

        builder: BaseChart = CHARTS[chart_type]

        return builder.build(chart_name, chart_datasource, chart_x, chart_y, options)
