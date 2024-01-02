import util.style.styles as Styles
from models.CompanyModel import CompanyModel
from util.menus import COMPANY_MENU
import inquirer
from database import Database
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
                Styles.askWithConfirm("Select ID"),
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