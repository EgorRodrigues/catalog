from src.feedstock.repository import Repository
from src.feedstock.schemas import FeedstockIn, FeedstockInDB


class FeedstockService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(self, feedstock: FeedstockIn) -> FeedstockInDB:
        result = await self.repository.add(feedstock.to_model())
        return FeedstockInDB.from_dict(result)
