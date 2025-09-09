# Ejercicio 03 ---------------------------------------
#   Escribe un programa que intente acceder a una clave que 
#   no existe en un diccionario. Si se produce una excepción KeyError,
#   captura la excepción y muestra un mensaje de error al usuario.
# ----------------------------------------------------

# Diccionario para prueba
persona = {
    "nombre": "Luis",
    "edad": 63,
    "pais": "Argentina"
}


clave = input("Ingresar la clave que desea consultar: ")

try:
    valor = persona[clave]
    print(f"El valor de '{clave}' es: {valor}")

except KeyError:
    print(f"Error: la clave '{clave}' no existe en el diccionario.")
