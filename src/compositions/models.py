from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional


# Value Object
@dataclass
class Feedstock:
    id: int
    name: str
    unit: str
    quantity: Decimal
    # price: List


@dataclass
class _ParentCompositionBase:
    code: str
    description: str
    unit: str


@dataclass
class _ParentCompositionDefaults:
    feedstock: Optional[List[Feedstock]] = None
    services: Optional[List["Service"]] = None


@dataclass
class Composition(_ParentCompositionDefaults, _ParentCompositionBase):
    def add_feedstock(self, feedstock: Feedstock):
        self.feedstock.append(feedstock)

    def add_service(self, service: "Service"):
        self.services.append(service)


@dataclass
class _ParentServiceBase:
    id: int
    quantity: Decimal


@dataclass
class Service(_ParentCompositionDefaults, _ParentServiceBase, _ParentCompositionBase):
    ...
