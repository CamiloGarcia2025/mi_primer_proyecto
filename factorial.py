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
