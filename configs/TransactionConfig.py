import datetime as date_
from .Config import Config
class TransactionConfig(Config):
    company_id:int
    company_name:str
    account:str
    description:str
    source:str
    date: date_
    receipt_num:str
    debit:float = 0
    credit:float = 0
    def __init__(self, id: int, company_id:int, company_name, account:str, description:str, source:str, date:date_, receipt_num:str, debit: float, credit:float) -> None:
        super().__init__(id)
        self.company_id = company_id
        self.company_name = company_name
        self.account = account
        self.description = description
        self.source = source
        self.receipt_num = receipt_num
        self.debit = debit
        self.credit = credit
        self.date = date
    
    def getAsList(self) -> list:
        return [str(self.id), str(self.company_id), self.company_name, self.account, self.description, self.source, self.date, self.receipt_num, str(self.debit), str(self.credit)]

    def __str__(self) -> str:
        return " | ".join(self.getAsList())
        

class TransactionConfigBalance(TransactionConfig):
    balance:float = 0
    def __init__(self, id: int, company_id:int, company_name:str, account:str, description:str, source:str, date:date_, receipt_num:str, debit: float, credit:float) -> None:
        super().__init__(id, company_id,  company_name, account, description, source, date, receipt_num, debit, credit)
    
    def getAsList(self) -> list:
        return [str(self.id), str(self.company_id), self.company_name, self.account, self.description, self.source, self.date, self.receipt_num, str(self.debit), str(self.credit), str(self.balance)]

    def __str__(self) -> str:
        return " | ".join(self.getAsList())