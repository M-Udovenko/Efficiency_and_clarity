from dataclasses import dataclass


@dataclass
class DeliveryDetails:
    distance_km: float
    weight_kg: float
    is_express: bool = False
