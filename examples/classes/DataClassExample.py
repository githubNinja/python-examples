from dataclasses import dataclass

from dataclasses import dataclass, field


@dataclass
class Customer:
    name: str
    number_cards: int

    # default values
    credit_limit: float = field(default=200.5)


p1 = Customer("John", 2, 100.5)
p2 = Customer("John2", 5)
print(f"customer data instance::{p1}")
print(f"customer data instance::{p2}")
