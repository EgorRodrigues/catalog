from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

from src.prices.models import Price


# todo verificar problemas com o Pydantic na importação do Feedstock
class Feedstock(BaseModel):
    id: int
    description: str
    unit: str


class PriceBase(BaseModel):
    date_create: datetime
    price: Decimal
    feedstock: Feedstock


class PriceIn(PriceBase):
    @property
    def to_model(self) -> Price:
        return Price(
            date_create=self.date_create,
            price=self.price,
            feedstock=self.feedstock,
        )


class PriceInDB(PriceBase):
    id: int

    @staticmethod
    def from_dict(obj) -> "PriceInDB":
        return PriceInDB(
            id=obj["id"],
            date_create=obj["date_create"],
            price=obj["price"],
            feedstock=obj["feedstock"],
        )
