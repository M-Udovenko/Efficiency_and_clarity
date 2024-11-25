from abc import ABC


class Colleague(ABC):
    def __init__(self, mediator):
        self._mediator = mediator

class OrderMediator:
    def __init__(self):
        from ..components.date_component import DeliveryDateComponent
        from ..components.recipient_component import RecipientComponent
        from ..components.delivery_mode_component import DeliveryModeComponent

        self.date_component = DeliveryDateComponent(self)
        self.recipient_component = RecipientComponent(self)
        self.delivery_mode_component = DeliveryModeComponent(self)

    def date_changed(self, selected_date):
        print(f"📅 Выбрана дата: {selected_date.strftime('%d.%m.%Y')}")

    def recipient_toggle_changed(self, is_different_recipient):
        if is_different_recipient:
            print("👥 Получатель: Другое лицо (требуются дополнительные детали)")
        else:
            print("👤 Получатель: Я сам")

    def recipient_details_changed(self):
        print("🔍 Детали получателя обновлены")

    def delivery_mode_changed(self, is_self_pickup):
        if is_self_pickup:
            print("🏪 Самовывоз: Активирован!")
        else:
            print("🚚 Доставка: Готовы покорять расстояния!")
