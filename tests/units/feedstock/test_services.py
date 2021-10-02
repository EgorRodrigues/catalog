import pytest

from src.feedstock.schemas import FeedstockInDB
from src.feedstock.services import FeedstockService


class TestService:
    @pytest.mark.asyncio
    async def test_should_prepare_create(self):
        ...
