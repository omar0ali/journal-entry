from configs.CompanyConfig import CompanyConfig
import util.style.styles as Styles
from models.TransactionsModel import TransactionModel
from models.CompanyModel import CompanyModel
from util.menus import All_TRANSACTIONS_MENU
from db.database_sql import Database



def display_menu_company(db:Database):
    journal = TransactionModel(db)
    company = CompanyModel(db)
    answer:CompanyConfig = Styles.askFromList("Select Company", company.getCompanies())
    Styles.clear_screen()
    Styles.printTable(
        Styles.createTable(
            ["ID", "Company ID", "Company Name", "Account", "Description", "Source", "Date", "Receipt Number", "Debit", "Credit", "Balance"],
            journal.getJournals(answer),
            "Journals",
            "Registered Journals"
        )
    )
    
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
        try:
            answer: CompanyConfig = Styles.askFromList("Select Company", company.getCompanies())
            result = journal.transactionInsert(
                answer,
                answer.name,
                Styles.askWithConfirm("Account"),
                Styles.askWithConfirm("Description"),
                Styles.askWithConfirm("Source"),      
                Styles.askWithConfirm("Date (YYYY-MM-DD)"),
                Styles.askWithConfirm("Receipt Number"),
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