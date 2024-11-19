from core.notifications import EmailNotification
from adapters.slack_adapter import SlackNotificationAdapter
from adapters.sms_adapter import SMSNotificationAdapter


def main():
    email_notification = EmailNotification("emailforlab4@example.com")
    slack_notification = SlackNotificationAdapter(
        login="user_for_lab4",
        api_key="xoxb-your-api-key",
        chat_id="general"
    )
    sms_notification = SMSNotificationAdapter(
        phone="+88005553535",
        sender="NotifyBot"
    )

    notifications = [
        (email_notification, "Тест Email", "Привет через Email! 👋"),
        (slack_notification, "Тест Slack", "Привет через Slack! 🚀"),
        (sms_notification, "Тест SMS", "Привет через SMS! 📱")
    ]

    print("🌟 Начинаем тестирование системы уведомлений!")
    print("=" * 50)

    for notifier, title, message in notifications:
        try:
            notifier.send(title, message)
            print("✅ Уведомление успешно отправлено!")
        except Exception as e:
            print(f"❌ Ошибка при отправке: {e}")
        print("-" * 50)

    print("🎉 Тестирование завершено!")


if __name__ == "__main__":
    main()