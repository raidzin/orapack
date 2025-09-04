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

from sqlfluff.core import Lexer, Parser
from sqlfluff.core.parser import BaseSegment

_lexer = Lexer(dialect='oracle')
_parser = Parser(dialect='oracle')


def parse(text: str) -> BaseSegment:
    """Parse example PL/SQL and return file Segment."""
    lexed, _errors = _lexer.lex(text)
    parsed = _parser.parse(lexed)
    if parsed is None:
        raise RuntimeError
    return parsed


def print_segment_tree(segment: BaseSegment, indent: int = 0) -> None:
    """Output segment children tree."""
    print(f'{" " * indent}{segment.type}')  # noqa: T201
    for child in segment.segments:
        print_segment_tree(child, indent + 2)
