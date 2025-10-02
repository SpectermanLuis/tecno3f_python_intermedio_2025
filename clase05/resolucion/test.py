from cb import CuentaBancaria

from ca import CajaDeAhorro

# prueba de ejemplo 

ca1 = CajaDeAhorro("Luis",333333,'1990/02/03',15000.00)

print(ca1.obtener_saldo())

ca1.depositar(1000)

ca1.extraer(500)