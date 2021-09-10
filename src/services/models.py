from dataclasses import dataclass
from typing import List


@dataclass
class Service:
    description: str
    unit: str
    inputs: List
    compositions: List
