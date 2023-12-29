from datetime import datetime
import re
from rich.console import Console
class Utility:
    def __init__(self) -> None:
        self.console = Console()
    def validate_date(self, date_str)->bool:
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError as e:
            self.console.print("Validation Failed: "+e, style="danger")
            return False
        
    def validate_phone(self, phone_str) -> bool:
        validate = re.match(r'^\d{10}$', phone_str) is not None
        if(validate==None):
            self.console.print("Validation phone number failed.", style="danger")
            return False
        return 