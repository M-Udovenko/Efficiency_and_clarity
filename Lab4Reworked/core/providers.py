class SlackAPI:

    def __init__(self, login: str, api_key: str):
        self.login = login
        self.api_key = api_key

    def login_to_slack(self) -> None:
        print(f"🔑 Авторизация в Slack с логином {self.login}")

    def post_message(self, chat_id: str, msg: str) -> None:
        print(f"💬 Отправка сообщения в Slack-чат {chat_id}: {msg}")


class SMSProvider:

    def send_sms(self, phone: str, sender: str, text: str) -> None:
        print(f"📱 SMS от {sender} на номер {phone}: {text}")

