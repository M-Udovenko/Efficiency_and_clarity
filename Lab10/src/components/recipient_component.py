from ..mediator.order_mediator import Colleague

class RecipientComponent(Colleague):
    def __init__(self, mediator):
        super().__init__(mediator)
        self._is_different_recipient = False
        self._recipient_name = ""
        self._recipient_phone = ""

    def toggle_different_recipient(self, is_different: bool):
        self._is_different_recipient = is_different
        self._mediator.recipient_toggle_changed(is_different)

    def set_recipient_details(self, name: str, phone: str):
        self._recipient_name = name
        self._recipient_phone = phone
        self._mediator.recipient_details_changed()
