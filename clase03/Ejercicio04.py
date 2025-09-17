# Ejercicio 04 ---------------------------------------
#   Calcular el promedio de una lista de números usando args 
#   y un operador ternario
# ----------------------------------------------------
def promedio(*args):
    return sum(args) / len(args) if len(args) > 0 else "Error: no se pasaron números"

numeros = []
print("Ingrese números (escriba 'fin' para terminar):")

while True:
    entrada = input("> ")
    if entrada.lower() == "fin":
        break
    try:
        numeros.append(int(entrada))
    except ValueError:
        print("Error: ingrese un número válido o 'fin' para salir.")

print(f"El promedio es:", promedio(*numeros))
