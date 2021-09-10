from fastapi import APIRouter, status

from src.config import database
from src.items.repository import DatabaseRepository
from src.items.schemas import ItemIn, ItemInDB
from src.items.services import ItemService
from src.orm import items as items_table
from src.orm import units as units_table

router = APIRouter(prefix="/items", tags=["items"])
repository = DatabaseRepository(database, units_table, items_table)


@router.post("/", response_model=ItemInDB, status_code=status.HTTP_201_CREATED)
async def create(item: ItemIn):
    return await ItemService(repository).prepare_create(item)
