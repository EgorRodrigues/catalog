from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List


@dataclass
class Feedstock:
    name: str
    unit: str
    price: List["Price"]


@dataclass
class Price:
    date_create: datetime
    price: Decimal
    feedstock: Feedstock
