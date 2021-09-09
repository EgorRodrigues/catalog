from pydantic import BaseModel

from src.units.models import Unit as UnitModel


class UnitBase(BaseModel):
    name: str
    initial: str


class UnitIn(UnitBase):
    def to_model(self) -> UnitModel:
        return UnitModel(
            name=self.name,
            initial=self.initial,
        )


class UnitInDB(UnitBase):
    id: int

    @staticmethod
    def from_dict(obj) -> "UnitInDB":
        return UnitInDB(
            id=obj["id"],
            name=obj["name"],
            initial=obj["initial"],
        )
