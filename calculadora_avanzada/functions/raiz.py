from colores import *


# FUNCION DE RAIZ
def raiz():
    print(f"\n{BOLD}{BLUE}Has seleccionado la operacion de raiz{RESET}")
    numero = int(input("\nIngrese el numero: "))
    resultado = numero ** 0.5
    print(f"\n{BOLD}{GREEN}El resultado de la raiz cuadrada de {numero} es: {resultado}{RESET}")
