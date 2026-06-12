from charts.pie import PieChart
from charts.table import Table
from .bar import BarChart
from .line import LineChart
from .scatter import ScatterChart

CHARTS = {
    "line": LineChart(),
    "bar": BarChart(),
    "pie": PieChart(),
    "scatter": ScatterChart(),
    "table": Table(),
}
