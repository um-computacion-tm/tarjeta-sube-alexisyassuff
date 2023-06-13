class Descubiertosuperado(Exception):
    pass
class CuentaCoriente():
    def __init__(self):
        self.saldo = 0
    def deposito(self, monto):
        self.saldo += monto
    def retiro(self, monto):
        if monto > self.saldo + 1000: 
            raise Descubiertosuperado()
        self.saldo -= monto
