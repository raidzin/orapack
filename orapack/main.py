"""Demo module for tests.

Example:

```python
parsed = parse_example()
package = find_segment(parsed, 'create_package_statement')
procedures = find_all_segments(package, 'create_procedure_statement')
for procedure in procedures:
    print(get_function_name(procedure))
```

"""

from pathlib import Path

from sqlfluff.core import Lexer, Parser
from sqlfluff.core.parser import BaseSegment

_SQL_FILE = Path() / 'examples' / 'test.decl.sql'
_SQL = _SQL_FILE.read_text('utf-8')


_lexer = Lexer(dialect='oracle')
_parser = Parser(dialect='oracle')


class SegmentNotFoundError(Exception):
    """Cant found segment error."""


def parse_example() -> BaseSegment:
    """Parse example PL/SQL and return file Segment."""
    lexed, _errors = _lexer.lex(str(_SQL))
    parsed = _parser.parse(lexed)
    if parsed is None:
        raise RuntimeError
    return parsed


def find_segment(
    start_segment: BaseSegment,
    segment_type: str,
) -> BaseSegment:
    """Find first segment by type in segment tree."""
    to_check = [start_segment]
    while to_check:
        segment = to_check.pop()
        if segment.type == segment_type:
            return segment
        to_check.extend(segment.segments)
    raise SegmentNotFoundError


def find_all_segments(
    start_segment: BaseSegment,
    segment_type: str,
) -> list[BaseSegment]:
    """Find all segments by type in segment tree."""
    to_check = [start_segment]
    found = []
    while to_check:
        segment = to_check.pop()
        if segment.type == segment_type:
            found.append(segment)
        to_check.extend(segment.segments)
    return found


def get_function_name(segment: BaseSegment) -> str:
    """Return function or procedure name."""
    return find_segment(
        find_segment(segment, 'function_name'),
        'word',
    ).raw
