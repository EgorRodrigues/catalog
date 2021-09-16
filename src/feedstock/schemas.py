from typing import Dict

from pydantic import BaseModel

from src.feedstock.models import Feedstock


class FeedstockBase(BaseModel):
    name: str
    unit: str


class FeedstockIn(FeedstockBase):
    def to_model(self) -> Feedstock:
        return Feedstock(
            name=self.name,
            unit=self.unit,
        )


class FeedstockInDB(FeedstockBase):
    id: int

    @staticmethod
    def from_dict(obj) -> "FeedstockInDB":
        return FeedstockInDB(
            id=obj["id"],
            name=obj["name"],
            unit=obj["unit"],
        )


class FeedstockOut(FeedstockBase):
    id: int

    @staticmethod
    def from_dict(obj) -> "FeedstockOut":
        return FeedstockOut(
            id=obj["id"],
            name=obj["name"],
            unit=obj["unit"],
        )
