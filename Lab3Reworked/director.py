from typing import List
from interfaces import QueryBuilder


class QueryDirector:

    def __init__(self):
        self._builder: QueryBuilder | None = None

    def set_builder(self, builder: QueryBuilder):
        self._builder = builder
        return self

    def build_simple_select(self, fields: List[str]) -> str:
        return self._builder.select(fields).get_sql()

    def build_filtered_select(self, fields: List[str], condition: str) -> str:
        return self._builder.select(fields).where(condition).get_sql()

    def build_complex_select(self, fields: List[str], condition: str, limit: int) -> str:
        return self._builder.select(fields).where(condition).limit(limit).get_sql()
