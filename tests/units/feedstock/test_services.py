import pytest

from src.feedstock.schemas import FeedstockInDB
from src.feedstock.services import FeedstockService


class TestService:
    @pytest.mark.asyncio
    async def test_should_prepare_create(
        self,
        shelve_session,
        fake_repository,
        item_in_schema,
    ):
        unit_in_db = await FeedstockService(fake_repository).prepare_create(
            item_in_schema
        )
        assert len(shelve_session["feedstock"]) == 1
        assert isinstance(unit_in_db, FeedstockInDB)
