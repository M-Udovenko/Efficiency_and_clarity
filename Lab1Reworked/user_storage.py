from typing import Optional


class UserStoragePreference:
    _instance = None
    _user_preferences = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._user_preferences = {}
        return cls._instance

    def set_user_storage(self, user_id: str, storage_type: str):
        self._user_preferences[user_id] = storage_type

    def get_user_storage(self, user_id: str) -> Optional[str]:
        return self._user_preferences.get(user_id)
