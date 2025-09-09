# Ejercicio 02 ---------------------------------------
#   Escribe un programa que intente sumar un número y una cadena. 
#   Si se produce un error de tipo, captura la excepción TypeError 
#   y muestra un mensaje de error al usuario.
# ----------------------------------------------------


def  suma(numero1,numero2):
   try:
       resultado = numero1 +  numero2
       print(f"El resultado de la suma es:", resultado)

   except TypeError:
     print(f"Ha ocurrido un error con los tipos de datos")



#  version con datos correctos
print("Ejecucion con datos correctos")
suma(100,15)

print("-----------------------------------")

#  version con datos incorrectos
print("Ejecucion con datos incorrectos")
suma(100,'z')

