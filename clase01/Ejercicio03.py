# Ejercicio 03 ---------------------------------------
# Dados dos conjuntos A y B, escribe un programa en Python que 
# imprima los elementos que se encuentran en A o en B, 
# pero no en ambos. 
#
# Resolucion con diferencia simetrica
# ----------------------------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# version 1 - leido en manual
print("Ejercicio 03 - Diferencia simétrica - version 1:", A ^ B)
print("------------------------------------------------------------------")
# version 2 - segun dado en clase
print("Ejercicio 03 - Diferencia simétrica - version 2:", A.symmetric_difference(B))

