def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def opcion_primos():
    entrada = input("Ingresa un número entero: ").strip()
    try:
        n = int(entrada)
        if es_primo(n):
            print(f"{n} es primo.")
        else:
            print(f"{n} no es primo.")
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")