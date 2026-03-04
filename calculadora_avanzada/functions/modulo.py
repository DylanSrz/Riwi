from colores import *


def modulo():
    print(f"\n{BLUE}{BOLD}Has seleccionado la operacion de modulo{RESET}")
    a = int(input("\nIngrese el dividendo: "))
    b = int(input("Ingrese el divisor: "))
    resultado = a % b
    print(f"\n{BOLD}{GREEN}El resultado de {a} mod {b} es: {resultado}{RESET}")
