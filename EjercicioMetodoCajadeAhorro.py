class NoHaySaldo(Exception):
    pass
class CajadeAhorro():
    def __init__(self):
        self.saldo = 0 
    def deposito(self, monto):
        self.saldo += monto
    def retiro(self, monto):
        if self.saldo < monto:
            raise NoHaySaldo()
        self.saldo -= monto

