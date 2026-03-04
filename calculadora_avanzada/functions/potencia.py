from colores import *


# FUNCION DE POTENCIA
def potencia():
    print(f"\n{BOLD}{BLUE}Has seleccionado la operacion de potencia{RESET}")
    base = int(input("\nIngrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = base ** exponente
    print(f"\n{BOLD}{GREEN}El resultado de {base} elevado a {exponente} es: {resultado}{RESET}")
