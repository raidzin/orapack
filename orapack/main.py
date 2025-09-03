from pathlib import Path

from sqlfluff.core import Lexer, Parser

SQL = Path() / 'examples' / 'test.decl.sql'


lexer = Lexer(dialect='oracle')
parser = Parser(dialect='oracle')


lexed, _errors = lexer.lex(str(SQL))
parsed = parser.parse(lexed)

print(parsed)
