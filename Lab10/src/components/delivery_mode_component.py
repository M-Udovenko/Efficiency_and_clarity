from ..mediator.order_mediator import Colleague

class DeliveryModeComponent(Colleague):
    def __init__(self, mediator):
        super().__init__(mediator)
        self._self_pickup = False

    def toggle_self_pickup(self, is_self_pickup: bool):
        self._self_pickup = is_self_pickup
        self._mediator.delivery_mode_changed(is_self_pickup)
