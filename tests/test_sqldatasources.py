import pytest
from dashi.datasources import PostgresDatasource


@pytest.fixture
def postgres_datasource(mocker):
    mock_conn = mocker.MagicMock()
    mock_conn.__enter__.return_value = mock_conn
    mocker.patch(
        "dashi.datasources.postgres_datasource.psycopg2.connect", return_value=mock_conn
    )
    source_def = {
        "name": "test",
        "type": "postgres",
        "query": "SELECT 1",
        "host": "localhost",
        "port": 5432,
        "username": "user",
        "password": "pass",
        "dbname": "db",
    }

    ds = PostgresDatasource(source_def)

    return ds


def test_datasource_is_initialized(postgres_datasource):
    assert postgres_datasource.connection_info["host"] == "localhost"
    assert postgres_datasource.connection_info["user"] == "user"
    assert postgres_datasource.query == "SELECT 1"


def test_load_datasource(mocker, postgres_datasource):
    mock_curs = mocker.MagicMock()
    mock_curs.fetchall.return_value = [(1,), (2,)]
    mock_conn = mocker.MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_curs
    postgres_datasource.conn = mock_conn
    df = postgres_datasource.load_data()
    assert df.shape == (2, 1)
    assert [k for k in df.to_dict().keys()] == ["column_0"]
    mock_curs.execute.assert_called_once_with(postgres_datasource.query)
