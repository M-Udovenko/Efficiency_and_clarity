from base_updater import EntityUpdater
from entities import Product
from messenger import Messenger
from typing import Dict, Any, Optional, Tuple


class ProductUpdater(EntityUpdater):
    def _get_entity(self, entity_id: int) -> Optional[Product]:
        return Product(id=entity_id, name="Тестовый продукт", price=100, description="Описание")

    def _validate_data(self, entity: Product, data: Dict[str, Any]) -> bool:
        return True

    def _handle_validation_failure(self, entity: Product, data: Dict[str, Any]) -> None:
        Messenger.send_admin_notification(f"Продукт {entity.name} не прошел валидацию!")

    def _prepare_update_request(self, entity: Product, data: Dict[str, Any]) -> Dict[str, Any]:
        return {"entity_type": "product", "data": data}
