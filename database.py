import sqlite3
import datetime
import re
from rich.console import Console
from rich.theme import Theme
class Database:
    console = Console(theme=Theme({
        "info": "dim cyan",
        "warning": "magenta",
        "danger": "bold red"
    }))
    connection = sqlite3.connect('kashfHesab.db')
    cursor = connection.cursor()
    def __init__(self) -> None:
        
        ## CREATE TABELS ##
        # CREATE COMPANY TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS company (
                id INTEGER PRIMARY KEY,
                name TEXT,
                connectionDate DATE,
                description TEXT,
                email TEXT,
                phone TEXT CHECK (length(phone) <= 15)                  
        """)
        
        
        
        
        
        self.cursor.connection.commit()

        
        
    def insertCompany(self, name: str, date: str, desc:str, email:str, phone:str):
        if(self.validate_date(date)==False):
            return
        if(self.validate_phone(phone)==False):
            return
        self.cursor.execute('''
            INSERT INTO company (name, connectionDate, description, email, phone) 
            VALUES (?,?,?,?,?)
        ''', (name, date, desc, email, phone))
        self.connection.commit()
    
    
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
        
    def disconnect(self):
        self.connection.close()