from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional


# Value Object
@dataclass
class Feedstock:
    feedstock_id: int
    quantity: Decimal


@dataclass
class Service:
    service_id: int
    quantity: Decimal


@dataclass
class Composition:
    code: str
    description: str
    unit: str
    feedstock: Optional[List[Feedstock]] = None
    services: Optional[List[Service]] = None

    def add_feedstock(self, feedstock: Feedstock):
        self.feedstock.append(feedstock)

    def add_service(self, service: "Service"):
        self.services.append(service)
