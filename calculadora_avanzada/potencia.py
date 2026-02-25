# FUNCION DE POTENCIA
def potencia():
    print("\nHas seleccionado la operacion de potencia")
    base = int(input("\nIngrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = base ** exponente
    print(f"\nEl resultado de {base} elevado a {exponente} es: {resultado}")
