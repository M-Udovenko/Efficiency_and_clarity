from core.simple_downloader import SimpleDownloader
from core.cached_downloader import CachedDownloader


def main():
    """🌈 Демонстрация работы прокси-загрузчика с кешированием"""
    # Создаем базовый загрузчик
    simple_downloader = SimpleDownloader()

    # Оборачиваем его в прокси с кешированием
    cached_downloader = CachedDownloader(simple_downloader)

    # Демонстрация работы
    print("\n📚 Тест 1: Первая загрузка файла")
    cached_downloader.download("important_doc.pdf")

    print("\n📚 Тест 2: Повторная загрузка того же файла")
    cached_downloader.download("important_doc.pdf")

    print("\n📚 Тест 3: Загрузка нового файла")
    cached_downloader.download("another_file.txt")


if __name__ == "__main__":
    main()