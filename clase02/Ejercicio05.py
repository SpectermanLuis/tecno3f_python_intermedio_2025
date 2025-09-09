# Ejercicio 05 ---------------------------------------
#  Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#  captura la excepción ZeroDivisionError. 
#  Si el primer número es un número no válido, captura la excepción ValueError.
#  En cualquier caso, muestra un mensaje de error al usuario.
# ----------------------------------------------------


try:
    numerador = float(input("Ingrese el primer número: "))
except ValueError:
    print("Error: el primer número no es válido.")
    exit()   

try:
    divisor = float(input("Ingrese el segundo número: "))
except ValueError:
    print("Error: el segundo número no es válido.")
    exit()

try:
    resultado = numerador / divisor
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print(f"Error: Divisor es Cero .No se puede realizar la division.")
