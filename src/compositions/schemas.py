from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel

from src.compositions.models import Composition, Feedstock, Service

# Feedstock = dataclasses.dataclass(Feedstock)

#
# class FeedstockSchema(BaseModel):
#     quantity: Decimal
#     feedstock_id: int


class CompositionBase(BaseModel):
    code: str
    description: str
    unit: str


class ServiceBase(BaseModel):
    quantity: Decimal


class ServiceIn(ServiceBase):
    service_id: int


class CompositionIn(CompositionBase):
    feedstock: Optional[List[Feedstock]]
    services: Optional[List[ServiceIn]]

    @property
    def to_model(self) -> Composition:
        if self.feedstock:
            self._list_feedstock()

        if self.services:
            self._list_service()

        return Composition(
            code=self.code,
            description=self.description,
            unit=self.unit,
            feedstock=self.feedstock,
            services=self.services,
        )

    def _list_feedstock(self):
        feedstock_list = []
        for feedstock in self.feedstock:
            feedstock_list.append(Feedstock(feedstock.feedstock_id, feedstock.quantity))
        self.feedstock = feedstock_list

    def _list_service(self):
        services_list = []
        for service in self.services:
            services_list.append(Service(service.service_id, service.quantity))
        self.services = services_list


class CompositionInDB(CompositionBase):
    id: int

    @staticmethod
    def from_dict(obj):
        return CompositionInDB(
            id=obj["id"],
            code=obj["code"],
            description=obj["description"],
            unit=obj["unit"],
        )


class FeedstockOut(Feedstock):
    description: str
    unit: str


class CompositionOut(CompositionBase):
    ...


class ServiceOut(ServiceBase):
    service_id: int
    code: str
    description: str
    unit: str


class CompositionServiceOut(CompositionBase, ServiceBase):
    feedstock: Optional[List[FeedstockOut]]
    services: Optional[List[ServiceOut]]
