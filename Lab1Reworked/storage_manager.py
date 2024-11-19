from storage_types import StorageSystem, LocalStorage, AmazonS3Storage
from typing import Optional


class StorageManager:
    _instance = None
    _storage_systems = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._storage_systems = {
                'local': LocalStorage(),
                's3': AmazonS3Storage()
            }
        return cls._instance

    def get_storage(self, storage_type: str) -> Optional[StorageSystem]:
        return self._storage_systems.get(storage_type)

    def add_storage_system(self, name: str, storage_system: StorageSystem):
        self._storage_systems[name] = storage_system

