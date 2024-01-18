import datetime as date
from .Config import Config
class CompanyConfig(Config):
    name: str
    connection_date: date
    description:str
    email: str
    phone: str
    def __init__(self, id:int, name:str, connection_date:date, description:str, email:str, phone:str):
        super().__init__(id)
        self.name = name
        self.connection_date = connection_date
        self.description = description
        self.email = email
        self.phone = phone
        
    def getAsList(self):
        return [str(self.id), self.name, self.connection_date, self.description, self.email, self.phone]
    
    def __str__(self) -> str:
        return f"{self.id} : {self.name} - Starting Date: {self.connection_date}"