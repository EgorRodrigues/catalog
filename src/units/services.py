from src.units.repository import Repository
from src.units.schemas import UnitIn, UnitInDB


class UnitService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(self, unit: UnitIn) -> UnitInDB:
        result = await self.repository.add(unit.to_model())
        return UnitInDB.from_dict(result)
