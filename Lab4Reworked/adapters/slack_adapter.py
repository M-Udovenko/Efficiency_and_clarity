from core.notifications import Notification
from core.providers import SlackAPI


class SlackNotificationAdapter(Notification):

    def __init__(self, login: str, api_key: str, chat_id: str):
        self.slack = SlackAPI(login, api_key)
        self.chat_id = chat_id
        self.slack.login_to_slack()

    def send(self, title: str, message: str) -> None:
        formatted_message = f"*{title}*\n{message}"
        self.slack.post_message(self.chat_id, formatted_message)

