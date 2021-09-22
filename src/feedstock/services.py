from typing import List

from src.feedstock.repository import Repository
from src.feedstock.schemas import FeedstockIn, FeedstockInDB, FeedstockOut
from src.units.entrypoints.clients import AsyncClientService as UnitClient


class FeedstockService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(self, feedstock: FeedstockIn) -> FeedstockInDB:
        feedstock.unit = await UnitClient().get_id(slug=feedstock.unit)
        result = await self.repository.add(feedstock.to_model)
        return FeedstockInDB.from_dict(result)

    async def prepare_delete(self, pk: int) -> bool:
        result = await self.repository.delete(pk)
        return bool(result)

    async def prepare_item(self, pk: int) -> FeedstockOut:
        result = await self.repository.get_item(pk)
        result["unit"] = await UnitClient().get_slug(result["unit_id"])
        return FeedstockOut.from_dict(result)

    async def prepare_list(self) -> List:
        result = await self.repository.get_all()
        for item in result:
            item["unit"] = await UnitClient().get_slug(item["unit_id"])
        return result
