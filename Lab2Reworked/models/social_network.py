from abc import ABC, abstractmethod
from .credentials import FacebookCredentials, LinkedInCredentials


class SocialNetwork(ABC):
    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def post_message(self, message: str) -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass


class Facebook(SocialNetwork):
    def __init__(self, credentials: FacebookCredentials):
        self.credentials = credentials
        self.connected = False

    def connect(self) -> bool:
        print(f"🔌 Подключаемся к Facebook как {self.credentials.login}")
        self.connected = True
        return True

    def post_message(self, message: str) -> bool:
        if not self.connected:
            print("❌ Ошибка: Сначала нужно подключиться к Facebook!")
            return False
        print(f"📱 Публикуем в Facebook: {message}")
        return True

    def disconnect(self) -> None:
        if self.connected:
            print("👋 Отключаемся от Facebook")
            self.connected = False


class LinkedIn(SocialNetwork):
    def __init__(self, credentials: LinkedInCredentials):
        self.credentials = credentials
        self.connected = False

    def connect(self) -> bool:
        print(f"🔌 Подключаемся к LinkedIn используя {self.credentials.email}")
        self.connected = True
        return True

    def post_message(self, message: str) -> bool:
        if not self.connected:
            print("❌ Ошибка: Сначала нужно подключиться к LinkedIn!")
            return False
        print(f"💼 Публикуем в LinkedIn: {message}")
        return True

    def disconnect(self) -> None:
        if self.connected:
            print("👋 Отключаемся от LinkedIn")
            self.connected = False

