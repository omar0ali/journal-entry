from configs.CompanyConfig import CompanyConfig
import util.style.styles as Styles
from models.TransactionsModel import TransactionModel
from models.CompanyModel import CompanyModel
from util.menus import All_TRANSACTIONS_MENU
from db.database_sql import Database
from db.database_json import DatabaseJSON
from util import utility as Utility



def display_menu_company(db:Database):
    journal = TransactionModel(db)
    company = CompanyModel(db)
    answer:CompanyConfig = Styles.askFromList("Select Company", company.getCompanies())
    transactions, totalDebit, totalCredit, startDate, endDate = journal.getJournals(answer)
    Styles.clear_screen()
    Styles.printTable(
        Styles.createTable(
            ["ID", "Company ID", "Company Name", "Account", "Description", "Source", "Date", "Receipt Number", "Debit", "Credit", "Balance"],
            transactions,
            "Journals",
            "Registered Journals"
        )
    )
    print(f"Start Date: {startDate}")
    print(f"End Date: {endDate}")
    print(f"Total Debit: {round(totalDebit,2)}")
    print(f"Total Credit: {round(totalCredit,2)}")
    print(f"Reaming Value of Goods: {round(totalDebit-totalCredit, 2)}")
    print("-------------")
    tempAnswer = Styles.askFromList(
        "Would you like to export this table to a PDF file", ["Yes", "No"]
    )
    if tempAnswer == "Yes":
        Utility.exportTransactionPDF(transactions, totalDebit, totalCredit, startDate, endDate)
    
def display_menu(db:Database):
    journal = TransactionModel(db)
    company = CompanyModel(db)
    Styles.clear_screen()
    Styles.printTable(
        Styles.createTable(
            ["ID", "Company ID", "Company Name", "Account", "Description", "Source", "Date", "Receipt Number", "Debit", "Credit"],
            journal.getJournals(),
            "Journals",
            "Registered Journals"
        )
    )
    answer = Styles.askFromList("Transaction Menu", All_TRANSACTIONS_MENU.LIST)
    if answer == All_TRANSACTIONS_MENU.INERT_TRANSACTION:
        db = DatabaseJSON()
        try:
            answer: CompanyConfig = Styles.askFromList("Select Company", company.getCompanies())
            result = journal.transactionInsert(
                answer,
                answer.name,
                Styles.askWithConfirmShowHistory("Account","Account", db),
                Styles.askWithConfirmShowHistory("Description", "Description", db),
                Styles.askWithConfirmShowHistory("Source", "Source", db),      
                Styles.askDateConfirm("Date (YYYY-MM-DD)"),
                Styles.askWithConfirmShowHistory("Receipt Number", "Receipt Number",db),
                Styles.askWithConfirm("Debit"),
                Styles.askWithConfirm("Credit")
            )
            Styles.clear_screen()
            Styles.messageEmoji(result)
        except Exception as e:
            Styles.messageEmoji(e, ":x:")
    elif answer == All_TRANSACTIONS_MENU.EDIT_TRANSACTION:
        try:
            answer: CompanyConfig = Styles.askFromList("Select Company", company.getCompanies())
            result = journal.transactionUpdate(
                Styles.askFromList("Select Transaction", journal.getJournals()),
                answer.id,
                answer.name,
                Styles.askWithConfirmOrKeep("Account"),
                Styles.askWithConfirmOrKeep("Description"),
                Styles.askWithConfirmOrKeep("Source"),
                Styles.askWithConfirmOrKeep("Date (YYYY-MM-DD)"),
                Styles.askWithConfirmOrKeep("Receipt Number"),
                Styles.askWithConfirmOrKeep("Debit"),
                Styles.askWithConfirmOrKeep("Credit")
            )
            Styles.clear_screen()
            Styles.messageEmoji(result)
        except Exception as e:
            Styles.messageEmoji(e, ":x:")
    elif answer == All_TRANSACTIONS_MENU.REMOVE_TRANSACTION:
        try:
            result = journal.journalRemove(
                Styles.askFromList("Select Row To Remove",journal.getJournals())
            )
            Styles.clear_screen()
            Styles.messageEmoji(result)
        except Exception as e:
            Styles.messageEmoji(e, ":x:")