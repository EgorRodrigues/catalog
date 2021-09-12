from src.compositions.repository import Repository
from src.compositions.schemas import CompositionIn, CompositionInDB


class ServiceService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(self, composition: CompositionIn) -> CompositionInDB:
        result = await self.repository.add(composition.to_model)
        return CompositionInDB.from_dict(result)
