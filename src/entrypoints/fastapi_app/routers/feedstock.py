from typing import List

from fastapi import APIRouter, status

from src.config import database
from src.feedstock.repository import DatabaseRepository
from src.feedstock.schemas import FeedstockIn, FeedstockInDB, FeedstockOut
from src.feedstock.services import FeedstockService
from src.orm import feedstock as feedstock_table
from src.orm import units as units_table

router = APIRouter(prefix="/feedstock", tags=["feedstock"])
repository = DatabaseRepository(database, units_table, feedstock_table)


@router.post("/", response_model=FeedstockInDB, status_code=status.HTTP_201_CREATED)
async def create(feedstock: FeedstockIn) -> FeedstockInDB:
    return await FeedstockService(repository).prepare_create(feedstock)


@router.get("/", response_model=List[FeedstockOut], status_code=status.HTTP_200_OK)
async def list_feedstock() -> List:
    return await FeedstockService(repository).prepare_list()


@router.get("/{pk}", response_model=FeedstockOut, status_code=status.HTTP_200_OK)
async def get_item(pk: int) -> FeedstockOut:
    return await FeedstockService(repository).prepare_item(pk)


@router.delete("/{pk}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(pk: int) -> bool:
    return await FeedstockService(repository).prepare_delete(pk)
