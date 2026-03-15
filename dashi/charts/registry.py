from dashi.charts.pie import PieChart
from .bar import BarChart
from .line import LineChart
from .scatter import ScatterChart

CHARTS = {
    "line": LineChart(),
    "bar": BarChart(),
    "pie": PieChart(),
    "scatter": ScatterChart(),
}
