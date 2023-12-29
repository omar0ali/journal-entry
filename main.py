from typing import Any
from database import Database
import inquirer
from rich.console import Console
from pyfiglet import Figlet
import sys, subprocess

class Main:
    console = Console()
    db = Database()# Init tables.
    def __init__(self) -> None:
        self.clear_screen()
        f = Figlet(font='small')
        print(f.renderText('Account of statement'))
        self.display_menu() 

    #Display the menu
    def display_menu(self):
        self.console.rule("[bold red]Main Menu")
        while(True):
            answer = inquirer.prompt(questions=[inquirer.List(
                name="select", 
                message="Operations", 
                choices=["All Accounts",
                        "Accounts of a company",
                        "Insert a company",
                        "Exit"]
                )])
            
            
            
            if answer.get('select') == "Exit":
                self.clear_screen()
                break
             
    
    
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
