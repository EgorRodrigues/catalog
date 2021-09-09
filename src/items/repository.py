from dataclasses import asdict
from typing import Dict, Protocol, runtime_checkable

from databases import Database
from sqlalchemy import Table
from sqlalchemy.sql import select

from src.items.models import Item


@runtime_checkable
class Repository(Protocol):
    async def add(self, item: Item) -> Dict:
        """Method responsible for including the item in the db"""


class DatabaseRepository:
    def __init__(
        self,
        database: Database,
        units_table: Table,
        items_table: Table,
    ):
        self.database = database
        self.units_table = (units_table,)
        self.items_table = (items_table,)

    async def add(self, item: Item) -> Dict:
        unit_id = (
            select([self.units_table.c.id])
            .where(self.units_table.c.initial == item.unit)
            .limit(1)
        )
        query = self.items_table.insert().values(
            name=item.name,
            unit=unit_id,
        )
        last_record_id = await self.database.execute(query=query)
        return {"id": last_record_id, **asdict(item)}
