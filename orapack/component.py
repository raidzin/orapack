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
class Callable:
    """Base callable class for functions & procedures."""

    name: str
    parameters: list[Parameter]  # noqa: WPS110


@dataclass
class Function(Callable):
    """Represent PL/SQL function."""

    return_value: str | None


@dataclass
class Procedure(Callable):
    """Represent PL/SQL procedure."""
