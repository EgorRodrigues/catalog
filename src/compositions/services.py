from typing import List

from src.compositions.repository import Repository
from src.compositions.schemas import CompositionIn, CompositionInDB, CompositionOut


class CompositionService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(self, composition: CompositionIn) -> CompositionInDB:
        result = await self.repository.add(composition.to_model)
        return CompositionInDB.from_dict(result)

    async def prepare_list(self) -> List[CompositionOut]:
        result = await self.repository.get_all()
        return result
