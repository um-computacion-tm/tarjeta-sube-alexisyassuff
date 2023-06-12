class NoHayMonedaException(Exception):
    pass
class NoHayAguaException(Exception):
    pass
class NoHayLecheException(Exception):
    pass

class MaquinaCafe:
    def __init__(self): 
        self.vasos = 0
        self.cafe = 0
        self.leche = 0
        self.agua = 0
        self.monedas = 0
    
    def hacer_cafe_solo(self):
        self.vasos -= 1
        self.cafe -= 50
        self.agua -= 100
        self.monedas -= 1
        self.leche -= 0
    
    def hacer_cafe_solo(self):
        if self.monedas == 0:
            raise NoHayMonedaException()
        self.vasos -= 1
        self.cafe -= 50
        self.agua -= 100
        self.monedas -= 1
        self.leche -= 0
    
    def hacer_cafe_solo_sin_agua(self):
        if self.agua < 100:
            raise NoHayAguaException()
        self.vasos -= 1
        self.cafe -= 50
        self.agua -= 100
        self.monedas -= 1
        self.leche -= 0
    
    def hacer_cafe_con_leche_sin_leche(self):
        if self.leche == 0:
            raise NoHayLecheException()
        self.vasos -= 0
        self.cafe -= 0
        self.agua -= 0
        self.monedas -= 0
        self.leche -= 0