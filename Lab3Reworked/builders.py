from typing import List
from interfaces import QueryBuilder


class PostgreSQLQueryBuilder(QueryBuilder):
    def __init__(self):
        self._query_parts = {
            'select': [],
            'where': [],
            'limit': None
        }
        print("🚀 PostgreSQL Query Builder активирован!")

    def select(self, fields: List[str]) -> 'PostgreSQLQueryBuilder':
        self._query_parts['select'] = fields
        return self

    def where(self, condition: str) -> 'PostgreSQLQueryBuilder':
        self._query_parts['where'].append(condition)
        return self

    def limit(self, count: int) -> 'PostgreSQLQueryBuilder':
        self._query_parts['limit'] = count
        return self

    def get_sql(self) -> str:
        query = f"SELECT {', '.join(self._query_parts['select'])}"

        if self._query_parts['where']:
            query += f" WHERE {' AND '.join(self._query_parts['where'])}"

        if self._query_parts['limit'] is not None:
            query += f" LIMIT {self._query_parts['limit']}"

        print(f"✨ PostgreSQL запрос готов: {query}")
        return query


class MySQLQueryBuilder(QueryBuilder):
    def __init__(self):
        self._query_parts = {
            'select': [],
            'where': [],
            'limit': None
        }
        print("🚀 MySQL Query Builder активирован!")

    def select(self, fields: List[str]) -> 'MySQLQueryBuilder':
        self._query_parts['select'] = fields
        return self

    def where(self, condition: str) -> 'MySQLQueryBuilder':
        self._query_parts['where'].append(condition)
        return self

    def limit(self, count: int) -> 'MySQLQueryBuilder':
        self._query_parts['limit'] = count
        return self

    def get_sql(self) -> str:
        query = f"SELECT {', '.join(self._query_parts['select'])}"

        if self._query_parts['where']:
            query += f" WHERE {' AND '.join(self._query_parts['where'])}"

        if self._query_parts['limit'] is not None:
            query += f" LIMIT {self._query_parts['limit']}"

        print(f"✨ MySQL запрос готов: {query}")
        return query
