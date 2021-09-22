import abc

from src.config import database
from src.orm import units
from src.units.repository import DatabaseRepository
from src.units.services import UnitService

repository = DatabaseRepository(database, units)


class AsyncClient:
    @abc.abstractmethod
    async def get_slug(self, pk: int) -> str:
        ...

    @abc.abstractmethod
    async def get_id(self, slug: str) -> int:
        ...


class AsyncClientService(AsyncClient):
    async def get_slug(self, pk: int):
        return await UnitService(repository).get_slug(pk)

    async def get_id(self, slug: str) -> int:
        return await UnitService(repository).get_id_by_slug(slug)
