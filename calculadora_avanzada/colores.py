# ansi.py

# Escape base
ESC = "\033["
RESET = f"{ESC}0m"

# Estilos
BOLD = f"{ESC}1m"
UNDERLINE = f"{ESC}4m"
REVERSED = f"{ESC}7m"

# Colores de texto
BLACK = f"{ESC}30m"
RED = f"{ESC}31m"
GREEN = f"{ESC}32m"
YELLOW = f"{ESC}33m"
BLUE = f"{ESC}34m"
MAGENTA = f"{ESC}35m"
CYAN = f"{ESC}36m"
WHITE = f"{ESC}37m"

# Fondos
BG_RED = f"{ESC}41m"
BG_GREEN = f"{ESC}42m"
BG_YELLOW = f"{ESC}43m"
BG_BLUE = f"{ESC}44m"


# USO
# print(f"{BOLD}{RED}Error crítico{RESET}")
