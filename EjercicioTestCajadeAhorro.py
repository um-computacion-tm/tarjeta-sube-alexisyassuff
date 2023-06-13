import unittest
from EjercicioMetodoCajadeAhorro import (CajadeAhorro, NoHaySaldo)

class Test_CajadeaAhorro(unittest.TestCase):
    def  test_inicializacion_en_cero(self):
        caja_ahorro = CajadeAhorro()
        self.assertEqual(         
            caja_ahorro.saldo, 0)

    def test_deposito(self):
        caja_ahorro = CajadeAhorro()
        caja_ahorro.deposito(100)
        self.assertEqual(caja_ahorro.saldo, 100) 
    
    def test_retiro_correcto(self):
        caja_ahorro = CajadeAhorro()
        caja_ahorro.deposito(100)
        caja_ahorro.retiro(20)
        self.assertEqual(caja_ahorro.saldo, 80)
    
    def test_retiro_sin_saldo(self):
        caja_ahorro = CajadeAhorro()            
        with self.assertRaises(NoHaySaldo):
            caja_ahorro.retiro(110)
        self.assertEqual(caja_ahorro.saldo, 0)


if __name__ == '__main__':
    unittest.main()