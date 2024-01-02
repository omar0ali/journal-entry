import util.style.styles as Styles
from models.TransactionsModel import TransactionModel
from models.CompanyModel import CompanyModel
from util.menus import All_TRANSACTIONS_MENU
from database import Database
def display_menu(db:Database):
    journal = TransactionModel(db)
    company = CompanyModel(db)
    Styles.clear_screen()
    Styles.printTable(
        Styles.createTable(
            ["ID", "Copmany ID", "Account", "Description", "Source", "Date", "Receipt Number", "Debit", "Credit"],
            journal.getJournals(),
            "Journals",
            "Registered Journals"
        )
    )
    answer = Styles.askFromList("Transaction Menu", All_TRANSACTIONS_MENU.LIST)
    if answer == All_TRANSACTIONS_MENU.INERT_TRANSACTION:
        try:
            result = journal.transactionInsert(
                Styles.askFromList("Select Company", company.getCompanies()),
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