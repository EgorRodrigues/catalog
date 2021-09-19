import pytest

from src.compositions.models import Composition


@pytest.fixture
def composition_model():
    return Composition(
        code="A02",
        description="Teste de serviço",
        unit="m2",
        feedstock=[],
        services=[],
    )
