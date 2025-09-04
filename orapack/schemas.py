from dataclasses import dataclass


@dataclass
class Argument:
    name: str
    type: str


@dataclass
class Function:
    name: str
