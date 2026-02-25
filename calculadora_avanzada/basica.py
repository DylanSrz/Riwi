# FUNCIONES DE LA CALCULADORA BASICA

def suma():
    a = int(input("\n Dame el 1er numero: "))
    b = int(input("\n Dame el 2do numero: "))
    x = a + b
    print(f"\n El resultado de la operacion es: {x }")

def resta():
    a = int(input("\n Dame el 1er numero: "))
    b = int(input("\n Dame el 2do numero: "))
    x = a - b
    print(f"\n El resultado de la operacion es: {x }")

def multi():
    a = int(input("\n Dame el 1er numero: "))
    b = int(input("\n Dame el 2do numero: "))
    x = a * b
    print(f"\n El resultado de la operacion es: {x }")

def div():
    a = int(input("\n Dame el 1er numero: "))
    b = int(input("\n Dame el 2do numero: "))
    x = a / b
    print(f"\n El resultado de la operacion es: {x }")


def basiquita():
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    basica = int(input("\n¿Qué operacion basica desea realizar?: "))
    if basica == 1:
        suma()
    elif basica == 2:
        resta()
    elif basica == 3:
        multi()
    elif basica == 4:
        div()
    else:
        print("\nSeleccione una opcion valida.")
        
