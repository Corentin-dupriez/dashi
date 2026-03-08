from datasources import Datasource
import pytest
import polars as pl


@pytest.fixture
def data_source(mocker):
    mocked_file = mocker.patch("datasources.Datasource.load_data")
    mocked_file.return_value = pl.DataFrame()
    return Datasource(
        "test_data",
        "csv",
        [{"name": "name", "type": "string"}, {"name": "age", "type": "integer"}],
    )


@pytest.mark.parametrize(
    "data_input, expected",
    [
        ("string", pl.datatypes.String),
        ("integer", pl.datatypes.Int32),
        ("float", pl.datatypes.Float16),
        ("date", pl.datatypes.Date),
        ("spongebob", pl.datatypes.Unknown),
    ],
)
def test_convert_to_pl_datatype(data_source, data_input, expected):
    assert data_source.convert_type_to_pl_datatype(data_input) == expected
