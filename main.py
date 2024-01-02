from database import Database
import inquirer
from pyfiglet import Figlet
from util.menus import MAIN_MENU
from models.CompanyModel import CompanyModel
import util.style.styles as Styles
import views.CompanyView as CompanyView

class Main:
    db = None
    def __init__(self) -> None:
        Styles.clear_screen()
        print(Figlet(font='small').renderText('Journal Entry'))
        # Create/Load and prepare database.
        self.db = Database()
        # Set up connection
        self.company = CompanyModel(self.db)
        # Display MainMenu
        self.display_menu() 
        

    # Display the menu
    def display_menu(self):
        Styles.printRule("[bold red]Main Menu")
        while(True):
            answer = Styles.askFromList("Menu", MAIN_MENU.LIST)
            if answer == MAIN_MENU.ADD_COMPANY:
                CompanyView.display_menu(self.db)
                
            if answer == MAIN_MENU.EXIT:
                Styles.message("Data saved. Exit.")
                break
                




#################
#   Start app   #
#################
main = Main()
