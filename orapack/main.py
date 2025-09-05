"""
Demo module for tests.

Example:
```python
parsed = parse_example()
package = find_segment(parsed, 'create_package_statement')
procedures = find_all_segments(package, 'create_procedure_statement')
for procedure in procedures:
    print(get_function_name(procedure))
```

"""

from returns.result import Failure, Result, Success
from sqlfluff.core import Lexer, Parser
from sqlfluff.core.parser import BaseSegment
from sqlfluff.dialects.dialect_oracle import FileSegment

_lexer = Lexer(dialect='oracle')
_parser = Parser(dialect='oracle')


def parse(text: str) -> Result[FileSegment, str]:
    """Parse example PL/SQL and return file Segment."""
    lexed, _errors = _lexer.lex(text)
    parsed = _parser.parse(lexed)
    if parsed is None:
        return Failure('cant parse')
    if not isinstance(parsed, FileSegment):
        return Failure('parse incorrect segment')
    return Success(parsed)


def print_segment_tree(segment: BaseSegment, indent: int = 0) -> None:
    """
    Output segment children tree.

    Useful in development
    """
    print(f'{" " * indent}{segment.type}')  # noqa: RUF100, T201, WPS421, WPS237
    for child in segment.segments:
        print_segment_tree(child, indent + 2)
