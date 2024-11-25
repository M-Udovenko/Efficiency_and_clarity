from abc import ABC, abstractmethod
from models import DeliveryDetails


class DeliveryStrategy(ABC):

    @abstractmethod
    def calculate_cost(self, details: DeliveryDetails) -> float:
        pass

    @abstractmethod
    def get_estimated_time(self, details: DeliveryDetails) -> str:
        pass


class SelfPickupStrategy(DeliveryStrategy):

    def calculate_cost(self, details: DeliveryDetails) -> float:
        return 0.0  # Самовывоз бесплатный! 🎉

    def get_estimated_time(self, details: DeliveryDetails) -> str:
        return "Можно забрать в течение часа! ⏰"


class ExternalDeliveryStrategy(DeliveryStrategy):

    def calculate_cost(self, details: DeliveryDetails) -> float:
        base_cost = 100
        per_km_cost = 20
        express_multiplier = 1.5 if details.is_express else 1.0

        total = (base_cost + details.distance_km * per_km_cost) * express_multiplier
        return round(total, 2)

    def get_estimated_time(self, details: DeliveryDetails) -> str:
        if details.is_express:
            return "Доставим за 30-60 минут! 🏃💨"
        return "Доставка займет 1-2 часа 🚗"


class OwnDeliveryStrategy(DeliveryStrategy):

    def calculate_cost(self, details: DeliveryDetails) -> float:
        base_cost = 80
        per_km_cost = 15
        weight_cost = details.weight_kg * 10
        express_multiplier = 1.7 if details.is_express else 1.0

        total = (base_cost + details.distance_km * per_km_cost + weight_cost) * express_multiplier
        return round(total, 2)

    def get_estimated_time(self, details: DeliveryDetails) -> str:
        if details.is_express:
            return "Доставим за 45 минут или бесплатно! ⚡"
        return "Доставка займет около часа 🛵"