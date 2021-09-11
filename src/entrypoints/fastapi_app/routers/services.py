from fastapi import APIRouter, status

from src.config import database
from src.orm import items as items_table
from src.orm import list_items as list_items_table
from src.orm import list_services as list_services_table
from src.orm import services as services_table
from src.orm import units as units_table
from src.services.repository import DatabaseRepository
from src.services.schemas import ServiceIn, ServiceInDB
from src.services.services import ServiceService

router = APIRouter(prefix="/services", tags=["services"])
repository = DatabaseRepository(
    database,
    units_table,
    items_table,
    services_table,
    list_items_table,
    list_services_table,
)


@router.post("/", response_model=ServiceInDB, status_code=status.HTTP_201_CREATED)
async def create(service: ServiceIn):
    return await ServiceService(repository).prepare_create(service)
