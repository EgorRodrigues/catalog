from fastapi import APIRouter, status

from src.config import database
from src.orm import feedstock as feedstock_table
from src.orm import prices as prices_table
from src.prices.repository import DatabaseRepository
from src.prices.schemas import PriceIn, PriceInDB
from src.prices.services import PriceService

router = APIRouter(prefix="/price", tags=["Price"])
repository = DatabaseRepository(database, feedstock_table, prices_table)


@router.post("/", response_model=PriceInDB, status_code=status.HTTP_201_CREATED)  # noqa
async def create(price: PriceIn) -> PriceInDB:
    return await PriceService(repository).prepare_create(price)


#
# @router.get("/", response_model=List[FeedstockOut],
# status_code=status.HTTP_200_OK)
# async def list_feedstock() -> List:
#     return await FeedstockService(repository).prepare_list()
#
#
# @router.get("/{pk}",
# response_model=FeedstockOut,
# status_code=status.HTTP_200_OK) noqa
# async def get_item(pk: int) -> FeedstockOut:
#     return await FeedstockService(repository).prepare_item(pk)
#
#
# @router.delete("/{pk}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete(pk: int) -> bool:
#     return await FeedstockService(repository).prepare_delete(pk)
