from database import Database
import util.utility as utility
from configs.CompanyConfig import CompanyConfig
class CompanyModel:
    def __init__(self, db: Database) -> None:
        self.connection = db.getConnection()
        self.cursor = db.getConnection().cursor()
        
    def companyInsert(self, name: str, date: str, desc:str, email:str, phone:str):
        try:
            errorMessage = ""
            
            validName = utility.validate_empty(name)
            if(validName!=True):
                errorMessage = errorMessage + " " + validName
            
            validDate = utility.validate_date(date)
            if(validDate!=True):
                errorMessage = errorMessage + " " + validDate
                
            if(errorMessage!=""):
                raise ValueError(errorMessage)
            
            self.cursor.execute('''
                INSERT INTO company (name, connection_date, description, email, phone) 
                VALUES (?,?,?,?,?)
            ''', (name, date, desc, email, phone))
            self.connection.commit()
            return "Data inserted successfully!"
        except Exception as e:
            return f"Error: {e}"
        
    def companyUpdate(self, company_id: int, name: str, date: str, desc: str, email: str, phone: str):
        try:
            errorMessage = ""

            validName = utility.validate_empty(name)
            if validName != True:
                errorMessage = errorMessage + " " + validName

            validDate = utility.validate_date(date)
            if validDate != True:
                errorMessage = errorMessage + " " + validDate

            if errorMessage != "":
                raise ValueError(errorMessage)

            self.cursor.execute('''
                UPDATE company
                SET name = ?, connection_date = ?, description = ?, email = ?, phone = ?
                WHERE id = ?
            ''', (name, date, desc, email, phone, company_id))

            self.connection.commit()
            return "Data updated successfully!"
        except Exception as e:
            return f"Error: {e}"

    def getCompany(self, id) -> CompanyConfig:
        self.cursor.execute('SELECT * FROM company WHERE id = ?', (id,))
        company_data = self.cursor.fetchone()
        if company_data:
            return CompanyConfig(*company_data)
        else:
            return None
        
    def getCompanies(self):
        self.cursor.execute('SELECT * FROM company')
        companies_data = self.cursor.fetchall()
        companies = [CompanyConfig(*company_data) for company_data in companies_data]
        return companies
