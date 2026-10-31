pares = []
impares = []

while True:
    num = int(input("Ingrese un numero (0. para salir): "))
    if num == 0:
        break
    elif num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("\n--- Resultados ---")
print("Pares: ")
for p in pares:
    print(p)

print("Impares: ")
for i in impares:
    print(i)

