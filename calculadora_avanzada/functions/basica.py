from colores import *
from utils.spinner import spinner
import os


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")
# FUNCIONES DE LA CALCULADORA BASICA


def resultado(x):
    print(" ")
    spinner(2)
    print(f"\n {BG_GREEN}El resultado de la operacion es: {x}{RESET}")


def suma():
    a = int(input("\n Ingrese el 1er número: "))
    b = int(input("\n Ingrese el 2do número: "))
    x = a + b
    resultado(x)


def resta():
    a = int(input("\n Ingrese el 1er número: "))
    b = int(input("\n Ingrese el 2do número: "))
    x = a - b
    resultado(x)


def multi():
    a = int(input("\n Ingrese el 1er número: "))
    b = int(input("\n Ingrese el 2do número: "))
    x = a * b
    resultado(x)


def div():
    a = int(input("\n Ingrese el 1er número: "))
    b = int(input("\n Ingrese el 2do número: "))
    x = a / b
    resultado(x)


def basiquita():
    print(
        f"\n{BLUE}{BOLD}Has seleccionado la operacion de operaciones basicas{RESET}")
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    basica = (
        input(f"\n{BOLD}{BLUE}¿Qué operacion basica desea realizar?: {RESET}"))
    if basica == "1":
        suma()
    elif basica == "2":
        resta()
    elif basica == "3":
        multi()
    elif basica == "4":
        div()
    else:
        limpiar()
        print(f"\n{BG_RED}{BOLD}Seleccione una opcion valida.{RESET}")
        basiquita()
