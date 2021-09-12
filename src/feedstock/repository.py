from dataclasses import asdict
from typing import Dict, Protocol, runtime_checkable

from databases import Database
from sqlalchemy import Table, select

from src.feedstock.models import Feedstock


@runtime_checkable
class Repository(Protocol):
    async def add(self, feedstock: Feedstock) -> Dict:
        """Method responsible for including the item in the db"""


class DatabaseRepository:
    def __init__(
        self,
        database: Database,
        units_table: Table,
        items_table: Table,
    ):
        self.database = database
        self.units_table = units_table
        self.items_table = items_table

    async def add(self, feedstock: Feedstock) -> Dict:
        unit_id = select(self.units_table.c.id).where(
            self.units_table.c.initial == feedstock.unit
        )
        query = self.items_table.insert().values(
            name=feedstock.name,
            unit_id=unit_id.scalar_subquery(),
        )
        last_record_id = await self.database.execute(query)
        return {"id": last_record_id, **asdict(feedstock)}
