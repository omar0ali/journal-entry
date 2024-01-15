from db.database_sql import Database
import util.utility as utility
from configs.TransactionConfig import TransactionConfig, TransactionConfigBalance
from configs.CompanyConfig import CompanyConfig
from util.menus import MESSAGES
class TransactionModel:
    def __init__(self, db:Database) -> None:
        self.connection = db.getConnection()
        self.cursor = db.getConnection().cursor()
        
    def transactionInsert(self, company:CompanyConfig, company_name:str, account:str, description:str, source:str, date:str, receipt_num:str, debit: float, credit:float ):
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
                INSERT INTO transactions (company_id, company_name, account, description, source, date, receipt_num, debit, credit)
                VALUES (?, ?, ?, ?, ?, ? ,?, ?, ?)
                ''', (str(company.id), company_name, account, description, source, date , receipt_num, str(debit), str(credit)))
            self.connection.commit()
            return MESSAGES.SUCCESS_DATA_INSERTED
        except Exception as e:
            return f"Error: {e}"
        
    
    def transactionUpdate(self, journal: TransactionConfig, company_id=None, company_name=None, account=None, description=None, source=None, date=None, receipt_num=None, debit=None, credit=None):
        try:
            # Create a dictionary of non-None values
            update_data = {
                'company_id': company_id,
                'company_name': company_name,
                'account': account,
                'description': description,
                'source': source,
                'date': date,
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
                        validID = utility.validate_empty(value)
                        if(validID!=True):
                            errorMessage = errorMessage + " " + validID
                    if(key == 'account'):
                        validAccount = utility.validate_empty(value)
                        if(validAccount!=True):
                            errorMessage = errorMessage + " " + validAccount
                    if(key == 'company_name'):
                        company = utility.validate_empty(value)
                        if(company!=True):
                            errorMessage = errorMessage + " " + company
            if error_message != "":
                raise ValueError(error_message)
            
            query, values = utility.sqlGenerateSetClause(journal.id, update_data,"transactions")

            self.cursor.execute(query, values)
            self.connection.commit()
            return MESSAGES.SUCCESS_DATA_UPDATED
        except Exception as e:
            return f"Error: {e}"


    def getJournal(self, journal:TransactionConfig) -> TransactionConfig:
        self.cursor.execute('SELECT * FROM transactions WHERE id = ?', (str(journal.id)))
        transaction_data = self.cursor.fetchone()
        if transaction_data:
            return TransactionConfig(*transaction_data)
        else:
            return None
        
    # Either we return all transactions, or if CompanyConfig passed as an argument, 
    #   we return transactions connected to that company.
    def getJournals(self, company: CompanyConfig = None):
        if(company):
            self.cursor.execute('SELECT * FROM transactions where company_id = ?', (str(company.id)))
        else:
            self.cursor.execute('SELECT * FROM transactions')
        transactions_data = self.cursor.fetchall()
        if company:
            transactions_data = [TransactionConfigBalance(*transaction_data) for transaction_data in transactions_data]
        else:
            transactions_data = [TransactionConfig(*transaction_data) for transaction_data in transactions_data]
        if company:
            # Calculate the balance, totalDebit, totalCredit, extract start date, and end date.
            total: float = 0.0
            totalDebit: float = 0.0
            totalCredit: float = 0.0
            startDate: str = ""
            endDate:str = ""
            data_size = transactions_data.__len__()-1
            data_index = 0
            for data in transactions_data:
                if data_index == 0 :
                    startDate = str(data.date)
                elif data_index == data_size:
                    endDate = str(data.date)
                totalDebit = totalDebit + data.debit
                totalCredit = totalCredit + data.credit
                
                if data.credit > 0:
                    total = total - data.credit
                else:
                    total = total + data.debit
                data.balance = round(total,2)
                data_index = data_index+1
            return transactions_data, totalDebit, totalCredit, startDate, endDate
        return transactions_data

    def journalRemove(self, journal:TransactionConfig):
        try:
            errorMessage = ""
            validName = utility.validate_empty(str(journal.id))
            if validName != True:
                errorMessage = errorMessage + " " + validName
            self.cursor.execute(f"DELETE FROM transactions WHERE id = ?", (str(journal.id)))
            self.connection.commit()
            return MESSAGES.SUCCESS_DATA_UPDATED
        except Exception as e:
            return f"Error: {e}"