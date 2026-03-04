from colores import *


# FUNCION DE PROMEDIO
def promedio():
    print(f"\n{BOLD}{BLUE}Has seleccionado la operacion de promedio{RESET}")
    cantidad = int(input("\nIngrese la cantidad de numeros a promediar: "))
    numeros = []
    for i in range(cantidad):
        numero = float(input(f"Ingrese el numero {i+1}: "))
        numeros.append(numero)
    resultado = sum(numeros) / cantidad
    print(f"\n{BOLD}{GREEN}El resultado del promedio es: {resultado}{RESET}")
