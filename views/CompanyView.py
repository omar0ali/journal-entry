import util.style.styles as Styles
from models.CompanyModel import CompanyModel
from util.menus import COMPANY_MENU
from db.database_sql import Database
def display_menu(db: Database):
    company = CompanyModel(db)
    Styles.clear_screen()
    Styles.printTable(
        Styles.createTable(
            ["ID", "Name", "Start Date", "Description", "Email", "Phone"],
            company.getCompanies(),
            "Companies",
            "Registered Companies"
        )
    )
    answer = Styles.askFromList("Company Menu", COMPANY_MENU.LIST)
    if answer == COMPANY_MENU.INSERT_COMPANY:
        try:
            result = company.companyInsert(
                Styles.askWithConfirm("Company Name"),
                Styles.askWithConfirm("Date (YYYY-MM-DD)"),
                Styles.askWithConfirm("Memo or Description"),
                Styles.askWithConfirm("Email (example@gmail.com)"),
                Styles.askWithConfirm("Phone 10 digits")
            )
            Styles.clear_screen()
            Styles.messageEmoji(result)
        except Exception as e:
            Styles.messageEmoji(e, ":x:")
    elif answer == COMPANY_MENU.EDIT_COMPANY:
        try:
            result = company.companyUpdate(
                Styles.askFromList("Select Row To Edit",company.getCompanies()),
                Styles.askWithConfirmOrKeep("Company Name"),
                Styles.askWithConfirmOrKeep("Date (YYYY-MM-DD)"),
                Styles.askWithConfirmOrKeep("Memo or Description"),
                Styles.askWithConfirmOrKeep("Email (example@gmail.com)"),
                Styles.askWithConfirmOrKeep("Phone 10 digits")
            )
            
            Styles.messageEmoji(result)
        except Exception as e: 
            Styles.messageEmoji(e, ":x:")
            
    elif answer == COMPANY_MENU.REMOVE_COMPANY:
        try:
            result = company.companyRemove(
                Styles.askFromList("Select Row To Remove",company.getCompanies())   
            )
            Styles.clear_screen()
            Styles.messageEmoji(result)
        except Exception as e:
            Styles.messageEmoji(e, ":x:")