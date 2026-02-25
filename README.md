# 🧮 **Calculadora Avanzada en Python**

Una calculadora modular de línea de comandos diseñada en Python.
Este proyecto permite realizar desde operaciones aritméticas básicas
hasta cálculos de potencias, raíces y promedios, todo bajo una estructura
de archivos organizada y fácil de mantener.

## 🚀 *Características*
El sistema cuenta con un menú interactivo que incluye las siguientes funciones:
- Operaciones Básicas: Suma, resta, multiplicación y división.
- Cálculos Avanzados:
  - Potenciación (base y exponente).
  - Raíz cuadrada.
  - Cálculo de porcentajes.
  - Módulo (residuo de la división).
- Estadística Simple: Promedio de $n$ cantidad de números.
- Utilidades: Muestra la fecha y hora actual al iniciar la sesión.

## 📁 *Estructura del Proyecto*
El código está dividido en módulos para facilitar la lectura y escalabilidad:


| Archivo | Descripción|
| :--- | :--- |
| main.py | Punto de entrada del programa.|
| menu.py | Gestiona la interfaz de usuario y la navegación. |
| basica.py | Contiene las operaciones fundamentales (+, -, *, /). |
| potencia.py | Lógica para elevar números. |
| raiz.py | Cálculo de raíz cuadrada. |
| porcentaje.py | Obtención de porcentajes. |
| modulo.py | Cálculo del residuo de una división. |
| promedio.py | Lógica para promediar una lista de números. |


## 🛠️ *Instalación y Uso*
Requisitos previos
  - Tener instalado Python 3.x. No requiere librerías externas adicionales,
    ya que utiliza módulos nativos como datetime.

Ejecución:
1. Clona este repositorio o descarga los archivos.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo principal:

  ```
  python main.py
  ```

## 📝 *Ejemplo de Uso*
Al ejecutar el programa, verás un encabezado con la fecha actual y las opciones disponibles:

```
Fecha: 2026-02-24
Hora: 23:15

===================================
    Bienvenido a la calculadora 
===================================

Menu:
1. Basicas.
2. Potencia.
...
¿Qué operacion desea realizar?:

```

## 🛡️ *Próximas Mejoras (Roadmap)*

- [ ] Implementar manejo de errores (ej. división por cero).
- [ ] Agregar funciones trigonométricas (Seno, Coseno).
- [ ] Crear una interfaz gráfica (GUI) con Tkinter.

