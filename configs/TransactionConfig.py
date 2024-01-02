import datetime as date
from .Config import Config
class TranscationConfig(Config):
    company_id:int
    account:str
    description:str
    source:str
    date:date
    receipt_num:str
    debit:float
    credit:float
    def __init__(self, id: int, company_id:int, account:str, description:str, source:str, date:date, receipt_num:str, debit: float, credit:float) -> None:
        super().__init__(id)
        self.company_id = company_id
        self.account = account
        self.description = description
        self.source = source
        self.receipt_num = receipt_num
        self.debit = debit
        self.credit = credit
        self.date = date
    
    def getAsList(self) -> list:
        return [str(self.id), self.company_id, self.account, self.description, self.source, self.date, self.receipt_num, self.debit, self.credit]

    def __str__(self) -> str:
        return " | ".join(self.getAsList())