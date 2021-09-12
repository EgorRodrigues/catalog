from dataclasses import asdict
from typing import Dict, List, Protocol, runtime_checkable

from databases import Database
from sqlalchemy import Table

from src.units.models import Unit


@runtime_checkable
class Repository(Protocol):
    async def add(self, unit: Unit) -> Dict:
        """Method responsible for including the item in the db"""

    async def delete(self, pk: int) -> bool:
        """Method responsible for deleting the item in the db"""

    async def get_items(self) -> List:
        """Method responsible for deleting the item in the db"""


class DatabaseRepository:
    def __init__(self, database: Database, table: Table):
        self.database = database
        self.table = table

    async def add(self, unit: Unit) -> Dict:
        query = self.table.insert().values(
            name=unit.name,
            initial=unit.initial,
        )
        last_record_id = await self.database.execute(query=query)
        return {"id": last_record_id, **asdict(unit)}

    async def delete(self, pk: int) -> bool:
        query = self.table.delete().where(
            self.table.c.id == pk,
        )
        result = await self.database.execute(query=query)
        return bool(result)

    async def get_items(self) -> List:
        query = self.table.select()
        rows = await self.database.fetch_all(query=query)
        result = [dict(row) for row in rows]
        return result
