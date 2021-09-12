from decimal import Decimal
from typing import Dict, List, Optional

from pydantic import BaseModel

from src.compositions.models import Composition, Feedstock


class CompositionBase(BaseModel):
    code: str
    description: str
    unit: str


class ServiceSchema(CompositionBase):
    id: int
    quantity: Decimal


class CompositionIn(CompositionBase):
    feedstock: Optional[List[Feedstock]]
    services: Optional[List[ServiceSchema]]

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
        ...
