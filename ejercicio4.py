def generar_tabla(base):
    print(f"\nTabla de multiplicar del {base}")
    for i in range(1,11):
        print(f"{i} x {base} = {i*base}")
print("--- Generador de Tablas de Multiplicar ---")

while True:
    numero = int(input("Ingrese el numero base (0. Salir): "))
    
    if numero == 0:
        print("Saliendo...")
        break
    generar_tabla(numero)