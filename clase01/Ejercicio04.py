# Ejercicio 04 ---------------------------------------
# Dado un conjunto A, escribe un programa en Python que imprima
# si el conjunto A es un subconjunto de otro conjunto B.
#
# Resolucion con metodo issubset
# ----------------------------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

if A.issubset(B):
    print("Ejercicio 04 - A es subconjunto de B")
else:
    print("Ejercicio 04 - A no es subconjunto de B")


