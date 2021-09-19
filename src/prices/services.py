from src.prices.repository import Repository
from src.prices.schemas import PriceIn, PriceInDB


class PriceService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(self, price: PriceIn) -> PriceInDB:
        result = await self.repository.add(price.to_model)
        return PriceInDB.from_dict(result)
