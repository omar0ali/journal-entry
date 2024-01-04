from datetime import datetime
import re
from typing import Any
from rich.console import Console

def validate_date(date_str) -> bool | str:
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError as e:
        return f"Validation Failed: {e}."
        
def validate_phone(phone_str) -> bool | str:
    validate = re.match(r'^\d{10}$', phone_str)
    if(validate == None):
        return "Validation phone number failed."
    return True

def validate_empty(text) -> bool | str:
    if(text==""):
        return "Validation text is empty."
    return True



def sqlGenerateSetClause(id:int, data: dict[str, Any | None], table:str):
    # Generate the SET clause for the SQL query
    set_clause = ', '.join(f'{key} = ?' for key, value in data.items() if value is not None)

    # Execute the update query
    query = f'''
        UPDATE {table}
        SET {set_clause}
        WHERE id = ?
    '''
    values = [value for value in data.values() if value is not None] + [id]
    return query, values