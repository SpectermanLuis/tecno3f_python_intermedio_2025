# Ejercicio 04 ---------------------------------------
#   Escribe un programa que intente abrir un archivo que no existe. 
#   Si se produce una excepción FileNotFoundError, captura la excepción 
#   y muestra un mensaje de error al usuario. 
#   Sin embargo, también intenta crear el archivo si no existe
# ----------------------------------------------------

nombre_archivo = "prueba_ejercicio_04.txt"

try:
    # abrir el supuesto archivo existente como lectura
    # y mostrar el contenido 
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    # Archivo no existe, mensaje de error y creacion del archivo
    print(f"Error: el archivo '{nombre_archivo}' no existe.")
    print("Creando el archivo...")

    with open(nombre_archivo, "w") as archivo:
        archivo.write("Este es un archivo nuevo.\n")
        print(f"El archivo '{nombre_archivo}' ha sido creado correctamente.")
