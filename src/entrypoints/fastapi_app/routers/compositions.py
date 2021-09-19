from typing import List

from fastapi import APIRouter, status

from src.compositions.repository import DatabaseRepository
from src.compositions.schemas import CompositionIn, CompositionInDB, CompositionOut, CompositionServiceOut
from src.compositions.services import CompositionService
from src.config import database
from src.orm import compositions as compositions_table
from src.orm import compositions_feedstock as compositions_feedstock_table
from src.orm import compositions_services as compositions_services_table
from src.orm import feedstock as feedstock_table
from src.orm import units as units_table

router = APIRouter(prefix="/compositions", tags=["compositions"])
repository = DatabaseRepository(
    database,
    units_table,
    feedstock_table,
    compositions_table,
    compositions_feedstock_table,
    compositions_services_table,
)


@router.post("/", response_model=CompositionInDB, status_code=status.HTTP_201_CREATED)
async def create(composition: CompositionIn):
    return await CompositionService(repository).prepare_create(composition)


@router.get("/", response_model=List[CompositionOut], status_code=status.HTTP_200_OK)
async def get_items():
    return await CompositionService(repository).prepare_list()


@router.get("/{pk}", response_model=CompositionServiceOut, status_code=status.HTTP_200_OK)
async def get_items(pk: int) -> CompositionServiceOut:
    return await CompositionService(repository).prepare_composition(pk)
