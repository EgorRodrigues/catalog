from typing import Dict, List

import pytest

from src.compositions.models import Composition


class FakeRepository:
    async def add(self, composition: Composition) -> Dict:
        """Method"""

    async def get_all(self) -> List[Composition]:
        """Method r"""

    async def get_item(self, pk: int) -> Dict:
        """Method"""

    async def update(self, composition: Composition) -> Dict:
        """Method"""


@pytest.fixture
def fake_repository():
    return FakeRepository()


# database
# compositions_table
# compositions_feedstock_table
# compositions_services_table
