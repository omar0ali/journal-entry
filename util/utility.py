from datetime import datetime
import re
from typing import Any
from rich.console import Console
from fpdf import FPDF
import os

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
    pdf = FPDF()
    pdf.set_margins(3, 10, 3)
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(5, 10, "ID", 1)
    pdf.cell(5, 10, "C.I", 1)
    pdf.cell(30, 10, "Comp.Name", 1)
    pdf.cell(25, 10, "Account", 1)
    pdf.cell(35, 10, "Desc", 1)
    pdf.cell(25, 10, "Source", 1)
    pdf.cell(20, 10, "Date", 1)
    pdf.cell(10, 10, "Rec.#", 1)
    pdf.cell(15, 10, "Debit", 1)
    pdf.cell(15, 10, "Credit", 1)
    pdf.cell(15,10, "Balance",1)
    pdf.ln()
    for row in transactions:
        pdf.cell(5, 10, str(row.id), 1)
        pdf.cell(5, 10, str(row.company_id), 1)
        pdf.cell(30, 10, str(row.company_name), 1)
        pdf.cell(25, 10, str(row.account), 1)
        pdf.cell(35, 10, str(row.description), 1)
        pdf.cell(25, 10, str(row.source), 1)
        pdf.cell(20, 10, str(row.date), 1)
        pdf.cell(10, 10, str(row.receipt_num), 1)
        pdf.cell(15, 10, str(row.debit), 1)
        pdf.cell(15, 10, str(row.credit), 1)
        pdf.cell(15, 10, str(row.balance), 1)
        pdf.ln()
    # Add lines under the table
    pdf.ln(10)  # Add some space before the lines
    pdf.line(10, pdf.get_y(), 190, pdf.get_y())  # Horizontal line
    pdf.ln(10)  # Add more space before the next line   
    pdf.cell(0, 10, f"Start Date: {startDate}", ln=True, align='C')
    pdf.cell(0, 10, f"End Date: {endDate}", ln=True, align='C')
    pdf.cell(0, 10, f"Total Credit: {round(totalCredit, 2)}", ln=True, align='C')
    pdf.cell(0, 10, f"Total debit: {round(totalDebit, 2)}", ln=True, align='C')
    pdf.cell(0, 10, f"Reaming Value of Goods: {round(totalDebit-totalCredit, 2)}", ln=True, align='C')
    checkDirExists("assets")
    pdf.output("assets/output.pdf")
    print("PDF file exported")
    print(os.getcwd()+"/assets/output.pdf")
    
    
    
def checkDirExists(dir: str):
    dir: str = os.getcwd()+"/"+dir
    if not os.path.exists(dir):    
        os.makedirs(dir)
        print(f"Directory '{dir}' created.")
    else:
        print(f"Directory '{dir}' already exists.")
        
        
        
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