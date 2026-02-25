'''CALCULADORA AVANZADA'''
#import basica
from basica import suma, resta, multi, div, basiquita
# from potencia import
# from raiz import
# from porcentaje import
# from modulo import
# from promedio import


print("\nBienvenido a la calculadora ")

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
elif operacion ==2:
    print("Potencia")
elif operacion ==3:
    print("Raiz")
elif operacion ==4:
    print("Porcentaje")
elif operacion ==5:
    print("Modulo")
elif operacion ==6:
    print("Promedio")
else:
    print("Ingrese una opción valida.")


