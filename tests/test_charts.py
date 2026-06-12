from charts import BaseChart, CHARTS
from charts.bar import BarChart
from charts.line import LineChart
from charts.pie import PieChart
from charts.scatter import ScatterChart
import pytest


def test_registry_chart_exists_returns_chart():
    assert type(CHARTS["line"]) is LineChart
    assert type(CHARTS["bar"]) is BarChart
    assert type(CHARTS["pie"]) is PieChart
    assert type(CHARTS["scatter"]) is ScatterChart


def test_registry_chart_doesnt_exist_raises():
    with pytest.raises(KeyError):
        CHARTS["banana"]
