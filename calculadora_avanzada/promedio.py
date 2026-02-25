# FUNCION DE PROMEDIO
def promedio():
    print("\nHas seleccionado la operacion de promedio")
    cantidad = int(input("\nIngrese la cantidad de numeros a promediar: "))
    numeros = []
    for i in range(cantidad):
        numero = float(input(f"Ingrese el numero {i+1}: "))
        numeros.append(numero)
    resultado = sum(numeros) / cantidad
    print(f"\nEl resultado del promedio es: {resultado}")
