# redefinicion de clase CuentaCorriente 
# en base al original suministrado en el ejercicio
# por haber cambiado la clase padre CuentaBancaria
from cb import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0,limite_extraccion = 500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
        

def obtener_saldo(self):
        return super().obtener_saldo()

def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se depositaron {monto}. Saldo actual: {self._saldo}")
        else:
            print("El monto a depositar debe ser mayor a 0")

def extraer(self, monto):
        if monto <= self._saldo and monto <= self._limite_extraccion:
            self._saldo -= monto
            print(f"Se extrajeron {monto}. Saldo actual: {self._saldo}")
        else:
            if monto > self._limite_extraccion:
                print("Usted no puede extraer ese monto")
            else:
                print("Usted no posee saldo suficiente para realizar la operación")