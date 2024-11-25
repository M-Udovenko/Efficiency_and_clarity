from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple, Optional



class EntityUpdater(ABC):
    def update_entity(self, entity_id: int, data: Dict[str, Any]) -> Tuple[int, str, Optional[Dict]]:

        entity = self._get_entity(entity_id)
        if not entity:
            return 404, "Сущность не найдена", None

        if not self._validate_data(entity, data):
            self._handle_validation_failure(entity, data)
            return 400, "Ошибка валидации", None

        update_request = self._prepare_update_request(entity, data)

        return self._prepare_response(update_request)

    @abstractmethod
    def _get_entity(self, entity_id: int) -> Optional[Any]:
        """Получение сущности по ID"""
        pass

    @abstractmethod
    def _validate_data(self, entity: Any, data: Dict[str, Any]) -> bool:
        """Валидация данных"""
        pass

    def _handle_validation_failure(self, entity: Any, data: Dict[str, Any]) -> None:
        """Хук для обработки ошибок валидации"""
        pass

    @abstractmethod
    def _prepare_update_request(self, entity: Any, data: Dict[str, Any]) -> Dict[str, Any]:
        """Подготовка запроса на обновление"""
        pass

    def _prepare_response(self, update_request: Dict[str, Any]) -> Tuple[int, str, Optional[Dict]]:
        """Базовая подготовка ответа"""
        return 200, "Успешно обновлено", None
