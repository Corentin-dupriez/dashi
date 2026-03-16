from dashi.charts import BaseChart, CHARTS
from dashi.charts.bar import BarChart
from dashi.charts.line import LineChart
from dashi.charts.pie import PieChart
from dashi.charts.scatter import ScatterChart
import pytest


def test_registry_chart_exists_returns_chart():
    assert type(CHARTS["line"]) is LineChart
    assert type(CHARTS["bar"]) is BarChart
    assert type(CHARTS["pie"]) is PieChart
    assert type(CHARTS["scatter"]) is ScatterChart


def test_registry_chart_doesnt_exist_raises():
    with pytest.raises(KeyError):
        CHARTS["banana"]
