from dataclasses import asdict
from typing import Dict, List, Protocol, runtime_checkable

from databases import Database
from sqlalchemy import Table, select

from src.feedstock.models import Feedstock
from src.feedstock.schemas import FeedstockOut


@runtime_checkable
class Repository(Protocol):
    async def add(self, feedstock: Feedstock) -> Dict:
        """Method responsible for including the feedstock in the db"""

    async def delete(self, pk: int) -> bool:
        """Method responsible for excluding the feedstock in the db"""

    async def get_all(self) -> List:
        """Method responsible for geting the list feedstock in the db"""

    async def get_item(self, pk) -> FeedstockOut:
        """Method responsible for excluding the feedstock in the db"""


class DatabaseRepository:
    def __init__(
        self,
        database: Database,
        units_table: Table,
        items_table: Table,
    ):
        self.database = database
        self.units_table = units_table
        self.feedstock_table = items_table

    async def add(self, feedstock: Feedstock) -> Dict:
        unit_id = select(self.units_table.c.id).where(
            self.units_table.c.initial == feedstock.unit
        )
        query = self.feedstock_table.insert().values(
            name=feedstock.name,
            unit_id=unit_id.scalar_subquery(),
        )
        last_record_id = await self.database.execute(query)
        return {"id": last_record_id, **asdict(feedstock)}

    async def delete(self, pk: int) -> bool:
        query = self.feedstock_table.delete().where(self.feedstock_table.c.id == pk)
        result = self.database.execute(query)
        return bool(result)

    async def get_all(self) -> List:
        query = select(
            [
                self.feedstock_table,
                self.units_table.c.initial.label("unit"),
            ]
        ).select_from(self.feedstock_table.join(self.units_table))
        rows = await self.database.fetch_all(query=query)
        result = [dict(row) for row in rows]
        return result

    async def get_item(self, pk: int) -> FeedstockOut:
        query = (
            select(
                [
                    self.feedstock_table,
                    self.units_table.c.initial.label("unit"),
                ]
            )
            .select_from(self.feedstock_table.join(self.units_table))
            .where(self.feedstock_table.c.id == pk)
        )
        result = await self.database.fetch_one(query=query)
        return FeedstockOut.from_dict(result)
