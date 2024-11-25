from base_updater import EntityUpdater
from entities import Order
from typing import Dict, Any, Optional, Tuple


class OrderUpdater(EntityUpdater):
    def _get_entity(self, entity_id: int) -> Optional[Order]:
        return Order(id=entity_id, user_id=1, products=[], total=0, status="new")

    def _validate_data(self, entity: Order, data: Dict[str, Any]) -> bool:
        return True

    def _prepare_update_request(self, entity: Order, data: Dict[str, Any]) -> Dict[str, Any]:
        return {"entity_type": "order", "data": data}

    def _prepare_response(self, update_request: Dict[str, Any]) -> Tuple[int, str, Dict]:
        return 200, "Успешно обновлено", {
            "order_id": 1,
            "status": "updated",
            "details": update_request["data"]
        }
