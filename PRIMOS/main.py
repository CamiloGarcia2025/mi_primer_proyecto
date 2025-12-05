from PRIMOS.primos import opcion_primos

def mostrar_menu():
    print("1. Fibonacci")
    print("2. Factorial")
    print("3. Primos")
    print("4. Números perfectos")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            print("Función Fibonacci aún no integrada.")
        elif opcion == "2":
            print("Función Factorial aún no integrada.")
        elif opcion == "3":
            opcion_primos()
        elif opcion == "4":
            print("Función Números Perfectos aún no integrada.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
    