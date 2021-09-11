from dataclasses import dataclass
from typing import Optional


@dataclass
class Service:
    code: str
    description: str
    unit: str
    inputs: Optional = None
    compositions: Optional = None
