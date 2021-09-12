from typing import List

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
        result = await self.repository.get_items()
        return result
