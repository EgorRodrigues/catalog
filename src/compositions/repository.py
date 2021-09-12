from dataclasses import asdict
from typing import Dict, List, Protocol

from databases import Database
from sqlalchemy import Table, select

from src.compositions.models import Composition, Feedstock, Service


class Repository(Protocol):
    async def add(self, composition: Composition) -> Dict:
        """Method responsible for including the service in the db"""


class DatabaseRepository:
    def __init__(
        self,
        database: Database,
        units_table: Table,
        feedstock_table: Table,
        compositions_table: Table,
        compositions_feedstock_table: Table,
        compositions_services_table: Table,
    ):
        self.database = database
        self.units_table = units_table
        self.feedstock_table = feedstock_table
        self.compositions_table = compositions_table
        self.compositions_feedstock_table = compositions_feedstock_table
        self.compositions_services_table = compositions_services_table

    async def add(self, composition: Composition) -> Dict:
        unit_id = select(self.units_table.c.id).where(
            self.units_table.c.initial == composition.unit
        )
        query = self.compositions_table.insert().values(
            code=composition.code,
            description=composition.description,
            unit=unit_id.scalar_subquery(),
        )
        last_composition_id = await self.database.execute(query)

        if composition.feedstock:
            await self._add_feedstock(composition.feedstock, last_composition_id)

        if composition.services:
            await self._add_service(composition.services, last_composition_id)

        return {"id": last_composition_id, **asdict(composition)}

    async def _add_feedstock(
        self, feedstock: List[Feedstock], last_composition_id: int
    ) -> bool:
        values = []
        for feedstock_item in feedstock:
            values.append(
                {
                    "quantity": feedstock_item.quantity,
                    "feedstock_id": feedstock_item.id,
                    "composition_id": last_composition_id,
                }
            )
        query = self.compositions_feedstock_table.insert().values(values)
        await self.database.execute(query)
        return True

    async def _add_service(self, service: List[Service], last_composition_id: int) -> bool:
        values = []
        for service_item in service:
            values.append(
                {
                    "quantity": service_item.quantity,
                    "service_id": service_item.id,
                    "composition_id": last_composition_id,
                }
            )
        query = self.compositions_services_table.insert().values(values)
        await self.database.execute(query)
        return True
