import pytest

from src.items.models import Item
from src.services.models import Service


@pytest.fixture
def service_model():
    return Service(
        code="A02",
        description="Teste de serviço",
        unit="m2",
        inputs=[("id", "name", "unit")],
        compositions=[
            Service(
                code="A01",
                description="Teste de composicao",
                unit="unit",
                inputs=[("id", "name", "unit")],
                compositions=[],
            ),
            Item(name="teste", unit="m2"),
        ],
    )
