from typing import Optional
from models import DeliveryDetails
from strategies import DeliveryStrategy


class DeliveryContext:

    def __init__(self):
        self._strategy: Optional[DeliveryStrategy] = None

    def set_strategy(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def calculate_delivery_cost(self, details: DeliveryDetails) -> float:
        if not self._strategy:
            raise ValueError("Пожалуйста, выберите способ доставки! 🤔")
        return self._strategy.calculate_cost(details)

    def get_delivery_time(self, details: DeliveryDetails) -> str:
        if not self._strategy:
            raise ValueError("Пожалуйста, выберите способ доставки! 🤔")
        return self._strategy.get_estimated_time(details)
