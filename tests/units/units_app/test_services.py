import pytest

from src.units.schemas import UnitInDB
from src.units.services import UnitService


class TestService:
    @pytest.mark.asyncio
    async def test_should_prepare_create(
        self,
        shelve_session,
        fake_repository,
        unit_in_schema,
    ):
        unit_in_db = await UnitService(fake_repository).prepare_create(unit_in_schema)
        assert len(shelve_session["units"]) == 1
        assert isinstance(unit_in_db, UnitInDB)
