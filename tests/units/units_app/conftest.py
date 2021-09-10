import asyncio
from dataclasses import asdict
from typing import Dict

import pytest

from src.units.models import Unit
from src.units.schemas import UnitIn


class FakeRepository:
    def __init__(self, session):
        self.id = 1
        session["units"] = []
        self.session = session["units"]

    async def add(self, unit: Unit) -> Dict:
        await asyncio.sleep(0.3)

        data = {"id": self.id, **asdict(unit)}
        self.session.append({self.id: data})
        self.id += 1
        return data


@pytest.fixture
def unit_model():
    return Unit(name="Metros", initial="m")


@pytest.fixture
def fake_repository(shelve_session):
    return FakeRepository(shelve_session)


@pytest.fixture
def unit_in_schema():
    return UnitIn(
        name="Metros",
        initial="m",
    )
