class NoHaySaldoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass

PRIMARIO = 0.5
PRECIO_TICKET = 70
DESACTIVADO = 0
ACTIVADO = 0

class Sube:
    def __init__(self):
        self.saldo = 1000
        self.grupo_beneficiario = None
        self.estado = "activado"

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == PRIMARIO:            #Cuando el grupo es primario se paga la mitad
            precio_ticket = PRECIO_TICKET * PRIMARIO        
            return precio_ticket                           # y se guarda el valor del rticket
        else:    
            precio_ticket = PRECIO_TICKET                  #Cuando no es primario 
            return precio_ticket                           #Se guarda el precio a pagar del ticket 
    
    def pagar_pasaje(self):
        if self.estado == "desactivado":
            raise UsuarioDesactivadoException()
        else:
            if self.saldo > self.obtener_precio_ticket():        #La funcion al hacer la verificacion retorna un valor u otro, el que retorne es lo que va a valer                                                                
                self.saldo -= self.obtener_precio_ticket()      # Si en cualquiera de los dos casos el valor del ticket a pagar es menor al saldo actual: se realiza el pago
               
            else:
                raise NoHaySaldoException()                     #En el caso de que no, se lanza la excepcion
            
    def cambiar_estado(self, estado):
        self.estado = estado
        if self.estado != ACTIVADO and self.estado != DESACTIVADO:
            raise EstadoNoExistenteException()
        
        
    
    
    
        
        
    