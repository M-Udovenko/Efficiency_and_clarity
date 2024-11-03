from abc import ABC, abstractmethod


# Початковий інтерфейс
class Notification:
    @abstractmethod
    def send(self, title: str, message: str) -> None:
        pass


# Початковий клас для відправки email
class EmailNotification(Notification):
    def __init__(self, admin_email: str):
        self.admin_email = admin_email

    def send(self, title: str, message: str) -> None:
        """Логіка відправки email"""
        print(f"Відправлено email з заголовком '{title}' на адресу '{self.admin_email}' з повідомленням '{message}'")


# Клас для роботи зі Slack API
class SlackAPI:
    def __init__(self, login: str, api_key: str):
        self.login = login
        self.api_key = api_key

    def login_to_slack(self) -> bool:
        """Логіка авторизації у Slack"""
        print(f"Авторизація у Slack з логіном {self.login}")
        return True

    def post_message(self, chat_id: str, message_text: str) -> bool:
        """Логіка відправки повідомлення у Slack"""
        print(f"Відправка повідомлення у Slack чат {chat_id}: {message_text}")
        return True


# Адаптер для Slack
class SlackNotificationAdapter(Notification):
    def __init__(self, login: str, api_key: str, chat_id: str):
        self.slack = SlackAPI(login, api_key)
        self.chat_id = chat_id
        # Авторизуємося одразу при створенні адаптера
        self.slack.login_to_slack()

    def send(self, title: str, message: str) -> None:
        """Адаптує відправку повідомлення для Slack"""
        # Формуємо повідомлення у форматі Slack
        formatted_message = f"*{title}*\n{message}"
        self.slack.post_message(self.chat_id, formatted_message)


# Клас для роботи з SMS API
class SMSService:
    def __init__(self, phone: str, sender: str):
        self.phone = phone
        self.sender = sender

    def send_sms(self, text: str) -> bool:
        """Логіка відправки SMS"""
        print(f"Відправка SMS від {self.sender} на номер {self.phone}: {text}")
        return True


# Адаптер для SMS
class SMSNotificationAdapter(Notification):
    def __init__(self, phone: str, sender: str):
        self.sms_service = SMSService(phone, sender)

    def send(self, title: str, message: str) -> None:
        """Адаптує відправку повідомлення для SMS"""
        # Об'єднуємо заголовок і повідомлення, бо в SMS немає окремого заголовку
        sms_text = f"{title}: {message}"
        self.sms_service.send_sms(sms_text)


# Клієнтський код для демонстрації роботи
def main():
    # Створюємо сповіщення для email
    email_notification = EmailNotification("admin@example.com")

    # Створюємо адаптер для Slack
    slack_notification = SlackNotificationAdapter(
        login="admin",
        api_key="slack-api-key-123",
        chat_id="general-channel"
    )

    # Створюємо адаптер для SMS
    sms_notification = SMSNotificationAdapter(
        phone="+380981231231",
        sender="NotifyService"
    )

    # Відправляємо тестові повідомлення
    print("\n=== Відправка Email ===")
    email_notification.send(
        "Сервер не відповідає",
        "Виявлено проблему з сервером DB-2"
    )

    print("\n=== Відправка у Slack ===")
    slack_notification.send(
        "Високе навантаження",
        "Навантаження на сервер APP-1 перевищує 80%"
    )

    print("\n=== Відправка SMS ===")
    sms_notification.send(
        "Критична помилка",
        "Термінова необхідність перезавантаження сервера"
    )


if __name__ == "__main__":
    main()