from rich.console import Console
from rich.table import Table
from Config import Config

def createTable(columns: list[str], rows: list[Config], name:str, title:str) -> Table:
    console = Console()
    console.rule(f"[bold red] {name}")
    table = Table(title=f"{title}")
    switchColor = True
    for colum in columns:
        table.add_column(colum, justify="left", style="green" if switchColor else "cyan")
        switchColor = False
    for row in rows:
        table.add_row(row.getAsList())
    return table