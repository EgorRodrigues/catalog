from src.items.repository import Repository
from src.items.schemas import ItemIn, ItemInDB


class ItemService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(self, unit: ItemIn) -> ItemInDB:
        result = await self.repository.add(unit.to_model())
        return ItemInDB.from_dict(result)
