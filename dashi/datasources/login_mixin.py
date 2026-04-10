from abc import ABC

import psycopg2


class LoginMixin(ABC):
    def build_connection(self, source_def: dict) -> dict[str, str]:
        host = source_def.get("host")
        port = source_def.get("port")
        username = source_def.get("username")
        password = source_def.get("password")
        dbname = source_def.get("dbname")
        connection_info: dict = {
            "dbname": dbname,
            "host": host,
            "port": port,
            "user": username,
            "password": password,
        }
        return connection_info

    def login(self, connection_info: dict) -> psycopg2.extensions.connection:
        raise NotImplementedError
