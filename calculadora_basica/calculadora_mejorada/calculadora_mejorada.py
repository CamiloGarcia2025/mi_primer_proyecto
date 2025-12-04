# calculadora_mejorada.py
# Mejora respecto a la calculadora básica:
# - Se agregaron funciones para cada operación
# - Se validan entradas para evitar errores
# - Se incluye un menú interactivo con opción de salir
# - Se permite repetir cálculos sin reiniciar el programa
# - Se maneja la división por cero y operaciones inválidas
# - Se formatea el resultado a 2 decimales


def leer_numero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return float(valor)
        except ValueError:
            print("Error: ingresa un número válido.")

def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        print("Error: no se puede dividir por cero.")
        return None
    return a / b

def mostrar_menu():
    print("\n=== Calculadora mejorada ===")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")

def ejecutar_operacion(op, n1, n2):
    if op == "1": return sumar(n1, n2)
    if op == "2": return restar(n1, n2)
    if op == "3": return multiplicar(n1, n2)
    if op == "4": return dividir(n1, n2)
    print("Operación no válida.")
    return None

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()
        if opcion == "5":
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

        n1 = leer_numero("Primer número: ")
        n2 = leer_numero("Segundo número: ")

        resultado = ejecutar_operacion(opcion, n1, n2)
        if resultado is not None:
            print(f"Resultado: {round(resultado, 2)}")

if __name__ == "__main__":
    main()
