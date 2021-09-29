import asyncio
from dataclasses import asdict
from typing import Dict, List

import pytest

from src.feedstock.models import Feedstock
from src.feedstock.schemas import FeedstockIn


class FakeRepository:
    def __init__(self, session):
        self.id = 1
        session["feedstock"] = []
        self.session = session["feedstock"]

    async def add(self, feedstock: Feedstock) -> Dict:
        await asyncio.sleep(0.3)

        data = {"id": self.id, **asdict(feedstock)}
        self.session.append({self.id: data})
        self.id += 1
        return data

    async def delete(self, pk: int) -> bool:
        ...

    async def get_all(self) -> List:
        ...

    async def get_item(self, pk) -> Dict:
        ...


@pytest.fixture
def feedstock_model():
    return Feedstock(
        description="Lápis",
        unit="un",
    )


@pytest.fixture
def fake_repository(shelve_session):
    return FakeRepository(shelve_session)


@pytest.fixture
def item_in_schema():
    return FeedstockIn(
        description="Lápis",
        unit="un",
    )
