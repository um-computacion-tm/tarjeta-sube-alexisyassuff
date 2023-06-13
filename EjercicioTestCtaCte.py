import unittest
from EjercicioMetodoCtaCte import(CuentaCoriente, Descubiertosuperado)

class Test_Cuenta_Corriente(unittest.TestCase):

    def test_incio_en_cero(self):
        cuenta_corriente = CuentaCoriente()
        self.assertEqual(cuenta_corriente.saldo, 0)
    
    def test_deposito(self):
        cuenta_corriente = CuentaCoriente()
        cuenta_corriente.deposito(1000)
        self.assertEqual(cuenta_corriente.saldo, 1000)
    
    def test_retiro_con_saldo(self):
        cuenta_corriente = CuentaCoriente()
        cuenta_corriente.deposito(1000)
        cuenta_corriente.retiro(600)
        self.assertEqual(cuenta_corriente.saldo, 400)
    
    def test_retiro_sin_saldo_cumpliendo_limite_descubierto(self): #La cuenta corriente permite un descubierto
        cuenta_corriente = CuentaCoriente()
        cuenta_corriente.retiro(1000)
    
    def test_retiro_sin_saldo_cumpliendo_limite_descubierto(self): #La cuenta corriente permite un descubierto
        cuenta_corriente = CuentaCoriente()
        cuenta_corriente.retiro(1000)
        self.assertEqual(cuenta_corriente.saldo, -1000)

    def test_retiro_sin_cumplir_limite_descubierto(self): 
        cuenta_corriente = CuentaCoriente()
        with self.assertRaises(Descubiertosuperado ):
            cuenta_corriente.retiro(2000)
        self.assertEqual(cuenta_corriente.saldo, 0)

if __name__ == "__main__":
    unittest.main()