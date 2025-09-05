from dataclasses import dataclass
from enum import StrEnum


class PythonType(StrEnum):
    """Supported python types."""

    bool = 'bool'
    int = 'int'
    float = 'float'
    str = 'str'
    datetime = 'datetime.datetime'


@dataclass
class Parameter:
    """Used for function params or return value."""

    name: str
    type: PythonType


@dataclass
class Function:
    """Represent PL/SQL function."""

    name: str
    parameters: list[Parameter]
    return_value: str | None


@dataclass
class Procedure:
    """Represent PL/SQL procedure."""

    name: str
    parameters: list[Parameter]
