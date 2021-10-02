import shelve
from decimal import Decimal

import pytest
from faker import Faker

from src.compositions.models import Composition, Feedstock, Service

faker = Faker()


@pytest.fixture
def shelve_session():
    session = shelve.open("test", writeback=True)
    try:
        yield session
    finally:
        session.close()


list_feedstock = [
    Feedstock(feedstock_id=1, quantity=Decimal(10.6)),
    Feedstock(feedstock_id=2, quantity=Decimal(10.6)),
]
list_service = [
    Service(service_id=1, quantity=Decimal(10.8)),
    Service(service_id=2, quantity=Decimal(5.889)),
]


@pytest.fixture
def composition_model():
    return Composition(
        code=faker.lexify(text="?????"),
        description=faker.lexify(text="?????? ?????"),
        unit=1,
        feedstock=list_feedstock,
        services=list_service,
    )
