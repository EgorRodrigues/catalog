from src.services.repository import Repository
from src.services.schemas import ServiceIn, ServiceInDB


class ServiceService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def prepare_create(self, service: ServiceIn) -> ServiceInDB:
        result = await self.repository.add(service.to_model())
        return ServiceInDB.from_dict(result)
