from typing import Any
from rich.console import Console
from rich.table import Table
from rich import print
from rich.text import Text
import sys
import subprocess
from configs.Config import Config
import inquirer

def createTable(columns: list[str], rows: list[Config], name:str, title:str) -> Table:
    console = Console()
    console.rule(f"[bold red] {name}")
    table = Table(title=f"{title}")
    switchColor = True
    for colum in columns:
        table.add_column(colum, justify="left", style="green" if switchColor else "cyan")
        if(switchColor):
            switchColor = False
        else:
            switchColor = True
    for row in rows:
        row_as_strings = [str(element) for element in row.getAsList()]
        table.add_row(*row_as_strings)
    return table

def printTable(table) -> Table:
    Console().print(table)

def printRule(text: str) -> None:
    Console().rule(text)

# Clearning the screen.
def clear_screen():
    os = sys.platform
    if os == 'win32':
        subprocess.run('cls', shell=True)
    elif os == 'darwin' or os == 'linux':
        subprocess.run('clear', shell=True)
      
# Message with an emoji  
def messageEmoji(text:str, emoji:str=":information:"):
    print(f"{emoji} {text}")
    
def message(text:str):
    print(f"{text}")
    
    
# Question and Confirm
def askWithConfirm(question: str) -> Any:
    while True:
        answer = inquirer.prompt(
            questions=[
                inquirer.Text(
                    name="qs",
                    message=f"{question}"
                ),
                inquirer.List(
                    name="cs",
                    message="Do you want to processed with this choice ({qs}) ?",
                    choices=["Yes", "No", "Cancel"]
                )
            ]
        )
        if(answer.get('cs') == "Yes"):
            return answer.get("qs")
        elif answer.get("cs") == "Cancel":
            raise ValueError("Canceled Operation")
        else:
            messageEmoji(f"Please enter {question}", ":warning:")
            continue
    
    
def askWithConfirmOrKeep(question:str):
    answer = inquirer.prompt(
        questions=[
            inquirer.List(
                name="kp",
                message=f"{question}",
                choices=["Keep Previous Cell", "Edit Current Cell"]
            ),
        ]
    )
    if(answer.get('kp')=="Keep Previous Cell"):
        return None
    while True:
        answer = inquirer.prompt(
            questions=[
                inquirer.Text(
                    name="qs",
                    message=f"{question}"
                ),
                inquirer.List(
                    name="cs",
                    message="Do you want to processed with this choice ({qs}) ?",
                    choices=["Yes", "No", "Cancel"]
                )
            ]
        )
        if(answer.get('cs') == "Yes"):
            return answer.get("qs")
        elif answer.get("cs") == "Cancel":
            raise ValueError("Canceled Operation")
        else:
            messageEmoji(f"Please enter {question}", ":warning:")
            continue
    
        
def askFromList(question:str, list:[str]) -> Any:
    answer = inquirer.prompt(
        questions=[
            inquirer.List(
                name="qs",
                message=f"{question}",
                choices=list
            )
        ]
    )
    return answer.get('qs')