import pytest
from returns.primitives.exceptions import UnwrapFailedError
from sqlfluff.core.parser import BaseSegment
from sqlfluff.dialects.dialect_oracle import (
    CreatePackageStatementSegment,
    CreateProcedureStatementSegment,
)

from orapack.finder import find_all_segments, find_segment

_PROCEDURE_SEGMENTS_COUNT = 2


def test_find_segment(parsed_package: BaseSegment) -> None:
    segment = find_segment(parsed_package, 'create_package_statement').unwrap()

    assert isinstance(segment, CreatePackageStatementSegment)


def test_find_segment_error(parsed_package: BaseSegment) -> None:
    with pytest.raises(UnwrapFailedError):
        find_segment(parsed_package, 'non_existent_segment').unwrap()


def test_find_all_segment(parsed_package: BaseSegment) -> None:
    segments = find_all_segments(parsed_package, 'create_procedure_statement')

    assert len(segments) == _PROCEDURE_SEGMENTS_COUNT

    for segment in segments:
        assert isinstance(segment, CreateProcedureStatementSegment)


def test_test_find_all_segment_error(parsed_package: BaseSegment) -> None:
    segments = find_all_segments(parsed_package, 'non_existent_segment')

    assert len(segments) == 0
