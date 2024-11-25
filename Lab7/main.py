from models import DeliveryDetails
from strategies import SelfPickupStrategy, ExternalDeliveryStrategy, OwnDeliveryStrategy
from delivery_context import DeliveryContext


def main():
    delivery = DeliveryContext()

    order_details = DeliveryDetails(
        distance_km=5.5,
        weight_kg=2.3,
        is_express=True
    )

    print("🚀 Давайте посмотрим на разные варианты доставки!\n")

    delivery.set_strategy(SelfPickupStrategy())
    print("🚶 Самовывоз:")
    print(f"Стоимость: {delivery.calculate_delivery_cost(order_details)} руб.")
    print(f"Время: {delivery.get_delivery_time(order_details)}\n")

    delivery.set_strategy(ExternalDeliveryStrategy())
    print("🚗 Внешняя служба доставки:")
    print(f"Стоимость: {delivery.calculate_delivery_cost(order_details)} руб.")
    print(f"Время: {delivery.get_delivery_time(order_details)}\n")

    delivery.set_strategy(OwnDeliveryStrategy())
    print("🛵 Наша служба доставки:")
    print(f"Стоимость: {delivery.calculate_delivery_cost(order_details)} руб.")
    print(f"Время: {delivery.get_delivery_time(order_details)}")


if __name__ == "__main__":
    main()