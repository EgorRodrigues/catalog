from typing import List

from fastapi import APIRouter, status

from src.config import database
from src.feedstock.repository import DatabaseRepository
from src.feedstock.schemas import FeedstockIn, FeedstockInDB, FeedstockOut
from src.feedstock.services import FeedstockService
from src.orm import feedstock as feedstock_table

router = APIRouter(prefix="/feedstock", tags=["feedstock"])
repository = DatabaseRepository(database, feedstock_table)


@router.post(
    "/", response_model=FeedstockInDB, status_code=status.HTTP_201_CREATED
)  # noqa
async def create(feedstock: FeedstockIn) -> FeedstockInDB:
    return await FeedstockService(repository).prepare_create(feedstock)


@router.get(
    "/", response_model=List[FeedstockOut], status_code=status.HTTP_200_OK
)  # noqa
async def get_items() -> List:
    return await FeedstockService(repository).prepare_list()


@router.get(
    "/{pk}", response_model=FeedstockOut, status_code=status.HTTP_200_OK
)  # noqa
async def get_item(pk: int) -> FeedstockOut:
    return await FeedstockService(repository).prepare_item(pk)


@router.delete("/{pk}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(pk: int) -> bool:
    return await FeedstockService(repository).prepare_delete(pk)
