from fastapi import APIRouter, status

from src.config import database
from src.feedstock.repository import DatabaseRepository
from src.feedstock.schemas import FeedstockIn, FeedstockInDB
from src.feedstock.services import FeedstockService
from src.orm import feedstock as feedstock_table
from src.orm import units as units_table

router = APIRouter(prefix="/feedstock", tags=["feedstock"])
repository = DatabaseRepository(database, units_table, feedstock_table)


@router.post("/", response_model=FeedstockInDB, status_code=status.HTTP_201_CREATED)
async def create(item: FeedstockIn):
    return await FeedstockService(repository).prepare_create(item)
