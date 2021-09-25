from typing import Dict, List

from src.units.repository import Repository
from src.units.schemas import UnitIn, UnitInDB


class UnitService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(self, unit: UnitIn) -> UnitInDB:
        result = await self.repository.add(unit.to_model())
        return UnitInDB.from_dict(result)

    async def prepare_delete(self, pk: int) -> bool:
        result = await self.repository.delete(pk)
        return bool(result)

    async def prepare_list(self) -> List:
        result = await self.repository.get_all()
        return result

    async def prepare_item(self, pk: int) -> Dict:
        result = await self.repository.get_item(pk)
        return result

    async def get_slug(self, pk: int) -> str:
        result = await self.prepare_item(pk)
        return result["slug"]

    async def get_id_by_slug(self, slug: str) -> int:
        result = await self.repository.get_item_by_slug(slug)
        return result["id"]
