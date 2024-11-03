from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


# Базовий клас для всіх соціальних мереж
class SocialNetwork(ABC):
    @abstractmethod
    def connect(self) -> bool:
        """З'єднання з соціальною мережею"""
        pass

    @abstractmethod
    def post_message(self, message: str) -> bool:
        """Публікація повідомлення"""
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        """Відключення від соціальної мережі"""
        pass


# Клас для роботи з Facebook
class Facebook(SocialNetwork):
    def __init__(self, login: str, password: str):
        # Перевірка креденшелів
        self.login = login
        self.password = password

    def connect(self) -> bool:
        # Логіка підключення до Facebook API
        print(f"Підключаємось до Facebook з логіном: {self.login}")
        return True

    def post_message(self, message: str) -> bool:
        # Логіка публікації у Facebook
        print(f"Публікуємо у Facebook: {message}")
        return True

    def disconnect(self) -> bool:
        print("Відключаємось від Facebook")
        return True


# Клас для роботи з LinkedIn
class LinkedIn(SocialNetwork):
    def __init__(self, email: str, password: str):
        # Перевірка креденшелів
        self.email = email
        self.password = password

    def connect(self) -> bool:
        # Логіка підключення до LinkedIn API
        print(f"Підключаємось до LinkedIn з поштою: {self.email}")
        return True

    def post_message(self, message: str) -> bool:
        # Логіка публікації у LinkedIn
        print(f"Публікуємо у LinkedIn: {message}")
        return True

    def disconnect(self) -> bool:
        print("Відключаємось від LinkedIn")
        return True


# Клас для зберігання креденшелів Facebook
@dataclass
class FacebookCredentials:
    login: str
    password: str


# Клас для зберігання креденшелів LinkedIn
@dataclass
class LinkedInCredentials:
    email: str
    password: str


# Абстрактна фабрика соціальних мереж
class SocialNetworkFactory(ABC):
    @abstractmethod
    def create_network(self) -> SocialNetwork:
        """Створює екземпляр соціальної мережі"""
        pass


# Фабрика для створення Facebook
class FacebookFactory(SocialNetworkFactory):
    def __init__(self, credentials: FacebookCredentials):
        self.credentials = credentials

    def create_network(self) -> Facebook:
        return Facebook(self.credentials.login, self.credentials.password)


# Фабрика для створення LinkedIn
class LinkedInFactory(SocialNetworkFactory):
    def __init__(self, credentials: LinkedInCredentials):
        self.credentials = credentials

    def create_network(self) -> LinkedIn:
        return LinkedIn(self.credentials.email, self.credentials.password)


# Клас для публікації повідомлень
class SocialMediaPoster:
    def __init__(self, factory: SocialNetworkFactory):
        self.social_network = factory.create_network()

    def post(self, message: str) -> bool:
        """Публікує повідомлення у соціальній мережі"""
        # Підключаємось до мережі
        if not self.social_network.connect():
            return False

        # Публікуємо повідомлення
        success = self.social_network.post_message(message)

        # Відключаємось
        self.social_network.disconnect()
        return success


# Приклад використання
def main():
    # Створюємо креденшели для Facebook
    fb_creds = FacebookCredentials(
        login="user123",
        password="secret123"
    )

    # Створюємо креденшели для LinkedIn
    li_creds = LinkedInCredentials(
        email="user@example.com",
        password="secret456"
    )

    # Публікуємо у Facebook
    print("\n--- Публікація у Facebook ---")
    fb_factory = FacebookFactory(fb_creds)
    fb_poster = SocialMediaPoster(fb_factory)
    fb_poster.post("Привіт, Facebook! Це тестове повідомлення!")

    # Публікуємо у LinkedIn
    print("\n--- Публікація у LinkedIn ---")
    li_factory = LinkedInFactory(li_creds)
    li_poster = SocialMediaPoster(li_factory)
    li_poster.post("Привіт, LinkedIn! Це професійне повідомлення!")


if __name__ == "__main__":
    main()