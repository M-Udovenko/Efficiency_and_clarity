from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, title: str, message: str) -> None:
        pass


class EmailNotification(Notification):

    def __init__(self, admin_email: str):
        self.admin_email = admin_email

    def send(self, title: str, message: str) -> None:
        print(f"✉️ Отправлено email с заголовком '{title}' на адрес '{self.admin_email}' с сообщением '{message}'")

