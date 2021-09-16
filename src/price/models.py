from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class price:
    date: datetime
    price: Decimal
    feedstock: int
