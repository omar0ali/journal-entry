import datetime as date
class CompanyConfig:
    id: int
    name: str
    connection_date: date
    description:str
    email: str
    phone: str
    def __init__(self, id:int, name:str, connection_date:date, description:str, email:str, phone:str):
        self.id = id
        self.name = name
        self.connection_date = connection_date
        self.description = description
        self.email = email
        self.phone = phone
        
    def getAsList(self):
        return [self.id, self.name, self.connection_date, self.description, self.email, self.phone]
        