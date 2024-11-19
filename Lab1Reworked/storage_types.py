from abc import ABC, abstractmethod
from typing import List, Optional


class StorageSystem(ABC):
    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def list_files(self) -> List[str]:
        pass

    @abstractmethod
    def upload_file(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def download_file(self, file_name: str, destination: str) -> bool:
        pass


class LocalStorage(StorageSystem):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self) -> bool:
        print("🖥️ Подключаемся к локальному хранилищу...")
        return True

    def list_files(self) -> List[str]:
        return ["document1.txt", "photo.jpg", "data.csv"]

    def upload_file(self, file_path: str) -> bool:
        print(f"📤 Загружаем файл {file_path} в локальное хранилище")
        return True

    def download_file(self, file_name: str, destination: str) -> bool:
        print(f"📥 Скачиваем файл {file_name} в {destination}")
        return True


class AmazonS3Storage(StorageSystem):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self) -> bool:
        print("☁️ Подключаемся к Amazon S3...")
        return True

    def list_files(self) -> List[str]:
        return ["cloud_doc.txt", "backup.zip", "images.tar"]

    def upload_file(self, file_path: str) -> bool:
        print(f"⬆️ Загружаем файл {file_path} в Amazon S3")
        return True

    def download_file(self, file_name: str, destination: str) -> bool:
        print(f"⬇️ Скачиваем файл {file_name} из Amazon S3 в {destination}")
        return True

