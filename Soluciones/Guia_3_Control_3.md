Guía de ejercicios

Estudio personal: [https://www.w3schools.com/python/default.asp](https://www.w3schools.com/python/default.asp)

Soluciones: [https://github.com/Brojass05/Solucionario-Guia-Control-3](https://github.com/Brojass05/Solucionario-Guia-Control-3)

**_Ejercicio 1: Calculadora Básica (+) (-) (\*) (/) (%) (\*\*) (//) (porcentaje)_**

Construye una calculadora básica interactiva basada en funciones y un bucle de ejecución continua. El programa debe cumplir con los siguientes requerimientos:

- **Estructura Modular:** Define funciones independientes para cada operación matemática básica: suma, resta, multiplicación, división, módulo, potencia, división entera y cálculo de porcentaje.
- **Flujo de Entrada:** En cada iteración del menú, solicita al usuario primero el ingreso de dos números de tipo flotante (uno después del otro) y, a continuación, solicita el operador que se usará mediante una cadena de texto
- **Opciones Soportadas:** El programa debe reconocer los siguientes operadores mediante una estructura de control adecuada (match-case):
    - \+ para suma.
    - \- para resta.
    - \* para multiplicación.
    - / para división.
    - mod para el módulo.
    - \*\* para la potencia.
    - // para la división entera.
    - % para el porcentaje.
- **Validación de Errores:** Para las operaciones de división, módulo y división entera, verifica que el segundo número sea distinto de cero. Si es cero, la función correspondiente debe retornar el mensaje "No se puede dividir por 0".
- **Condición de Salida:** Si el usuario ingresa un operador fuera de las opciones válidas, muestra el mensaje "Opcion no valida, saliendo..." y finaliza la ejecución del programa.

**_Ejercicio 2: Cajero automático_**

- Crea una función principal.
- Inicializa una variable saldo con un valor de $50000.
- Implementa un ciclo while que mantenga activo el menú principal del cajero.
- **Opción 1:** Depositar (solicita un monto y lo suma al saldo actual). Se debe validar que el monto a depositar sea mayor a 0 y mostrar un mensaje “No puede ingresar numeros negativos o 0”
- **Opción 2:** Retirar (solicita un monto a restar, pero debe validar estrictamente que la cantidad ingresada no exceda el saldo disponible).
- **Opción 3:** Salir del programa.

**_Ejercicio 3: Filtro Dinámico de Pares e Impares_**

- Define dos listas vacías al inicio del programa: pares = \[\] e impares = \[\].
- Inicia un ciclo while que solicite números al usuario de forma continua.
- Establece que, si el usuario ingresa un "0", el ciclo se detiene.
- Evalúa cada número ingresado: si cumple con num % 2 == 0, agrégalo a la lista de pares usando el método. append().
- Si no cumple la condición, utiliza. append() para agregarlo a la lista de impares.
- Una vez que el ciclo termine, imprime el contenido de ambas listas iterándolas con un ciclo for.

**_Ejercicio 4: Función de tablas de multiplicar_**

- Solicita al usuario que ingrese un número base de tipo entero (int).
- Construye una función que reciba dicho número y utilice un ciclo for i in range(1, 11).
- Dentro del ciclo, calcula e imprime el resultado de la multiplicación entre el número base y el iterador actual para generar la tabla completa.

**_Ejercicio 5: Registro de Tiempos de Atletismo_**

**Contexto:** Un entrenador quiere registrar los tiempos (en minutos) que tardan sus atletas en completar una carrera de 10 km.

Requerimientos: Dentro de una función principal, inicializa una lista vacía para los tiempos y un menú controlado por un ciclo while:

1. **Registrar tiempo:** Solicita un tiempo en minutos (float). Usa un ciclo while para obligar a que el tiempo ingresado sea mayor a 10.0 y menor a 120.0. Agrégalo a la lista.
2. **Listar tiempos:** Recorre la lista con un ciclo for e imprime cada tiempo.
3. **Calcular tiempo promedio:** Usa un for y un acumulador para sumar los tiempos. Divide por la cantidad de registros. Evalúa el promedio con if-elif-else:
    - Promedio < 40.0: "Rendimiento de Élite"
    - Promedio entre 40.0 y 60.0 (inclusive): "Rendimiento Avanzado"
    - Promedio > 60.0: "Rendimiento Principiante"
4. **Contar tiempos rápidos:** Usa un for y un contador para registrar cuántos atletas hicieron un tiempo menor a 50.0 minutos.
5. **Salir:** Cierra el menú.
