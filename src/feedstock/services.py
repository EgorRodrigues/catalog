from typing import List

from src.feedstock.repository import Repository
from src.feedstock.schemas import FeedstockIn, FeedstockInDB, FeedstockOut


class FeedstockService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(self, feedstock: FeedstockIn) -> FeedstockInDB:
        result = await self.repository.add(feedstock.to_model)
        return FeedstockInDB.from_dict(result)

    async def prepare_delete(self, pk: int) -> bool:
        result = await self.repository.delete(pk)
        return bool(result)

    async def prepare_item(self, pk: int) -> FeedstockOut:
        result = await self.repository.get_item(pk)
        return result

    async def prepare_list(self) -> List:
        result = await self.repository.get_all()
        return result
