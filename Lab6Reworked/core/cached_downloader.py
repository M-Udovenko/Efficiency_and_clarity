from interfaces.downloader import Downloader


class CachedDownloader(Downloader):

    def __init__(self, real_downloader: Downloader):
        self._real_downloader = real_downloader
        self._cache: dict[str, bytes] = {}

    def download(self, file_path: str) -> bytes:
        if file_path in self._cache:
            print(f"🎯 Беру {file_path} из кеша - молниеносная скорость!")
            return self._cache[file_path]

        print(f"🔍 Файл {file_path} не найден в кеше, придется загрузить...")
        result = self._real_downloader.download(file_path)
        self._cache[file_path] = result
        print(f"✨ Отлично! Сохранил {file_path} в кеш для будущих запросов")
        return result