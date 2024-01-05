from db.database_sql import Database
import util.utility as utility
from configs.CompanyConfig import CompanyConfig
from util.menus import MESSAGES
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
            return MESSAGES.SUCCESS_DATA_INSERTED
        except Exception as e:
            return f"Error: {e}"
        
    def companyUpdate(self, company: CompanyConfig, name=None, date=None, desc=None, email=None, phone=None):
        try:
            # Create a dictionary of non-None values
            update_data = {
                'name': name,
                'connection_date': date,
                'description': desc,
                'email': email,
                'phone': phone,
            }

            # Validate the provided data
            error_message = ""
            for key, value in update_data.items():
                if value is not None:
                    if(key == 'connection_date'):
                        validDate = utility.validate_date(value)
                        if(validDate!=True):
                            errorMessage = errorMessage + " " + validDate
                    if(key == 'name'):
                        validDate = utility.validate_empty(value)
                        if(validDate!=True):
                            errorMessage = errorMessage + " " + validDate
            if error_message != "":
                raise ValueError(error_message)

            query, values = utility.sqlGenerateSetClause(company.id, update_data, "company")

            self.cursor.execute(query, values)
            self.connection.commit()
            return MESSAGES.SUCCESS_DATA_UPDATED
        except Exception as e:
            return f"Error: {e}"


    
    def companyRemove(self, company:CompanyConfig):
        try:
            errorMessage = ""
            validId = utility.validate_empty(str(company.id))
            if validId != True:
                errorMessage = errorMessage + " " + validId
            self.cursor.execute(f"DELETE FROM company WHERE id = ?", (str(company.id)))
            self.connection.commit()
            return MESSAGES.SUCCESS_DATA_UPDATED
        except Exception as e:
            return f"Error: {e}"
        
        
    def getCompany(self, company:CompanyConfig) -> CompanyConfig:
        self.cursor.execute('SELECT * FROM company WHERE id = ?', (str(company.id)))
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
