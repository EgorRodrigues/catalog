from dataclasses import asdict
from typing import Dict, Protocol

from databases import Database
from sqlalchemy import Table, select

from src.price.models import Price


class Repository(Protocol):
    async def add(self, price: Price) -> Dict:
        """Method responsible for including the price in the db"""


class DatabaseRepository:
    def __init__(self, database: Database, feedstock_table: Table, prices_table: Table):
        self.database = database
        self.feedstock_table = feedstock_table
        self.price_table = prices_table

    async def add(self, price: Price) -> Dict:
        feedstock_id = select(self.feedstock_table.c.id).where(
            self.feedstock_table.c.id == price.feedstock
        )
        query = self.price_table.insert().values(
            data_create=price.date_create,
            price=price.price,
            feedstock=feedstock_id.scalar_subquery(),
        )
        last_price_id = await self.database.execute(query=query)
        return {"id": last_price_id, **asdict(price)}
