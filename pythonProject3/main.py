from abc import ABC, abstractmethod
from typing import List, Optional


# Абстрактний клас будівельника запитів
class SQLQueryBuilder(ABC):
    def __init__(self):
        self.reset()

    def reset(self):
        """Скидає всі параметри запиту до початкових значень"""
        self.table = ""
        self.columns: List[str] = []
        self.conditions: List[str] = []
        self.limit_value: Optional[int] = None

    @abstractmethod
    def select(self, table: str, columns: List[str]) -> 'SQLQueryBuilder':
        """Додає SELECT частину запиту"""
        pass

    @abstractmethod
    def where(self, condition: str) -> 'SQLQueryBuilder':
        """Додає WHERE умову до запиту"""
        pass

    @abstractmethod
    def limit(self, value: int) -> 'SQLQueryBuilder':
        """Додає LIMIT до запиту"""
        pass

    @abstractmethod
    def get_sql(self) -> str:
        """Повертає готовий SQL запит"""
        pass


# Будівельник запитів для PostgreSQL
class PostgreSQLQueryBuilder(SQLQueryBuilder):
    def select(self, table: str, columns: List[str]) -> 'PostgreSQLQueryBuilder':
        """
        Формує SELECT частину запиту для PostgreSQL
        Приклад: SELECT column1, column2 FROM table_name
        """
        self.table = f'"{table}"'  # В PostgreSQL використовуємо подвійні лапки
        self.columns = [f'"{col}"' for col in columns]
        return self

    def where(self, condition: str) -> 'PostgreSQLQueryBuilder':
        """
        Додає WHERE умову до PostgreSQL запиту
        Приклад: WHERE column_name = 'value'
        """
        self.conditions.append(condition)
        return self

    def limit(self, value: int) -> 'PostgreSQLQueryBuilder':
        """
        Додає LIMIT до PostgreSQL запиту
        Приклад: LIMIT 10
        """
        self.limit_value = value
        return self

    def get_sql(self) -> str:
        """Формує кінцевий PostgreSQL запит"""
        # Формуємо базовий SELECT
        query = f"SELECT {', '.join(self.columns)} FROM {self.table}"

        # Додаємо WHERE якщо є умови
        if self.conditions:
            query += f" WHERE {' AND '.join(self.conditions)}"

        # Додаємо LIMIT якщо вказано
        if self.limit_value is not None:
            query += f" LIMIT {self.limit_value}"

        return query + ";"


# Будівельник запитів для MySQL
class MySQLQueryBuilder(SQLQueryBuilder):
    def select(self, table: str, columns: List[str]) -> 'MySQLQueryBuilder':
        """
        Формує SELECT частину запиту для MySQL
        Приклад: SELECT column1, column2 FROM table_name
        """
        self.table = f'`{table}`'  # В MySQL використовуємо зворотні апострофи
        self.columns = [f'`{col}`' for col in columns]
        return self

    def where(self, condition: str) -> 'MySQLQueryBuilder':
        """
        Додає WHERE умову до MySQL запиту
        Приклад: WHERE column_name = 'value'
        """
        self.conditions.append(condition)
        return self

    def limit(self, value: int) -> 'MySQLQueryBuilder':
        """
        Додає LIMIT до MySQL запиту
        Приклад: LIMIT 10
        """
        self.limit_value = value
        return self

    def get_sql(self) -> str:
        """Формує кінцевий MySQL запит"""
        # Формуємо базовий SELECT
        query = f"SELECT {', '.join(self.columns)} FROM {self.table}"

        # Додаємо WHERE якщо є умови
        if self.conditions:
            query += f" WHERE {' AND '.join(self.conditions)}"

        # Додаємо LIMIT якщо вказано
        if self.limit_value is not None:
            query += f" LIMIT {self.limit_value}"

        return query + ";"


# Директор, який керує будівельником
class QueryDirector:
    def __init__(self, builder: SQLQueryBuilder):
        self._builder = builder

    def make_simple_select(self, table: str, columns: List[str]) -> str:
        """Створює простий SELECT запит"""
        return self._builder.select(table, columns).get_sql()

    def make_filtered_select(self, table: str, columns: List[str],
                             condition: str, limit: int) -> str:
        """Створює SELECT запит з фільтрацією та лімітом"""
        return (self._builder
                .select(table, columns)
                .where(condition)
                .limit(limit)
                .get_sql())


# Приклад використання
def main():
    # Створюємо будівельників для різних СУБД
    postgres_builder = PostgreSQLQueryBuilder()
    mysql_builder = MySQLQueryBuilder()

    # Створюємо директорів
    postgres_director = QueryDirector(postgres_builder)
    mysql_director = QueryDirector(mysql_builder)

    print("=== PostgreSQL запити ===")

    # Простий SELECT для PostgreSQL
    query1 = postgres_director.make_simple_select(
        "users",
        ["id", "name", "email"]
    )
    print(f"Простий SELECT:\n{query1}\n")

    # SELECT з фільтрацією для PostgreSQL
    query2 = postgres_director.make_filtered_select(
        "users",
        ["id", "name", "email"],
        "age >= 18",
        10
    )
    print(f"SELECT з фільтрацією:\n{query2}\n")

    print("=== MySQL запити ===")

    # Простий SELECT для MySQL
    query3 = mysql_director.make_simple_select(
        "users",
        ["id", "name", "email"]
    )
    print(f"Простий SELECT:\n{query3}\n")

    # SELECT з фільтрацією для MySQL
    query4 = mysql_director.make_filtered_select(
        "users",
        ["id", "name", "email"],
        "age >= 18",
        10
    )
    print(f"SELECT з фільтрацією:\n{query4}")


if __name__ == "__main__":
    main()