from fastapi import APIRouter, status

from src.config import database
from src.orm import units
from src.units.repository import DatabaseRepository
from src.units.schemas import UnitIn, UnitInDB
from src.units.services import UnitService

router = APIRouter(prefix="/units", tags=["units"])
repository = DatabaseRepository(database, units)


@router.post("/", response_model=UnitInDB, status_code=status.HTTP_201_CREATED)
async def create(unit: UnitIn):
    return await UnitService(repository).prepare_create(unit)
