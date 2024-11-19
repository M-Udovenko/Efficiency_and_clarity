from interfaces.downloader import Downloader

class SimpleDownloader(Downloader):
    def download(self, file_path: str) -> bytes:
        print(f"🚀 Загружаем файл {file_path}...")
        return f"Содержимое файла {file_path}".encode()