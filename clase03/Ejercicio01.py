# Ejercicio 01 ---------------------------------------
#   Calcular el mayor de dos números ingresados por 
#   teclado usando un operador ternario
# ----------------------------------------------------

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

mayor = numero1 if numero1 > numero2 else numero2
print(f"El mayor es: {mayor}")
