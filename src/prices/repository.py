from dataclasses import asdict
from typing import Dict, Protocol

from databases import Database
from sqlalchemy import Table, select

from src.prices.models import Price


class Repository(Protocol):
    async def add(self, price: Price) -> Dict:
        """Method responsible for including the prices in the db"""


class DatabaseRepository:
    def __init__(
        self,
        database: Database,
        feedstock_table: Table,
        prices_table: Table,
    ):
        self.database = database
        self.feedstock_table = feedstock_table
        self.price_table = prices_table

    async def add(self, price: Price) -> Dict:
        feedstock_id = select(self.feedstock_table.c.id).where(
            self.feedstock_table.c.id == price.feedstock.id
        )
        query = self.price_table.insert().values(
            date_create=price.date_create,
            price=price.price,
            feedstock_id=feedstock_id.scalar_subquery(),
        )
        print(query)
        last_price_id = await self.database.execute(query=query)
        return {"id": last_price_id, **asdict(price)}
