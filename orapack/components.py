from dataclasses import dataclass


@dataclass
class Argument:
    """Used for function params or return value."""

    name: str
    type: str


@dataclass
class Function:
    """Represent PL/SQL function."""

    name: str
    parameters: list[Argument]
    return_value: str | None


@dataclass
class Procedure:
    """Represent PL/SQL procedure."""

    name: str
    parameters: list[Argument]
