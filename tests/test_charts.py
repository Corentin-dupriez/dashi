from dashi.charts import BaseChart, CHARTS
from dashi.charts.bar import BarChart
from dashi.charts.line import LineChart
from dashi.charts.pie import PieChart
from dashi.charts.scatter import ScatterChart
import pytest
import polars as pl


@pytest.fixture
def sample_df():
    return pl.DataFrame(
        {"category": ["a", "b", "a", "b", "a"], "value": [1.0, 2.0, 3.0, 4.0, 5.0]}
    )


def test_build_bar_chart_no_options_returns_fig(sample_df):
    chart = BarChart()
    fig = chart.build("test", sample_df, "category", "value")
    assert fig.layout.title.text == "test"
    assert fig.data[0].type == "bar"
    assert fig.data[0].x.tolist() == ["a", "b", "a", "b", "a"]


def test_build_bar_chart_with_options_returns_fig(sample_df):
    chart = BarChart()
    fig = chart.build(
        "test",
        sample_df,
        "category",
        "value",
        options={"title": "Test title", "template": "plotly_white"},
    )
    assert fig.layout.title.text == "Test title"
    assert fig.data[0].type == "bar"
    assert fig.data[0].x.tolist() == ["a", "b", "a", "b", "a"]


def test_build_scatter_chart_no_options_returns_fig(sample_df):
    chart = ScatterChart()
    fig = chart.build("test", sample_df, "category", "value")
    assert fig.layout.title.text == "test"
    assert fig.data[0].type == "scatter"
    assert fig.data[0].mode == "markers"
    assert fig.data[0].x.tolist() == ["a", "b", "a", "b", "a"]


def test_build_scatter_chart_with_options_returns_fig(sample_df):
    chart = ScatterChart()
    fig = chart.build(
        "test",
        sample_df,
        "category",
        "value",
        options={"title": "Test title", "template": "plotly_white"},
    )
    assert fig.layout.title.text == "Test title"
    assert fig.data[0].type == "scatter"
    assert fig.data[0].mode == "markers"
    assert fig.data[0].x.tolist() == ["a", "b", "a", "b", "a"]


def test_build_line_chart_no_options_returns_fig(sample_df):
    chart = LineChart()
    fig = chart.build("test", sample_df, "category", "value")
    assert fig.layout.title.text == "test"
    assert fig.data[0].type == "scatter"
    assert fig.data[0].mode == "lines"
    assert fig.data[0].x.tolist() == ["a", "b", "a", "b", "a"]


def test_build_line_chart_with_options_returns_fig(sample_df):
    chart = LineChart()
    fig = chart.build(
        "test",
        sample_df,
        "category",
        "value",
        options={"title": "Test title", "template": "plotly_white"},
    )
    assert fig.layout.title.text == "Test title"
    assert fig.data[0].type == "scatter"
    assert fig.data[0].mode == "lines"
    assert fig.data[0].x.tolist() == ["a", "b", "a", "b", "a"]


def test_build_pie_chart_no_options_returns_fig(sample_df):
    chart = PieChart()
    fig = chart.build("test", sample_df, "category", "value")
    assert fig.layout.title.text == "test"
    assert fig.data[0].type == "pie"
    assert fig.data[0].values.tolist() == ["a", "b", "a", "b", "a"]


def test_build_pie_chart_with_options_returns_fig(sample_df):
    chart = PieChart()
    fig = chart.build(
        "test",
        sample_df,
        "category",
        "value",
        options={"title": "Test title", "template": "plotly_white"},
    )
    assert fig.layout.title.text == "Test title"
    assert fig.data[0].type == "pie"
    assert fig.data[0].values.tolist() == ["a", "b", "a", "b", "a"]


def test_registry_chart_exists_returns_chart():
    assert type(CHARTS["line"]) is LineChart
    assert type(CHARTS["bar"]) is BarChart
    assert type(CHARTS["pie"]) is PieChart
    assert type(CHARTS["scatter"]) is ScatterChart


def test_registry_chart_doesnt_exist_raises():
    with pytest.raises(KeyError):
        CHARTS["banana"]
