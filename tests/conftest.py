import pytest
from sqlfluff.core.parser import BaseSegment

from orapack.main import parse

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
END emp_actions;
"""


@pytest.fixture
def example_package() -> str:
    """Example package data."""
    return _EXAMPLE_PACKAGE


@pytest.fixture
def parsed_package(example_package: str) -> BaseSegment:
    """Parsed example package."""
    return parse(example_package)
