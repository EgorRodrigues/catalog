from dataclasses import asdict
from typing import Dict, Protocol, runtime_checkable

from databases import Database
from sqlalchemy import Table

from src.items.models import Item


@runtime_checkable
class Repository(Protocol):
    async def add(self, item: Item) -> Dict:
        """Method responsible for including the item in the db"""


class DatabaseRepository:
    def __init__(self, database: Database, table: Table):
        self.database = database
        self.table = table

    async def add(self, item: Item) -> Dict:
        query = self.table.insert().values(
            name=item.name,
            unit_name=item.unit.name,
            unit_initial=item.unit.initial,
        )
        last_record_id = await self.database.execute(query=query)
        return {"id": last_record_id, **asdict(item)}
