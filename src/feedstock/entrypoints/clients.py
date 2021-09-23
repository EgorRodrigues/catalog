import abc
from typing import List

from src.config import database
from src.feedstock.repository import DatabaseRepository
from src.feedstock.schemas import FeedstockOut
from src.feedstock.services import FeedstockService
from src.orm import feedstock as feedstock_table

repository = DatabaseRepository(database, feedstock_table)


class AsyncClient:
    @abc.abstractmethod
    async def get_items(self) -> List:
        ...

    @abc.abstractmethod
    async def get_item(self, pk: int) -> FeedstockOut:
        ...


class AsyncClientService(AsyncClient):
    @abc.abstractmethod
    async def get_items(self) -> List:
        return await FeedstockService(repository).prepare_list()

    @abc.abstractmethod
    async def get_item(self, pk: int) -> FeedstockOut:
        return await FeedstockService(repository).prepare_item(pk)
