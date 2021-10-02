import pytest

from src.compositions.repository import DatabaseRepository
from src.config import database
from src.orm import compositions as compositions_table
from src.orm import compositions_feedstock as compositions_feedstock_table
from src.orm import compositions_services as compositions_services_table


@pytest.fixture
async def startup():
    yield await database.connect()
    await database.disconnect()


@pytest.fixture
def repository():
    return DatabaseRepository(
        database,
        compositions_table,
        compositions_feedstock_table,
        compositions_services_table,
    )
