from dataclasses import asdict
from typing import Dict, List, Protocol

from databases import Database
from sqlalchemy import Table, select

from src.compositions.models import Composition, Feedstock, Service


class Repository(Protocol):
    async def add(self, composition: Composition) -> Dict:
        """Method responsible for including the service in the db"""

    async def get_all(self) -> List[Composition]:
        """Method responsible for get all compositions in the db"""

    async def get_item(self, pk: int) -> Composition:
        """Method"""


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

    async def _add_service(
        self, service: List[Service], last_composition_id: int
    ) -> bool:
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

    async def get_all(self) -> List:
        query = select(
            [
                self.compositions_table.c.code,
                self.compositions_table.c.description,
                self.units_table.c.initial.label("unit"),
            ]
        ).select_from(self.compositions_table.join(self.units_table))
        rows = await self.database.fetch_all(query=query)
        result = [dict(row) for row in rows]
        return result

    async def get_item(self, pk: int) -> Composition:

        composition = (
            select(
                self.compositions_table.c.code,
                self.compositions_table.c.description,
                self.units_table.c.initial,
            )
            .select_from(self.compositions_table.join(self.units_table))
            .where(self.compositions_table.c.id == pk)
        )
        print("Compoisição >->", composition)

        feedstock = (
            select(
                self.compositions_feedstock_table.c.feedstock_id,
                self.compositions_feedstock_table.c.quantity,
                self.feedstock_table.c.name,
                # self.units_table.c.initial,
            )
            .select_from(
                self.compositions_table.join(
                    self.compositions_feedstock_table,
                    self.compositions_table.c.id
                    == self.compositions_feedstock_table.c.composition_id,
                )
            )
            .where(self.compositions_feedstock_table.c.composition_id == pk)
        )
        print("Insumos >->", feedstock)

        services = (
            select(
                self.compositions_table.c.id,
                self.compositions_services_table.c.composition_id,
                self.compositions_services_table.c.quantity,
                self.compositions_table.c.description,
                # self.units_table.c.initial,
            )
            .select_from(
                self.compositions_table.join(
                    self.compositions_services_table,
                    self.compositions_table.c.id
                    == self.compositions_services_table.c.composition_id,
                )
            )
            .where(self.compositions_services_table.c.composition_id == pk)
        )
        print("Serviços >->", services)

        composition = await self.database.fetch_all(query=composition)
        feedstock = await self.database.fetch_all(query=feedstock)
        services = await self.database.fetch_all(query=services)

        print("Compoisição >->", composition)
        print("Insumos >->", feedstock)
        print("Serviços >->", services)

        # return result
