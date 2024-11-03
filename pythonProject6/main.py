from abc import ABC, abstractmethod
from typing import Dict


# Інтерфейс для завантажувача файлів
class Downloader(ABC):
    @abstractmethod
    def download(self, url: str) -> str:
        pass


# Базовий клас завантажувача
class SimpleDownloader(Downloader):
    def download(self, url: str) -> str:
        # Логіка завантаження файлу з мережі
        print(f"Завантажуємо файл з: {url}")
        return f"Вміст файлу з {url}"


# Клас-замісник з функціоналом кешування
class CachingDownloaderProxy(Downloader):
    def __init__(self, real_downloader: Downloader):
        self._real_downloader = real_downloader
        self._cache: Dict[str, str] = {}

    def download(self, url: str) -> str:
        # Перевіряємо наявність файлу в кеші
        if url in self._cache:
            print(f"Отримуємо файл з кешу: {url}")
            return self._cache[url]

        # Якщо файлу немає в кеші - завантажуємо його
        print(f"Файл не знайдено в кеші. Завантажуємо...")
        result = self._real_downloader.download(url)

        # Зберігаємо результат у кеш
        self._cache[url] = result
        return result

    def clear_cache(self):
        # Метод для очищення кешу
        print("Очищуємо кеш...")
        self._cache.clear()

    def get_cache_size(self) -> int:
        # Метод для отримання розміру кешу
        return len(self._cache)


# Демонстрація роботи
def main():
    # Створюємо базовий завантажувач
    simple_downloader = SimpleDownloader()

    # Створюємо проксі з кешуванням
    caching_downloader = CachingDownloaderProxy(simple_downloader)

    # Тестуємо завантаження
    file_url = "http://example.com/file.txt"

    print("Перше завантаження файлу:")
    content1 = caching_downloader.download(file_url)

    print("\nДруге завантаження того ж файлу (має взятись з кешу):")
    content2 = caching_downloader.download(file_url)

    print(f"\nРозмір кешу: {caching_downloader.get_cache_size()} файлів")

    print("\nОчищуємо кеш")
    caching_downloader.clear_cache()

    print(f"\nРозмір кешу після очищення: {caching_downloader.get_cache_size()} файлів")

    print("\nЗавантажуємо файл знову (після очищення кешу):")
    content3 = caching_downloader.download(file_url)


if __name__ == "__main__":
    main()