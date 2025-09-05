from datetime import date, datetime

ORACLE_TO_PYTHON_TYPES = {
    "VARCHAR2": str,
    'NVARCHAR2': str,
    "CHAR": str,
    "CLOB": str,
    "NUMBER": float,
    "INTEGER": int,
    "BINARY_INTEGER": int,
    'PLS_INTEGER': int,
    "BLOB": bytes,
    "ROW": bytes,
    "LONG ROW": bytes,
    "BOOLEAN": bool,
    "DATE": date,
    "TIMESTEP": datetime
}

def get_ora_type(ora_type: str) -> str:
    return ora_type.strip().upper().split("(")[0]

def mapping(ora_type: str):
    return ORACLE_TO_PYTHON_TYPES.get(get_ora_type(ora_type), object)

examples = [
    'VARCHAR2(100)',
    'NUMBER(10,2)',
    'DATE',
    'BLOB',
    'BOOLEAN'
]

for t in examples:
    print(f"{t} -> {mapping(t)}")