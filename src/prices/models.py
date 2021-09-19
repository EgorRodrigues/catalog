from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


# Value Object
@dataclass
class Feedstock:
    id: int
    name: str
    unit: str


@dataclass
class Price:
    date_create: datetime
    price: Decimal
    feedstock: Feedstock
