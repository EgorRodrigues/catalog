from pydantic import BaseModel

from src.feedstock.models import Feedstock


class FeedstockBase(BaseModel):
    description: str
    unit: str


class FeedstockIn(FeedstockBase):
    @property
    def to_model(self) -> Feedstock:
        return Feedstock(
            description=self.description,
            unit=self.unit,
        )


class FeedstockInDB(FeedstockBase):
    id: int

    @staticmethod
    def from_dict(obj) -> "FeedstockInDB":
        return FeedstockInDB(
            id=obj["id"],
            description=obj["description"],
            unit=obj["unit"],
        )


class FeedstockOut(FeedstockBase):
    id: int

    @staticmethod
    def from_dict(obj) -> "FeedstockOut":
        return FeedstockOut(
            id=obj["id"],
            description=obj["description"],
            unit=obj["unit"],
        )
