from dataclasses import dataclass

from dataclasses import dataclass, field

def get_pet_name():
    pet_name = "dog-tobby"
    return pet_name


@dataclass
class DefaultFactoryExample:
    name: str
    number_cards: int
    pet_name: str

    # default values
    credit_limit: float = field(default=200.5)
    pet_name: float = field(default_factory=get_pet_name)

p1 = DefaultFactoryExample("John", 2, 100.5)
p2 = DefaultFactoryExample("John2", 5)
print(f"customer data instance::{p1}")
print(f"customer data instance::{p2}")
