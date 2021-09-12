import asyncio
from dataclasses import asdict
from typing import Dict

import pytest

from src.feedstocks.models import Item
from src.feedstocks.schemas import ItemIn


class FakeRepository:
    def __init__(self, session):
        self.id = 1
        session["feedstock"] = []
        self.session = session["feedstock"]

    async def add(self, item: Item) -> Dict:
        await asyncio.sleep(0.3)

        data = {"id": self.id, **asdict(item)}
        self.session.append({self.id: data})
        self.id += 1
        return data


@pytest.fixture
def item_model():
    return Item(
        name="Pedra calcarea extraida da margem de rio",
        unit="m3",
    )


@pytest.fixture
def fake_repository(shelve_session):
    return FakeRepository(shelve_session)


@pytest.fixture
def item_in_schema():
    return ItemIn(
        name="Pedra calcarea extraida da margem de rio",
        unit="m3",
    )
