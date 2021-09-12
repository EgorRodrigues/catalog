from fastapi import APIRouter, status

from src.compositions.repository import DatabaseRepository
from src.compositions.schemas import CompositionIn, CompositionInDB
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
