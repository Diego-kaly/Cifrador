#!/usr/bin/env python3
import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from rich import box

# Configuración de Rich
console = Console()

# --- DICCIONARIO DE DATOS ---
MAPA_CIFRADO = {
    'q': '~', 'w': '`', 'e': '|', 'r': '•', 't': '√', 'y': 'π', 'u': '÷',
    'i': '×', 'o': '§', 'p': '∆', 'a': '£', 's': '€', 'd': '₡', 'f': '₲',
    'g': '^', 'h': '°', 'j': '=', 'k': '{', 'l': '}', 'ñ': '\\', 'z': '%',
    'x': '©', 'c': '®', 'v': '™', 'b': '✓', 'n': '[', 'm': ']'
}

# Mapa inverso
MAPA_DESCIFRADO = {v: k for k, v in MAPA_CIFRADO.items()}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    limpiar_pantalla()
    titulo = "[bold cyan]ENCRIPTADOR TERMUX[/bold cyan]"
    subtitulo = "[dim]Sistema de sustitución de símbolos[/dim]"
    contenido = f"{titulo}\n{subtitulo}"
    console.print(Panel(Align.center(contenido), border_style="green", box=box.ROUNDED))

def encriptar(texto):
    resultado = ""
    texto = texto.lower()
    for letra in texto:
        if letra in MAPA_CIFRADO:
            resultado += MAPA_CIFRADO[letra]
        else:
            resultado += letra 
    return resultado

def desencriptar(texto):
    resultado = ""
    for letra in texto:
        if letra in MAPA_DESCIFRADO:
            resultado += MAPA_DESCIFRADO[letra]
        else:
            resultado += letra
    return resultado

def main():
    while True:
        mostrar_banner()
        console.print("[1] [bold green]Encriptar[/bold green]")
        console.print("[2] [bold yellow]Desencriptar[/bold yellow]")
        console.print("[3] [bold red]Salir[/bold red]")
        console.print("")
        
        opcion = Prompt.ask("[bold white]Opción[/bold white]", choices=["1", "2", "3"])

        if opcion == "1":
            console.print("\n[bold cyan]-- MODO ENCRIPTAR --[/bold cyan]")
            mensaje = Prompt.ask("Escribe tu oración")
            with console.status("[bold green]Procesando...[/bold green]", spinner="dots"):
                time.sleep(1)
                resultado = encriptar(mensaje)
            console.print(Panel(f"[bold yellow]{resultado}[/bold yellow]", title="Resultado", border_style="cyan"))
            Prompt.ask("\nEnter para continuar...")

        elif opcion == "2":
            console.print("\n[bold cyan]-- MODO DESENCRIPTAR --[/bold cyan]")
            mensaje = Prompt.ask("Pega el código")
            with console.status("[bold yellow]Decodificando...[/bold yellow]", spinner="dots"):
                time.sleep(1)
                resultado = desencriptar(mensaje)
            console.print(Panel(f"[bold green]{resultado}[/bold green]", title="Original", border_style="green"))
            Prompt.ask("\nEnter para continuar...")

        elif opcion == "3":
            console.print("[bold red]Saliendo...[/bold red]")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Interrumpido.[/bold red]")
  
