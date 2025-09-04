from returns.maybe import Maybe
from sqlfluff.dialects.dialect_oracle import CreateFunctionStatementSegment

from orapack import components, finder


def get_function_name(
    function_segment: CreateFunctionStatementSegment,
) -> Maybe[str]:
    """Return function or procedure name."""
    return (
        finder.find_segment(function_segment, 'create_function_segment')
        .bind(lambda segment: finder.find_segment(segment, 'word'))
        .bind_optional(lambda segment: segment.raw)
    )


def build_function(
    segment: CreateFunctionStatementSegment,
) -> components.Function:
    """Build function structure."""
    raise NotImplementedError
