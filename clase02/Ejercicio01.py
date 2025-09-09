# Ejercicio 01 ---------------------------------------
#   Escribe un programa que intente dividir dos números.
#   Si el segundo número es cero, captura la excepción ZeroDivisionError
#   y muestra un mensaje de error al usuario.
# ----------------------------------------------------


def  division(numerador,divisor):
   try:
       resultado = numerador / divisor
       print("El resultado de la división es:", resultado)

   except ZeroDivisionError:
       print("Error: Divisor es Cero .No se puede realizar la division.")


#  version con datos correctos
print("Ejecucion con datos correctos")
division(100,15)

print("-----------------------------------")

#  version con datos incorrectos
print("Ejecucion con datos incorrectos")
division(100,0)
