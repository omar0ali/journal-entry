import sqlite3
from rich.console import Console
from rich.theme import Theme
import glob
class Database:
    console = Console(theme=Theme({
        "info": "dim cyan",
        "warning": "magenta",
        "danger": "bold red"
    }))
    def __init__(self, name:str = "JournalEntry") -> None:
        self.connection = sqlite3.connect(f"{name}.db")
        self.cursor = self.connection.cursor()
        ## CREATE TABELS ##
        # CREATE COMPANY TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS company (
                id INTEGER PRIMARY KEY,
                name TEXT,
                connection_date DATE,
                description TEXT,
                email TEXT,
                phone TEXT CHECK (length(phone) <= 15)
            )                 
        """)
        
        
        
        self.cursor.connection.commit()
        self.console.print("Tables Created.\nDatabase Connected.", style="magenta")

    
    def getConnection(self):
        return self.connection
    
    def getCursor(self):
        return self.cursor()
    
    def disconnectDatabase(self):
        self.connection.close()
    
    def checkDatabaseFile():
        matching_files = glob.glob("./*.db")
        if matching_files:
            print("Database file's found:")
            for file_path in matching_files:
                print(file_path)
        else:
            print("No databases found.")