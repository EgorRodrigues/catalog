from pydantic import BaseModel


class UnitBase(BaseModel):
    name: str
    initial: str
