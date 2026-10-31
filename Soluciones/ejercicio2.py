def cajero_automatico():
    saldo = 50000
    while True:
        print("\n--- Cajero Automatico ---")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")

        opcion = int(input("Elige una opcion: "))
        
        match opcion:
            case 1:
                monto = float(input("Ingrese monto a depositar: "))
                if monto > 0:
                    saldo += monto
                    print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
                else:
                    print("No puede ingresar numeros negativos o 0")
            case 2:
                monto = float(input("Ingrese monto a retirar: "))
                if monto <= saldo:
                    saldo -= monto
                    print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
                else:
                    print("Error: saldo insuficiente")
            case 3:
                print("Saliendo del cajero...")
                break
            case _:
                print("Opcion no valida.")

cajero_automatico()