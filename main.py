from typing import Any
from database import Database
import inquirer
from rich.console import Console
from rich.table import Table
from pyfiglet import Figlet
import sys, subprocess
from util.menus import MAIN_MENU, COMPANY_MENU
from models.company import Company
from util.utility import Utility
import styles


class Main:
    console = Console()
    db = None
    def __init__(self) -> None:
        self.clear_screen()
        f = Figlet(font='small')
        print(f.renderText('Account of statement'))
        self.db = Database()
        self.utility = Utility()
        self.company = Company(self.db)
        self.display_menu() 
        

    #Display the menu
    def display_menu(self):
        self.console.rule("[bold red]Main Menu")
        while(True):
            answer = inquirer.prompt(
                questions=[
                    inquirer.List(
                        name="selectMain", 
                        message="Operations", 
                        choices=MAIN_MENU.LIST
                    )
                ]
            )
            
            if answer.get('selectMain') == MAIN_MENU.EXIT:
                self.clear_screen()
                break
            
            if answer.get('selectMain') == MAIN_MENU.ADD_COMPANY:
                self.clear_screen()
                table = styles.createTable(
                    ["ID", "Name", "Start Date", "Description", "Email", "Phone"],
                    self.company.getCompanies(),
                    "Companies",
                    "Registered Companies"
                )
                self.console.print(table)
                companyAnswer = inquirer.prompt(
                    questions=[
                        inquirer.List(
                            name="selectCompany",
                            message="Operation",
                            choices=COMPANY_MENU.LIST
                        )
                    ]
                )
                if companyAnswer.get('selectCompany') == COMPANY_MENU.GO_BACK:
                    self.clear_screen()
                    pass
                elif companyAnswer.get('selectCompany') == COMPANY_MENU.INSERT_COMPANY:
                    qCompanyAnswer = inquirer.prompt(
                        questions=[
                            inquirer.Text(
                                name="CompanyName",
                                message="Name of the company"
                            ), 
                            inquirer.Text(
                                name="CompanyDate",
                                message="Enter date. Must follow (YYYY-MM-DD) Date"
                            ),
                            inquirer.Text(
                                name="CompanyDescription",
                                message="Description"
                            ),
                            inquirer.Text(
                                name="CompanyEmail",
                                message="Email Address"
                            ),
                            inquirer.Text(
                                name="CompanyPhone",
                                message="Phone Number. Must be 10 numbers"
                            )
                        ]
                    )
                    self.company.companyInsert(
                        qCompanyAnswer.get('CompanyName'),
                        qCompanyAnswer.get('CompanyDate'),
                        qCompanyAnswer.get('CompanyDescription'),
                        qCompanyAnswer.get('CompanyEmail'),
                        qCompanyAnswer.get('CompanyPhone')
                    )
                    self.clear_screen()
                
                
             
    
    
    #Clearning the screen.
    def clear_screen(self):
        os = sys.platform
        if os == 'win32':
            subprocess.run('cls', shell=True)
        elif os == 'darwin' or os == 'linux':
            subprocess.run('clear', shell=True)




#################
#   Start app   #
#################
main = Main()
