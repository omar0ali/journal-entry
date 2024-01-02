from database import Database
import util.utility as utility
from configs.TransactionConfig import TranscationConfig
from configs.CompanyConfig import CompanyConfig
class TransactionModel:
    def __init__(self, db:Database) -> None:
        self.connection = db.getConnection()
        self.cursor = db.getConnection().cursor()
        
    def transactionInsert(self, company:CompanyConfig, account:str, description:str, source:str, date:str, receipt_num:str, debit: float, credit:float ):
        try:
            errorMessage = ""
                
            validName = utility.validate_empty(str(company.id))
            if(validName!=True):
                errorMessage = errorMessage + " " + validName
            
            validDate = utility.validate_date(date)
            if(validDate!=True):
                errorMessage = errorMessage + " " + validDate
                
            if(errorMessage!=""):
                raise ValueError(errorMessage)
            self.cursor.execute('''
                INSERT INTO transactions (company_id, account, description, source, date, receipt_num, debit, credit)
                VALUES (?, ?, ?, ?, ? ,?, ?, ?)
                ''', (str(company.id), account, description, source, date , receipt_num, debit, credit))
            self.connection.commit()
            return "Data inserted successfully!"
        except Exception as e:
            return f"Error: {e}"
        
    
    def transactionUpdate(self, journal: TranscationConfig, company_id=None, account=None, description=None, source=None, date=None, receipt_num=None, debit=None, credit=None):
        try:
            # Create a dictionary of non-None values
            update_data = {
                'company_id': company_id,
                'account': account,
                'date': date,
                'description': description,
                'source': source,
                'receipt_num': receipt_num,
                'debit': debit,
                'credit': credit,
            }

            # Validate the provided data
            error_message = ""
            for key, value in update_data.items():
                if value is not None:
                    if(key == 'date'):
                        validDate = utility.validate_date(value)
                        if(validDate!=True):
                            errorMessage = errorMessage + " " + validDate
                    if(key == 'company_id'):
                        validDate = utility.validate_empty(value)
                        if(validDate!=True):
                            errorMessage = errorMessage + " " + validDate
                    if(key == 'account'):
                        validDate = utility.validate_empty(value)
                        if(validDate!=True):
                            errorMessage = errorMessage + " " + validDate
            if error_message != "":
                raise ValueError(error_message)

            query, values = utility.sqlGenerateSetClause(journal.id, update_data)

            self.cursor.execute(query, values)
            self.connection.commit()
            return "Data updated successfully!"
        except Exception as e:
            return f"Error: {e}"
        
    def getJournal(self, company:TranscationConfig) -> TranscationConfig:
        self.cursor.execute('SELECT * FROM transactions WHERE id = ?', (str(company.id)))
        transaction_data = self.cursor.fetchone()
        if transaction_data:
            return TranscationConfig(*transaction_data)
        else:
            return None
        
    def getJournals(self):
        self.cursor.execute('SELECT * FROM transactions')
        transactions_data = self.cursor.fetchall()
        transactions_data = [TranscationConfig(*transaction_data) for transaction_data in transactions_data]
        return transactions_data
