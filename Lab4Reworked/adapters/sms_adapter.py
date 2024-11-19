from core.notifications import Notification
from core.providers import SMSProvider


class SMSNotificationAdapter(Notification):

    def __init__(self, phone: str, sender: str):
        self.phone = phone
        self.sender = sender
        self.sms_provider = SMSProvider()

    def send(self, title: str, message: str) -> None:
        formatted_message = f"{title}: {message}"
        self.sms_provider.send_sms(self.phone, self.sender, formatted_message)

