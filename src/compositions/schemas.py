from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel

from src.compositions.models import Composition, Feedstock


class CompositionBase(BaseModel):
    code: str
    description: str
    unit: str


class ServiceBase(CompositionBase):
    id: int
    quantity: Decimal


class CompositionIn(CompositionBase):
    feedstock: Optional[List[Feedstock]]
    services: Optional[List[ServiceBase]]

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


class CompositionOut(CompositionBase):
    ...
    # @staticmethod
    # def from_dict(obj):
    #     return CompositionOut(
    #         code=obj["code"],
    #         description=obj["description"],
    #         unit=obj["unit_initial"],
    #     )

class CompositionServiceOut(CompositionIn):
    ...
