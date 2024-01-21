from datetime import datetime
import re
from typing import Any
from .pdf_utility import PdfUtility
from datetime import date
from configs.TransactionConfig import TransactionConfigBalance
def validate_date(date_str) -> bool | str:
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError as e:
        return f"Validation Failed: {e}."
        
def validate_phone(phone_str) -> bool | str:
    validate = re.match(r'^\d{10}$', phone_str)
    if(validate == None):
        return "Validation phone number failed."
    return True

def validate_empty(text) -> bool | str:
    if(text==""):
        return "Validation text is empty."
    return True



def exportTransactionPDF(transactions: list[TransactionConfigBalance],totalDebit, totalCredit, startDate, endDate):
            
    nPdf = PdfUtility()
    nPdf.createTable([
        "ID",
        "CD",
        "Company Name",
        "Account---",
        "Description--",
        "Source---",
        "Date-----",
        "Rec.#",
        "Debit",
        "Credit",
        "Balance"
        ]
    )
    
    for row in transactions:
        nPdf.addRowTable([
            str(row.id),
            str(row.company_id),
            str(row.company_name), 
            row.account,
            row.description,
            row.source,
            str(row.date),
            str(row.receipt_num),
            str(row.debit),
            str(row.credit),
            str(row.balance) 
        ])
        nPdf.emptyNewLine()
    nPdf.emptyNewLine(10)
    nPdf.styleLine()
    nPdf.emptyNewLine(10)
    nPdf.addTextCenterArray([
        f"Start Date: {startDate}",
        f"Start Date: {startDate}",
        f"End Date: {endDate}",
        f"Total Credit: {round(totalCredit, 2)}",
        f"Total debit: {round(totalDebit, 2)}",
        f"Reaming Value of Goods: {round(totalDebit-totalCredit, 2)}"
    ])
    
    try:
        if len(transactions)<0:
            raise IndexError("No transactions to read.")
        nPdf.export(f"assets/output-{date.today()}-{transactions[0].company_name}.pdf")
    except Exception as e:
        print(e)
    
        
def sqlGenerateSetClause(id:int, data: dict[str, Any | None], table:str):
    # Generate the SET clause for the SQL query
    set_clause = ', '.join(f'{key} = ?' for key, value in data.items() if value is not None)

    # Execute the update query
    query = f'''
        UPDATE {table}
        SET {set_clause}
        WHERE id = ?
    '''
    values = [value for value in data.values() if value is not None] + [id]
    return query, values