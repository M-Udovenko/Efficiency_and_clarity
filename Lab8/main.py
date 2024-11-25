from product_updater import ProductUpdater
from user_updater import UserUpdater
from order_updater import OrderUpdater


def main():
    product_updater = ProductUpdater()
    user_updater = UserUpdater()
    order_updater = OrderUpdater()

    print("🚀 Начинаем тестирование обновления сущностей...")

    print("\n🛍️ Тестируем обновление продукта...")
    code, status, data = product_updater.update_entity(1, {"name": "Новый продукт"})
    print(f"Результат: {status} (код {code})")

    print("\n👤 Тестируем обновление пользователя...")
    code, status, data = user_updater.update_entity(1, {"email": "new@email.com"})
    print(f"Результат: {status} (код {code})")

    print("\n📦 Тестируем обновление заказа...")
    code, status, data = order_updater.update_entity(1, {"status": "shipped"})
    print(f"Результат: {status} (код {code})")
    if data:
        print(f"Данные заказа: {data}")

    print("\n✨ Тестирование завершено!")


if __name__ == "__main__":
    main()