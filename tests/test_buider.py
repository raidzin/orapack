import pytest
from returns.maybe import Some
from returns.result import Failure, Success
from sqlfluff.dialects.dialect_oracle import (
    CreateFunctionStatementSegment,
    CreateProcedureStatementSegment,
    FileSegment,
)

from orapack import builder, component, finder


@pytest.fixture
def function_segment(
    parsed_package: FileSegment,
) -> CreateFunctionStatementSegment:
    match finder.find_segment(parsed_package, 'create_function_statement'):
        case Some(segment) if isinstance(
            segment,
            CreateFunctionStatementSegment,
        ):
            return segment
        case _:
            raise RuntimeError


@pytest.fixture
def procedure_segment(
    parsed_package: FileSegment,
) -> CreateProcedureStatementSegment:
    match finder.find_segment(parsed_package, 'create_procedure_statement'):
        case Some(segment) if isinstance(
            segment,
            CreateProcedureStatementSegment,
        ):
            return segment
        case _:
            raise RuntimeError


@pytest.mark.xfail(raises=NotImplementedError)
def test_function_builder(
    function_segment: CreateFunctionStatementSegment,
) -> None:
    match builder.build_function(function_segment):
        case Success(function) if isinstance(function, component.Function):
            pass
        case Success(other):
            pytest.fail(f'function_builder build error, get: {other}')
        case Failure(error):
            raise error
        case _:
            pytest.fail('incorrect build')


@pytest.mark.xfail(raises=NotImplementedError)
def test_procedure_builder(
    procedure_segment: CreateProcedureStatementSegment,
) -> None:
    match builder.build_procedure(procedure_segment):
        case Success(procedure) if isinstance(procedure, component.Function):
            pass
        case Success(other):
            pytest.fail(f'function_builder build error, get: {other}')
        case Failure(error):
            raise error
        case _:
            pytest.fail('incorrect build')
