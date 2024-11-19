from abc import ABC, abstractmethod
from typing import List, Self


class QueryBuilder(ABC):

    @abstractmethod
    def select(self, fields: List[str]) -> Self:
        pass

    @abstractmethod
    def where(self, condition: str) -> Self:
        pass

    @abstractmethod
    def limit(self, count: int) -> Self:
        pass

    @abstractmethod
    def get_sql(self) -> str:
        pass
