from dataclasses import dataclass, field

from src.units.models import Unit


@dataclass
class Item:
    name: str
    unit: Unit = field(init=False)
