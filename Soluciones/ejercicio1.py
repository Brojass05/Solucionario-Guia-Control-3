def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2 != 0:
        return num1/num2
    else:
        return "No se puede dividir por 0"
def modulo(num1,num2):
    if num2 != 0:
        return num1%num2
    else:
        return "No se puede dividir por 0"
def potencia(num1,num2):
    return num1**num2
def division_entera(num1,num2):
    if num2 != 0:
        return num1//num2
    else:
        return "No se puede dividir por 0"
def porcentaje(num1,num2):
    return  (num1*num2)/100

def calculadora():
    while True:
        print("\n --- Calculadora ---")
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        opcion = input("Operacion((+) (-) (*) (/) (mod) (**) (//) (%) (Otro para salir)): ")
        

        match opcion:
            
            case '+':
                resultado = suma(num1,num2)
            case '-':
                resultado = resta(num1,num2)
            case '*':
                resultado = multiplicacion(num1,num2)
            case '/':
                resultado = division(num1,num2)
            case 'mod':
                resultado = modulo(num1,num2)
            case '**':
                resultado = potencia(num1,num2)
            case '//':
                resultado = division_entera(num1,num2)
            case '%':
                resultado = porcentaje(num1,num2)
            case _:
                print("Opcion no valida, saliendo...")
                break
        
        print("Resultado: ",resultado)
                
            
calculadora()