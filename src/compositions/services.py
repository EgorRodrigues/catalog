from typing import Dict, List

from src.compositions.models import Composition
from src.compositions.repository import Repository
from src.compositions.schemas import CompositionIn, CompositionInDB
from src.feedstock.entrypoints.clients import (
    AsyncClientService as FeedstockClient,
)  # noqa


class CompositionService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(
        self, composition: CompositionIn
    ) -> CompositionInDB:  # noqa
        result = await self.repository.add(composition.to_model)
        return CompositionInDB.from_dict(result)

    async def prepare_list(self) -> List[Composition]:
        result = await self.repository.get_all()
        return result

    async def prepare_composition(self, pk: int) -> Dict:
        result = await self.repository.get_item(pk)
        if result["feedstock"]:
            for feedstock in result["feedstock"]:
                get_feedstock = await FeedstockClient().get_item(
                    feedstock["feedstock_id"]
                )
                feedstock["description"] = get_feedstock.description
                feedstock["unit"] = get_feedstock.unit

        if result["services"]:
            for service in result["services"]:
                get_service = await self.repository.get_item(
                    service["service_id"]
                )  # noqa
                service["code"] = get_service["code"]
                service["description"] = get_service["description"]
                service["unit"] = get_service["unit"]

        return result
