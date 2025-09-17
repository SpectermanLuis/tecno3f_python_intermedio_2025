# Ejercicio 05 ---------------------------------------
#   Imprimir un mensaje de error si no se pasan 
#   suficientes argumentos
# ----------------------------------------------------
# Se asume que por lo menos deberia venir un argumento
def verificar_argumentos(*args):
    return "Correcto: se pasó al menos un argumento" if len(args) >= 1 else "Error: no se pasaron argumentos"

print(verificar_argumentos())          
print(verificar_argumentos(10))        
print(verificar_argumentos(10, 20))    
print(verificar_argumentos("hola"))    
