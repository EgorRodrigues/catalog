import pytest

from src.compositions.models import Service
from src.feedstocks.models import Item


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
