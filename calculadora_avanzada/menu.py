'''CALCULADORA AVANZADA'''
# import basica
from functions.basica import basiquita
from functions.potencia import potencia
from functions.raiz import raiz
from functions.porcentaje import porcentaje
from functions.modulo import modulo
from functions.promedio import promedio
from utils.continuar import continue_
from colores import *
from utils.barra import progress_bar
from utils.spinner import spinner
import datetime
import os


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def menu():

    while True:

        print(f"\n{MAGENTA}"+datetime.datetime.now().strftime("Fecha: %Y-%m-%d"))
        print(datetime.datetime.now().strftime("Hora: %H:%M"))
        print(f"\n{BG_BLUE}{BOLD}==================================={RESET}")
        print(f"{BG_BLUE}{BOLD}    Bienvenido a la calculadora    {RESET}")
        print(f"{BG_BLUE}{BOLD}==================================={RESET}")
        print(f"\n{BLUE}{BOLD}Menu:{RESET}")
        print(f"\n1. Basicas.")
        print("2. Potencia.")
        print("3. Raiz.")
        print("4. Porcentaje.")
        print("5. Modulo.")
        print("6. Promedio.")

        operacion = input(
            f"\n {BOLD}{BLUE}¿Qué operacion desea realizar?: {RESET}")

        if operacion == "1":
            limpiar()
            basiquita()
            if not continue_():
                break
        elif operacion == "2":
            limpiar()
            potencia()
            if not continue_():
                break
        elif operacion == "3":
            limpiar()
            raiz()
            if not continue_():
                break
        elif operacion == "4":
            limpiar()
            porcentaje()
            if not continue_():
                break
        elif operacion == "5":
            limpiar()
            modulo()
            if not continue_():
                break
        elif operacion == "6":
            limpiar()
            promedio()
            if not continue_():
                break
        else:
            limpiar()
            spinner(2)
            print(
                f"\n{BG_YELLOW}{BOLD}Por favor ingrese una opción valida.{RESET}")


menu()
