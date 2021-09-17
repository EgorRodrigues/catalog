from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class price:
    date_create: datetime
    price: Decimal
    feedstock: int
