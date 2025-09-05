import pytest
from returns.result import Success
from sqlfluff.dialects.dialect_oracle import FileSegment

from orapack import main

_EXAMPLE_PACKAGE = """
CREATE OR REPLACE PACKAGE emp_actions AS
TYPE emprectyp IS RECORD (emp_id INT, salary REAL);
CURSOR desc_salary RETURN EMPRECTYP;
PROCEDURE hire_employee(
    ename VARCHAR2,
    job VARCHAR2,
    mgr NUMBER,
    sal NUMBER,
    comm NUMBER,
    deptno NUMBER
);
PROCEDURE fire_employee(emp_id NUMBER);
FUNCTION find_employee(ename VARCHAR2) RETURN NUMBER;
END emp_actions;
"""


@pytest.fixture
def example_package() -> str:
    """Example package data."""
    return _EXAMPLE_PACKAGE


@pytest.fixture
def parsed_package(example_package: str) -> FileSegment:
    """Parsed example package."""
    match main.parse(example_package):
        case Success(file_segment):
            return file_segment
        case _:
            raise RuntimeError
