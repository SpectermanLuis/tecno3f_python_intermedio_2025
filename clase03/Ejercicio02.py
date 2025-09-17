# Ejercicio 02---------------------------------------
#   Buscar una palabra en una lista ingresada por teclado 
#   usando args y un operador ternario
# ----------------------------------------------------

def buscar_palabra(palabra, *args):
    return "Encontrada" if palabra in args else "No encontrada"

lista_palabras = []
while True:
    palabra = input("Ingrese una palabra (o 'fin' para terminar): ")
    if palabra.lower() == "fin":
        break
    lista_palabras.append(palabra)

print("Lista de palabras:", lista_palabras)


palabra_a_buscar = input("Ingrese la palabra a buscar: ")

print(buscar_palabra(palabra_a_buscar.lower(), *lista_palabras))