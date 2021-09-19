from typing import List

import pytest

from src.units.schemas import UnitInDB
from src.units.services import UnitService


class TestUnitService:
    @pytest.mark.asyncio
    async def test_should_prepare_create(
        self,
        shelve_session,
        fake_repository,
        unit_in_schema,
    ):
        unit_in_db = await UnitService(fake_repository).prepare_create(
            unit_in_schema,
        )
        assert len(shelve_session["units"]) == 1
        assert isinstance(unit_in_db, UnitInDB)

    @pytest.mark.asyncio
    async def test_should_prepare_delete(
        self,
        shelve_session,
        fake_repository,
        unit_in_schema,
    ):
        Unit_1 = await UnitService(fake_repository).prepare_create(
            unit_in_schema,
        )
        Unit_2 = await UnitService(fake_repository).prepare_create(
            unit_in_schema,
        )
        Unit_3 = await UnitService(fake_repository).prepare_create(
            unit_in_schema,
        )
        await UnitService(fake_repository).prepare_delete(Unit_3.id)
        assert len(shelve_session["units"]) == 2
        await UnitService(fake_repository).prepare_delete(Unit_2.id)
        assert len(shelve_session["units"]) == 1
        await UnitService(fake_repository).prepare_delete(Unit_1.id)
        assert len(shelve_session["units"]) == 0

    @pytest.mark.asyncio
    async def test_should_prepare_list(
        self,
        fake_repository,
        unit_in_schema,
    ):
        await UnitService(fake_repository).prepare_create(unit_in_schema)
        await UnitService(fake_repository).prepare_create(unit_in_schema)
        await UnitService(fake_repository).prepare_create(unit_in_schema)

        list_unit = await UnitService(fake_repository).prepare_list()

        assert len(list_unit) == 3
        assert isinstance(list_unit, List)
