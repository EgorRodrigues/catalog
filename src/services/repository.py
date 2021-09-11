from dataclasses import asdict
from typing import Dict, List, Protocol

from databases import Database
from sqlalchemy import Table, select

from src.services.models import Service


class Repository(Protocol):
    async def add(self, service: Service) -> Dict:
        """Method responsible for including the service in the db"""


class DatabaseRepository:
    def __init__(
        self,
        database: Database,
        units_table: Table,
        items_table: Table,
        services_table: Table,
        list_items_table: Table,
        list_services_table: Table,
    ):
        self.database = database
        self.units_table = units_table
        self.items_table = items_table
        self.services_table = services_table
        self.list_items_table = list_items_table
        self.list_services_table = list_services_table

    async def add_item(self, item_list: List) -> bool:
        key_list = ['quantity', 'items_list', 'service_id']
        query = self.list_items_table.insert().values(
            [dict(zip(key_list, item)) for item in item_list]
        )
        await self.database.execute(query)
        return True


    async def add_service(self, service_list: List) -> bool:
        key_list = ['quantity', 'service_list', 'service_id']
        query = self.list_services_table.insert().values(
            [dict(zip(key_list, service)) for service in service_list]
        )
        await self.database.execute(query)
        return True

    async def add(self, service: Service) -> Dict:
        unit_id = select(self.units_table.c.id).where(
            self.units_table.c.initial == service.unit
        )
        query = self.services_table.insert().values(
            code=service.code,
            description=service.description,
            unit=unit_id.scalar_subquery(),
        )
        last_record_id = await self.database.execute(query)

        if service.inputs:
            await self.add_item(service.inputs)

        if service.compositions:
            await self.add_service(service.compositions)

        return {"id": last_record_id, **asdict(service)}
