from colores import *


def porcentaje():
    print(f"\n{BOLD}{BLUE}Has seleccionado la operacion de porcentaje{RESET}")
    a = int(input("\n Ingresa el numero: "))
    b = int(input("\n Ingresa el porcentaje: "))
    x = (a * b) / 100
    print(f"\n {BOLD}{GREEN}El resultado de la operacion es: {x}%{RESET}")
