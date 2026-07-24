from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.align import Align
from pyfiglet import figlet_format
from rich import box

console= Console()

def titulo(text) :
    art = figlet_format (text, font='straight')
    console.print(Align.center(f"[#0022FF]{art}[/#0022FF]"))

def subtitulo(text) :
    console.print(Panel.fit(text, style='bold bright_green'))
def captura(i):
    console.print(f"[bold blue]Capture {i}[/bold blue]")

def error(text):
    console.print(f"[red][X][/red] {text}")
def alerta(text):
    console.print(f'[yellow][!][/yellow] {text}')
def inputt(text):
    console.print(Panel.fit(text, border_style='#97DAF7'))
    return console.input ('[#01796F]→[/#01796F]')

def show_menu():
    console.print(Panel(
        '[bold cyan]1.[/bold cyan] Register a new sale\n'
        "[bold cyan]2.[/bold cyan] Search for an existing order\n"
        "[bold cyan]3.[/bold cyan]  Exit the program",
        title='PURIFIED WATER SYSTEM',
        border_style= "blue"
        ))
    return Prompt.ask ("Choose an option", choices= ["1", "2"])
def final_ticket (num_cliente, litros, subtotal, descuento, iva, total):
    table = Table(title=f"Ticket - Client {num_cliente}")
    table.add_column ("Concept", style="cyan")
    table.add_column ("Amount", justify="right", style="green")

    table.add_row("Liters bought", f"{litros} L")
    table.add_row("Subtotal", f"${subtotal:.2f}")
    table.add_row("Discount", f"-${descuento:.2f}")
    table.add_row("IVA (16%)", f"${iva:.2f}")
    table.add_row("Total Due", f"[bold]${total:.2f}[/bold]")

    console.print(table)

def resume (clientes, total_litros, total_pesos, total_descuentos, ID_client):
    table = Table(
        title="Day resume", 
        style="bold blue", 
        border_style="bright_blue",
        box=box.ROUNDED)
    
    table.add_column("", style= "cyan")
    table.add_column("", justify="right", style="green")

    table.add_row("Costumers reached:", f"{clientes}")
    table.add_row("Liters selled:", f"{total_litros} L")
    table.add_row("Total collected:", f"${total_pesos:.2f}")
    table.add_row("Total discount amount:", f"${total_descuentos:.2f}")
    table.add_row("Your order is the:", f"{ID_client}")

    console.print(table)

def ticketID (ID_client, acumc_1, total_con_iva, fecha, hora):
    table = Table (
        title=f"Client: {ID_client}",
        style="bold blue",
        border_style="bright_blue",
        box=box.ROUNDED
    )
    table.add_column("", style= "cyan")
    table.add_column("", justify="right", style="green")

    table.add_row("Ticket ID:", f"{ID_client}")
    table.add_row("Total water:", f"{acumc_1}")
    table.add_row("Total paid:", f"{total_con_iva:.2f}")
    table.add_row("Date:", f"{fecha}")
    table.add_row("Time:", f"{hora}")

    console.print(table)


