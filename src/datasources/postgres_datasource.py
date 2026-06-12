import polars as pl
import psycopg2
from dashi.datasources.login_mixin import LoginMixin
from dashi.datasources.sql_datasource import SqlDatasource


class PostgresDatasource(SqlDatasource, LoginMixin):
    DATATYPES: dict[str, type] = {
        "bool": bool,
        "varchar": str,
        "text": str,
        "float4": float,
        "float8": float,
        "money": float,
        "date": str,
        "time": str,
        "timestamp": str,
        "numeric": float,
        "char": str,
        "int8": int,
        "int4": int,
        "int2": int,
    }

    def __init__(self, source_def: dict) -> None:
        super().__init__(source_def)
        self.connection_info = self.build_connection(source_def)
        self.conn = self.login(self.connection_info)
        self._datatypes = self._load_datatypes()

    def login(self, connection_info: dict) -> psycopg2.extensions.connection:
        try:
            return psycopg2.connect(**connection_info)
        except psycopg2.DatabaseError as err:
            raise err

    def load_data(self) -> pl.DataFrame:
        with self.conn.cursor() as curs:
            curs.execute(self.query)
            res = curs.fetchall()
            meta = {info[0]: self._datatypes.get(info[1]) for info in curs.description}
        self.conn.close()
        df = pl.DataFrame(data=res, schema=meta, orient="row")
        return df

    def _load_datatypes(self) -> dict:
        with self.conn.cursor() as curs:
            curs.execute("select oid,typname from pg_type")
            res = curs.fetchall()
            return {dtype[0]: self._pg_datatype_to_python(dtype[1]) for dtype in res}

    def _pg_datatype_to_python(self, pg_datatype: str):
        return self.DATATYPES.get(pg_datatype)
