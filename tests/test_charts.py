from src.charts import BaseChart, CHARTS
from src.charts.bar import BarChart
from src.charts.line import LineChart
from src.charts.pie import PieChart
from src.charts.scatter import ScatterChart
import pytest


def test_registry_chart_exists_returns_chart():
    assert type(CHARTS["line"]) is LineChart
    assert type(CHARTS["bar"]) is BarChart
    assert type(CHARTS["pie"]) is PieChart
    assert type(CHARTS["scatter"]) is ScatterChart


def test_registry_chart_doesnt_exist_raises():
    with pytest.raises(KeyError):
        CHARTS["banana"]
