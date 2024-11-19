from abc import ABC, abstractmethod

class Downloader(ABC):
    @abstractmethod
    def download(self, file_path: str) -> bytes:
        pass