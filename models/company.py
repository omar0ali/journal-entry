from database import Database
import re
from configs.CompanyConfig import CompanyConfig
from util.utility import Utility
class Company:
    def __init__(self, db: Database) -> None:
        self.connection = db.getConnection()
        self.cursor = db.getConnection().cursor()
        self.utility = Utility()
        
    def companyInsert(self, name: str, date: str, desc:str, email:str, phone:str):
        if(self.utility.validate_date(date)==False):
            return
        if(self.utility.validate_phone(phone)==False):
            return
        self.cursor.execute('''
            INSERT INTO company (name, connection_date, description, email, phone) 
            VALUES (?,?,?,?,?)
        ''', (name, date, desc, email, phone))
        self.connection.commit()

    def getCompany(self, id) -> CompanyConfig:
        self.cursor.execute('SELECT * FROM company WHERE id = ?', (id,))
        company_data = self.cursor.fetchone()
        if company_data:
            return CompanyConfig(*company_data)
        else:
            return None
        
    def getCompanies(self):
        # Retrieve all records from the company table
        self.cursor.execute('SELECT * FROM company')
        companies_data = self.cursor.fetchall()
        companies = [CompanyConfig(*company_data) for company_data in companies_data]
        return companies
