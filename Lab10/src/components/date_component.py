from datetime import datetime, timedelta
from typing import List
from ..mediator.order_mediator import Colleague

class DeliveryDateComponent(Colleague):
    def __init__(self, mediator):
        super().__init__(mediator)
        self._available_dates = self._generate_dates()
        self._selected_date = None
        self._available_time_slots = []

    def _generate_dates(self) -> List[datetime]:
        return [datetime.now() + timedelta(days=x) for x in range(14)]

    def select_date(self, date: datetime):
        self._selected_date = date
        self._available_time_slots = self._get_time_slots_for_date(date)
        self._mediator.date_changed(date)

    def _get_time_slots_for_date(self, date: datetime) -> List[str]:
        time_slots = [
            "09:00-11:00", "11:00-13:00",
            "13:00-15:00", "15:00-17:00",
            "17:00-19:00"
        ]
        return time_slots

    def get_available_time_slots(self) -> List[str]:
        return self._available_time_slots
