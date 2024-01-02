from datetime import datetime
import re
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