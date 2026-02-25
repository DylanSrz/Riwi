'''CALCULADORA AVANZADA'''
# import basica
from basica import basiquita
from potencia import potencia
from raiz import raiz
from porcentaje import porcentaje
from modulo import modulo
from promedio import promedio
import datetime


def menu():
    print("\n" + datetime.datetime.now().strftime("Fecha: %Y-%m-%d"))
    print(datetime.datetime.now().strftime("Hora: %H:%M"))
    print("\n===================================")
    print("    Bienvenido a la calculadora ")
    print("===================================")
    print("\nMenu:")
    print("\n1. Basicas.")
    print("2. Potencia.")
    print("3. Raiz.")
    print("4. Porcentaje.")
    print("5. Modulo.")
    print("6. Promedio.")

    operacion = int(input("\n¿Qué operacion desea realizar?: "))

    if operacion == 1:
        basiquita()
    elif operacion == 2:
        potencia()
    elif operacion == 3:
        raiz()
    elif operacion == 4:
        porcentaje()
    elif operacion == 5:
        modulo()
    elif operacion == 6:
        promedio()
    else:
        print("Ingrese una opción valida.")
