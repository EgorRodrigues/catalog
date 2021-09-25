from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel

from src.compositions.models import Composition

# Feedstock = dataclasses.dataclass(Feedstock)


class FeedstockSchema(BaseModel):
    quantity: Decimal
    feedstock_id: int


class CompositionBase(BaseModel):
    code: str
    description: str
    unit: str


class ServiceBase(BaseModel):
    quantity: Decimal


class ServiceIn(ServiceBase):
    composition_id: int


class CompositionIn(CompositionBase):
    feedstock: Optional[List[FeedstockSchema]]
    services: Optional[List[ServiceIn]]

    @property
    def to_model(self) -> Composition:
        return Composition(
            code=self.code,
            description=self.description,
            unit=self.unit,
            feedstock=self.feedstock,
            services=self.services,
        )


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


class FeedstockOut(FeedstockSchema):
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
