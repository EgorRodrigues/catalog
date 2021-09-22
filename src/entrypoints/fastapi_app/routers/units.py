from typing import List

from fastapi import APIRouter, HTTPException, status

from src.config import database
from src.orm import units
from src.units.repository import DatabaseRepository
from src.units.schemas import UnitIn, UnitInDB, UnitOut
from src.units.services import UnitService

router = APIRouter(prefix="/units", tags=["units"])
repository = DatabaseRepository(database, units)


@router.get("/", response_model=List[UnitOut], status_code=status.HTTP_200_OK)
async def get_items():
    return await UnitService(repository).prepare_list()


@router.get("/{pk}", response_model=UnitOut, status_code=status.HTTP_200_OK)
async def get_item(pk: int):
    return await UnitService(repository).prepare_item(pk)


@router.post("/", response_model=UnitInDB, status_code=status.HTTP_201_CREATED)
async def create(unit: UnitIn):
    return await UnitService(repository).prepare_create(unit)


@router.delete("/{pk}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(pk: int):
    result = await UnitService(repository).prepare_delete(pk)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Change could not be made because the units was not found",
        )
