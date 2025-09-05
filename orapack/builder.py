from returns.maybe import Maybe
from returns.result import safe
from sqlfluff.dialects.dialect_oracle import (
    CreateFunctionStatementSegment,
    CreateProcedureStatementSegment,
)

from orapack import component, finder

type CreateCallableStatementSegment = (
    CreateFunctionStatementSegment | CreateProcedureStatementSegment
)


def get_callable_name(
    callable_segment: CreateCallableStatementSegment,
) -> Maybe[str]:
    """Return function or procedure name."""
    return (
        finder.find_segment(callable_segment, 'create_function_segment')
        .bind(lambda segment: finder.find_segment(segment, 'word'))
        .bind_optional(lambda segment: segment.raw)
    )


@safe
def get_callable_parameters(
    callable_segment: CreateCallableStatementSegment,
) -> list[component.Parameter]:
    """Return function or procedure parameters."""
    raise NotImplementedError


@safe
def get_function_return_value(
    function_segment: CreateFunctionStatementSegment,
) -> component.PythonType:
    """Return function return value."""
    raise NotImplementedError


@safe
def build_function(
    function_segment: CreateFunctionStatementSegment,
) -> component.Function:
    """Build function structure."""
    raise NotImplementedError


@safe
def build_procedure(
    procedure_segment: CreateProcedureStatementSegment,
) -> component.Function:
    """Build function structure."""
    raise NotImplementedError
