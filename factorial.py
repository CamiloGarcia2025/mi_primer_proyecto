# factorial.py
# Función implementada por el estudiante 3
# Mejora: cálculo del factorial con validación de entrada

def calcular_factorial(n):
    if n < 0:
        return "Error: el número debe ser positivo."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Prueba directa de la función
if __name__ == "__main__":
    try:
        numero = int(input("Ingresa un número para calcular su factorial: "))
        print("Resultado:", calcular_factorial(numero))
    except ValueError:
        print("Error: debes ingresar un número entero.")