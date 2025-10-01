# caja de ahorro
from cb import CuentaBancaria

class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
            
        self._tasainteres = 0.001
    
    def calcular_interes(self):
    #    return self._saldo + self._tasainteres
      return self._tasainteres
        
    def obtener_saldo(self):
        saldo_actual = super().obtener_saldo()
        print(f"Saldo antes de calcular interés: {saldo_actual}")
        interes = self.calcular_interes()
        self._saldo = saldo_actual + interes
        print(f"Saldo despues de calcular interés: {self._saldo}")
        return saldo_actual + interes

    def depositar(self, monto):
        if monto > 0:
            self._saldo = self._saldo + monto
            print(f"Se depositaron {monto}. Saldo antes de interés: {self._saldo}")
            self._saldo =  self._saldo + self.calcular_interes()
            print(f"Saldo despues de calcular interés: {self._saldo}")
        else:
            print("El monto a depositar debe ser mayor a 0")

    def extraer(self, monto):
        if monto <= self._saldo:
            self._saldo = self._saldo - monto
            print(f"Se extrajeron {monto}. Saldo antes de interés: {self._saldo}")
            self._saldo = self._saldo + self.calcular_interes()
            print(f"Saldo despues de calcular interés: {self._saldo}")
        
        else:
            print("Fondos insuficientes")