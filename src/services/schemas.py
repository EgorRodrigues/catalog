from typing import List

from pydantic import BaseModel

from src.services.models import Service as ServiceModel


class ServiceBase(BaseModel):
    code: str
    description: str
    unit: str


class ServiceIn(ServiceBase):
    inputs: List
    compositions: List

    def to_model(self) -> ServiceModel:
        return ServiceModel(
            code=self.code,
            description=self.description,
            unit=self.unit,
            inputs=self.inputs,
            compositions=self.compositions,
        )


class ServiceInDB(ServiceBase):
    id: int

    @staticmethod
    def from_dict(obj) -> "ServiceInDB":
        return ServiceInDB(
            id=obj["id"],
            code=obj["code"],
            description=obj["description"],
            unit=obj["unit"],
            inputs=obj["inputs"],
            compositions=obj["compositions"],
        )
