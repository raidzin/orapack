from returns.maybe import Maybe
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


def get_callable_parameters(
    callable_segment: CreateCallableStatementSegment,
) -> Maybe[list[component.Parameter]]:
    """Return function or procedure parameters."""
    raise NotImplementedError


def get_function_return_value(
    function_segment: CreateFunctionStatementSegment,
) -> Maybe[component.PythonType]:
    """Return function return value."""
    raise NotImplementedError


def build_function(
    function_segment: CreateFunctionStatementSegment,
) -> Maybe[component.Function]:
    """Build function structure."""
    raise NotImplementedError


def build_procedure(
    procedure_segment: CreateProcedureStatementSegment,
) -> Maybe[component.Function]:
    """Build function structure."""
    raise NotImplementedError
