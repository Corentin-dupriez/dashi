from dashi import datasources
from dashi.datasources import BaseDatasource, CsvDatasource
from dashi.datasources.json_datasource import JsonDatasource
from dashi.datasources.registry import DATASOURCES
import pytest
import polars as pl


@pytest.fixture
def data_source(mocker):
    mocked_file = mocker.patch("dashi.datasources.BaseDatasource.load_data")
    mocked_file.return_value = pl.DataFrame()
    return BaseDatasource(
        "test_data",
        "csv",
        [{"name": "name", "type": "string"}, {"name": "age", "type": "integer"}],
    )


@pytest.mark.parametrize(
    "data_input, expected",
    [
        ("string", pl.datatypes.String),
        ("integer", pl.datatypes.Int32),
        ("float", pl.datatypes.Float32),
        ("date", pl.datatypes.Date),
        ("spongebob", pl.datatypes.Unknown),
    ],
)
def test_convert_to_pl_datatype(data_source, data_input, expected):
    assert data_source.convert_type_to_pl_datatype(data_input) == expected


def test_csv_datasource_intitializes_attributes(data_source):
    assert data_source.name == "test_data"
    assert data_source.data_type == "csv"
    assert data_source.columns == [
        {"name": "name", "type": "string"},
        {"name": "age", "type": "integer"},
    ]


def test_csv_datasource_default_path(data_source):
    assert (
        data_source.path
        == data_source.STAGING_DATA_PATH / f"{data_source.name}.{data_source.data_type}"
    )


def test_datasources_registery_returns_correct_datasource():
    assert DATASOURCES["csv"] is CsvDatasource
    assert DATASOURCES["json"] is JsonDatasource
