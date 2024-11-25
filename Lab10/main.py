from src.mediator.order_mediator import OrderMediator
from datetime import datetime, timedelta

def main():
    mediator = OrderMediator()

    mediator.date_component.select_date(datetime.now() + timedelta(days=3))
    print("🕒 Доступные слоты:", mediator.date_component.get_available_time_slots())

    mediator.recipient_component.toggle_different_recipient(True)
    mediator.recipient_component.set_recipient_details("Анна Петрова", "+380568452655")

    mediator.delivery_mode_component.toggle_self_pickup(True)

if __name__ == "__main__":
    main()
