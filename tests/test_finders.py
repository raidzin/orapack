import pytest
from returns.maybe import Maybe, Some
from sqlfluff.core.parser import BaseSegment
from sqlfluff.dialects.dialect_oracle import (
    CreateFunctionStatementSegment,
    CreatePackageStatementSegment,
    CreateProcedureStatementSegment,
)

from orapack.finder import find_all_segments, find_segment

PROCEDURE_SEGMENTS_COUNT = 2
CALLABLE_SEGMENTS_COUNT = 3


def test_find_segment(parsed_package: BaseSegment) -> None:
    segment = find_segment(parsed_package, 'create_package_statement')

    match segment:
        case Some(value) if isinstance(value, CreatePackageStatementSegment):
            pass
        case Some(value):
            pytest.fail(f'found incorrect segment {value}')
        case _:
            pytest.fail('incorrect find_segment')


def test_many_find_segment(parsed_package: BaseSegment) -> None:
    segment = find_segment(
        parsed_package,
        ['create_function_statement', 'create_procedure_statement'],
    )

    match segment:
        case Some(value) if isinstance(value, CreateFunctionStatementSegment):
            pass
        case Some(value) if isinstance(value, CreateProcedureStatementSegment):
            pass
        case Some(value):
            pytest.fail(f'found incorrect segment {value}')
        case _:
            pytest.fail('incorrect find_segment')


def test_find_segment_empty(parsed_package: BaseSegment) -> None:
    segment = find_segment(parsed_package, 'non_existent_segment')

    match segment:
        case Maybe.empty:
            pass
        case Some(value):
            pytest.fail(f'found incorrect segment {value}')
        case _:
            pytest.fail('incorrect find_segment')


def test_find_all_segment(parsed_package: BaseSegment) -> None:
    segments = find_all_segments(parsed_package, 'create_procedure_statement')

    assert len(segments) == PROCEDURE_SEGMENTS_COUNT

    for segment in segments:
        assert isinstance(segment, CreateProcedureStatementSegment)


def test_many_find_all_segment(parsed_package: BaseSegment) -> None:
    segments = find_all_segments(
        parsed_package,
        ['create_procedure_statement', 'create_function_statement'],
    )

    assert len(segments) == CALLABLE_SEGMENTS_COUNT

    for segment in segments:
        assert any(
            (
                isinstance(segment, CreateProcedureStatementSegment),
                isinstance(segment, CreateFunctionStatementSegment),
            )
        )


def test_test_find_all_segment_error(parsed_package: BaseSegment) -> None:
    segments = find_all_segments(parsed_package, 'non_existent_segment')

    assert len(segments) == 0
