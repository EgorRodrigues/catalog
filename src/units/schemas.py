from pydantic import BaseModel

from src.units.models import Unit as UnitModel


class UnitBase(BaseModel):
    name: str
    slug: str


class UnitIn(UnitBase):
    def to_model(self) -> UnitModel:
        return UnitModel(
            name=self.name,
            slug=self.slug,
        )


class UnitInDB(UnitBase):
    id: int

    @staticmethod
    def from_dict(obj) -> "UnitInDB":
        return UnitInDB(
            id=obj["id"],
            name=obj["name"],
            slug=obj["slug"],
        )


class UnitOut(UnitBase):
    id: int
