import pytest

from src.items.models import Item
from src.services.models import Service


@pytest.fixture
def service_model():
    return Service(
        description="Teste de serviço",
        unit="m2",
        inputs=[("id", "name", "unit")],
        compositions=[
            Service(
                description="Teste de composicao",
                unit="unit",
                inputs=[("id", "name", "unit")],
                compositions=[],
            ),
            Item(name="teste", unit="m2"),
        ],
    )
