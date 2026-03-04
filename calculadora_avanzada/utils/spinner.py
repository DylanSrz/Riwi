import sys
import time
from colores import *


def spinner(seconds):
    symbols = ["|", "/", "-", "\\"]
    start = time.time()
    i = 0

    while time.time() - start < seconds:
        sys.stdout.write(f"\r{YELLOW}Procesando {symbols[i % 4]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    print(f"\r{GREEN}Procesado  ✔{RESET}")


# spinner(3) simula proceso de 3 segundos
