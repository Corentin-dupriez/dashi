from config.yaml_parser import parse_yaml, NoConfigFile
from pathlib import Path
import altair as alt
from datasources import Datasources


class Dashboard:
    DASHBOARD_FOLDER = Path.cwd() / "dashboards"

    def __init__(self, data_sources: Datasources) -> None:
        self.dash_data = self.load_dashboard()
        self.title = self.dash_data["title"]
        self.datasources = data_sources
        self.charts = [self.generate_chart(chart) for chart in self.dash_data["charts"]]

    def load_dashboard(self) -> dict[str, str]:
        """Retrieve the yaml parametrization from the dashboard folder and return the parametrization as a dict.
        For ease of use from the following modules, the returned dict is a sub-dict, accessed with the key "dashboard"
        Returns:
            A dict mapping keys to a corresponding dashboard parameter, or chart.
            Example: {"dashboard": {"title": "sample_dashboard"}}
        """
        data = parse_yaml(self.DASHBOARD_FOLDER, "dashboard")
        dashboard = data["dashboard"]
        return dashboard

    def generate_chart(self, chart_data: dict) -> alt.Chart | None:
        """Create the altair chart based on chart data retrieved from the yaml.
        The chart data contains chart type, data source, values for x and y. The actual data has to be fetched from the datasource, which should be kept
        as an instance of the class Datasource.
        Args:
            chart_data: a dictionnary representing the chart parametrization
            Example: {"name": "example_chart", "type": "line", "datasource": "sample_datasource", "x": "x_data", "y": "y_data"}
        Returns:
            An altait chart type, with its type corresponding to the value of the "type" key in the passed chart_data dict
        """
        chart_name = chart_data["name"]
        chart_type = chart_data["type"]
        chart_datasource = self.datasources.find_datasource(
            chart_data["datasource"]
        ).load_data()
        chart_x = chart_data["x"] + ":T"
        chart_y = chart_data["y"] + ":Q"

        if chart_type == "line":
            chart = (
                alt.Chart(chart_datasource, title=alt.Title(chart_name))
                .mark_line()
                .encode(x=chart_x, y=chart_y)
            )

            return chart
