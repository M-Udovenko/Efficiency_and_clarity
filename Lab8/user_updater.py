from base_updater import EntityUpdater
from entities import User
from typing import Dict, Any, Optional


class UserUpdater(EntityUpdater):
    def _get_entity(self, entity_id: int) -> Optional[User]:
        return User(id=entity_id, name="Тестовый пользователь", email="test@test.com", phone="123")

    def _validate_data(self, entity: User, data: Dict[str, Any]) -> bool:
        if 'email' in data and data['email'] != entity.email:
            return False
        return True

    def _prepare_update_request(self, entity: User, data: Dict[str, Any]) -> Dict[str, Any]:
        return {"entity_type": "user", "data": data}
