def mostrar_menu_atletismo():
    print("\n--- Menu de Atletismo ---")
    print("1. Registrar tiempo")
    print("2. Listar tiempos")
    print("3. Calcular tiempo promedio")
    print("4. Contar tiempos rapidos")
    print("5. Salir")

def registrar_tiempo(lista_tiempos):
    tiempo = float(input("Ingrese el tiempo en minutos: "))
    while not (10.0 < tiempo < 120.0):
        print("Tiempo invalido. Debe ser mayor a 10.0 y menor a 120.0")
        tiempo = float(input("Ingrese el tiempo en minutos: "))
    lista_tiempos.append(tiempo)
    print("Tiempo registrado con exito!") 
def listar_tiempos(lista_tiempos):
    if not lista_tiempos:
        print("No hay tiempos registrados, debe registrar tiempos")
    else:
        print("\nTiempos Registrados: ")
        for t in lista_tiempos:
            print(f"- {t} min")
            
def calcular_promedio(lista_tiempos):
    if not lista_tiempos:
        print("No hay tiempos registrados, debe registrar tiempos")
    else:
        suma = 0
        for t in lista_tiempos:
            suma += t
        promedio = suma/len(lista_tiempos)
        print(f"Tiempo promedio: {promedio}")
        
        if promedio < 40.0:
            print("Rendimiento de elite")
        elif 40.0 < promedio < 60.0:
            print("Rendimiento Avanzado")
        else:
            print("Rendimiento Principiante")
            
def contar_tiempos_rapidos(lista_tiempos):
    if not lista_tiempos:
        print("No hay tiempos registrados, debe registrar tiempos")
    else:
        contador_tiempos = 0
        for t in lista_tiempos:
            if t<50.0:
                contador_tiempos+=1
        print(f"Cantidad de atletas con tiempo menor a 50.0 minutos: {contador_tiempos}")
    
def iniciar_registro_atletismo():
    tiempos = []
    while True:
        mostrar_menu_atletismo()
        opcion = int(input("Eliga una opcion: "))
        
        match opcion:
            case 1:
                registrar_tiempo(tiempos)
            case 2:
                listar_tiempos(tiempos)
            case 3:
                calcular_promedio(tiempos)
            case 4:
                contar_tiempos_rapidos(tiempos)
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida")
                
            
iniciar_registro_atletismo()