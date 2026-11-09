from dataclasses import dataclass
from typing import Iterable

@dataclass
class Product:
    name: str
    price: float
    qty: int = 1

def subtotal(items: Iterable[Product]) -> float:
    return sum(p.price * p.qty for p in items)

def apply_discount(amount: float, percent: float = 10.0) -> float:
    rate: float = percent / 100
    return round(amount * (1 - rate), 2)

cart: list[Product] = [
    Product("keyboard", 49.99, 2),
    Product("mouse", 19.50),
    Product("monitor", 199.00),
]

total: float = subtotal(cart)
final: float = apply_discount(total, 15)
print("items:", len(cart))
print("subtotal:", round(total, 2))
print("final:", final)
