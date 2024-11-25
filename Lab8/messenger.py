class Messenger:
    @staticmethod
    def send_admin_notification(message: str) -> None:
        """Отправка уведомления администратору"""
        print(f"🔔 Уведомление админу: {message}")
