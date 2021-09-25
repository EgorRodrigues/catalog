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

    async def get_all(self) -> List:
        """Method responsible for deleting the item in the db"""

    async def get_item(self, pk: int) -> Dict:
        """Method responsible for return an item in the db"""

    async def get_item_by_slug(self, slug: str) -> Dict:
        """Method responsible for return an item in the db"""


class DatabaseRepository:
    def __init__(self, database: Database, units_table: Table):
        self.database = database
        self.units_table = units_table

    async def add(self, unit: Unit) -> Dict:
        query = self.units_table.insert().values(
            name=unit.name,
            slug=unit.slug,
        )
        last_record_id = await self.database.execute(query=query)
        return {"id": last_record_id, **asdict(unit)}

    async def delete(self, pk: int) -> bool:
        query = self.units_table.delete().where(
            self.units_table.c.id == pk,
        )
        result = await self.database.execute(query=query)
        return bool(result)

    async def get_all(self) -> List:
        query = self.units_table.select()
        rows = await self.database.fetch_all(query=query)
        result = [dict(row) for row in rows]
        return result

    async def get_item(self, pk: int) -> Dict:
        query = self.units_table.select().where(self.units_table.c.id == pk)
        result = await self.database.fetch_one(query=query)
        return dict(result)

    async def get_item_by_slug(self, slug: str) -> Dict:
        query = self.units_table.select().where(self.units_table.c.slug == slug)  # noqa
        result = await self.database.fetch_one(query=query)
        return dict(result)
