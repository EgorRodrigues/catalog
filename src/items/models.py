from dataclasses import dataclass, field


@dataclass
class Unit:
    name: str
    initial: str


@dataclass
class Item:
    name: str
    unit: Unit = field(init=False)
