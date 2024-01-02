import datetime as date
class JournalEntry:
    id: int
    credit: int
    debit: int
    date: date
    description: str
    origin: str
    company: str
    companyId: int
    receipt: int
    
    def __init__(self) -> None:
        pass