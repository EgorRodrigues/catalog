from typing import Dict

import pytest

from src.compositions.models import Feedstock, Service


class TestRepositoryIntegration:
    @pytest.mark.asyncio
    async def test_database_repository_add(
        self,
        composition_model,
        repository,
        startup,
    ):
        startup
        assert isinstance(composition_model.feedstock, list)
        assert isinstance(composition_model.feedstock[0], Feedstock)
        assert isinstance(composition_model.services, list)
        assert isinstance(composition_model.services[0], Service)
        add = await repository.add(composition_model)
        assert isinstance(add, Dict)


# @pytest.mark.asyncio
# async def test_database_repository_get_item(self, composition_model, repository):
#     add = await repository.add(composition_model)
#     get = await repository.get_item(add["id"])
#     assert get["description"] == add["description"]
