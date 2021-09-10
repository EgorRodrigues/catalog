from pydantic import BaseModel

from src.items.models import Item as ItemModel


class ItemBase(BaseModel):
    name: str
    unit: str


class ItemIn(ItemBase):
    def to_model(self) -> ItemModel:
        return ItemModel(
            name=self.name,
            unit=self.unit,
        )


class ItemInDB(ItemBase):
    id: int

    @staticmethod
    def from_dict(obj) -> "ItemInDB":
        return ItemInDB(
            id=obj["id"],
            name=obj["name"],
            unit=obj["unit"],
        )
