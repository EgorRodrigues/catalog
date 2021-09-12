from typing import List

from pydantic import BaseModel

from src.compositions.models import Feedstock
from src.compositions.models import Composition, Service


class CompositionBase(BaseModel):
    code: str
    description: str
    unit: str


class CompositionIn(CompositionBase):
    feedstock: List[Feedstock]
    services: List[Service]

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

    @property
    def from_dict(self):
        ...
