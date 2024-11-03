from abc import ABC, abstractmethod
from typing import Dict, Optional


# Абстрактний клас для сховища
class Storage(ABC):
    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        pass

    @abstractmethod
    def list_files(self) -> list:
        pass

    @abstractmethod
    def upload_file(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def download_file(self, file_name: str) -> bool:
        pass


# Конкретна реалізація локального сховища
class LocalStorage(Storage):
    def connect(self) -> bool:
        # Підключення до локального диска
        return True

    def disconnect(self) -> bool:
        # Відключення від локального диска
        return True

    def list_files(self) -> list:
        # Реалізація отримання списку файлів
        return []

    def upload_file(self, file_path: str) -> bool:
        # Реалізація завантаження файлу
        return True

    def download_file(self, file_name: str) -> bool:
        # Реалізація завантаження файлу
        return True


# Конкретна реалізація сховища Amazon S3
class AmazonS3Storage(Storage):
    def connect(self) -> bool:
        # Реалізація підключення до Amazon S3
        return True

    def disconnect(self) -> bool:
        # Реалізація відключення від Amazon S3
        return True

    def list_files(self) -> list:
        # Реалізація отримання списку файлів
        return []

    def upload_file(self, file_path: str) -> bool:
        # Реалізація завантаження файлу
        return True

    def download_file(self, file_name: str) -> bool:
        # Реалізація завантаження файлу
        return True


# Singleton клас для керування файлами користувача
class UserFileManager:
    _instances: Dict[str, 'UserFileManager'] = {}
    _storage: Optional[Storage] = None

    def __new__(cls, user_id: str) -> 'UserFileManager':
        if user_id not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[user_id] = instance
            return instance
        return cls._instances[user_id]

    def __init__(self, user_id: str):
        self.user_id = user_id

    def set_storage(self, storage_type: str) -> bool:
        """
        Встановлює тип сховища для користувача
        """
        if storage_type == "local":
            self._storage = LocalStorage()
        elif storage_type == "s3":
            self._storage = AmazonS3Storage()
        else:
            raise ValueError("Unsupported storage type")

        return self._storage.connect()

    def get_files_list(self) -> list:
        """
        Отримує список файлів із поточного сховища
        """
        if not self._storage:
            raise RuntimeError("Storage is not set")
        return self._storage.list_files()

    def upload_file(self, file_path: str) -> bool:
        """
        Завантажує файл у поточне сховище
        """
        if not self._storage:
            raise RuntimeError("Storage is not set")
        return self._storage.upload_file(file_path)

    def download_file(self, file_name: str) -> bool:
        """
        Завантажує файл із
        """
        if not self._storage:
            raise RuntimeError("Storage is not set")
        return self._storage.download_file(file_name)


# Приклад використання
def main():
    # Створюємо менеджер файлів для користувача 1
    user1_manager = UserFileManager("user1")
    user1_manager.set_storage("local")

    # Створюємо менеджер файлів для користувача 2
    user2_manager = UserFileManager("user2")
    user2_manager.set_storage("s3")

    # Перевіряємо, що для одного користувача повертається той самий екземпляр
    user1_manager_again = UserFileManager("user1")
    print(f"Same instance for user1: {user1_manager is user1_manager_again}")  # Should print True

    # Приклад використання методів
    user1_manager.upload_file("test.txt")
    files = user1_manager.get_files_list()
    user2_manager.download_file("document.pdf")


if __name__ == "__main__":
    main()