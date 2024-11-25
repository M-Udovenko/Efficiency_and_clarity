from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Product:
    id: int
    name: str
    price: float
    description: str


@dataclass
class User:
    id: int
    name: str
    email: str
    phone: str


@dataclass
class Order:
    id: int
    user_id: int
    products: list
    total: float
    status: str
