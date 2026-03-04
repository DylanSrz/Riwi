from colores import *


def continue_():

    while True:

        continua = input(
            f"\n{BLUE}{BOLD}¿Desea realizar otra operación? (si/no): {RESET}").lower()

        try:
            if continua == "si":
                return True
            elif continua == "no":
                print(
                    f"\n{CYAN}{BOLD}Gracias por usar nuestra APP. ¡Hasta pronto!{RESET}")
                return False
            else:
                print(
                    f"\n{BG_YELLOW}{BOLD}¡Valor invalido!, Intente nuevamente.{RESET}")
                continue
        except Exception as e:
            print(f"\n{BG_RED}{BOLD}Error: {e}{RESET}")
        break
