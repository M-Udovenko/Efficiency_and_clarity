from director import QueryDirector
from builders import PostgreSQLQueryBuilder, MySQLQueryBuilder


def main():
    director = QueryDirector()

    print("🚀 Начинаем магию SQL-запросов!\n")

    print("🐘 PostgreSQL Query Builder:")
    postgres_builder = PostgreSQLQueryBuilder()
    director.set_builder(postgres_builder)

    postgres_query1 = director.build_simple_select(['name', 'email'])
    print(f"Простой запрос: {postgres_query1}\n")

    postgres_query2 = director.build_filtered_select(
        ['id', 'title', 'price'],
        "category = 'electronics'"
    )
    print(f"Запрос с фильтрацией: {postgres_query2}\n")

    print("🐬 MySQL Query Builder:")
    mysql_builder = MySQLQueryBuilder()
    director.set_builder(mysql_builder)

    mysql_query = director.build_complex_select(
        ['product_id', 'name', 'price'],
        "price > 100",
        10
    )
    print(f"Сложный запрос: {mysql_query}")


if __name__ == "__main__":
    main()