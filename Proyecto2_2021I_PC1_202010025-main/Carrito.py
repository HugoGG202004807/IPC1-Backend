
class Carrito: 
    def __init__(self,cantidad,nombre, paciente):
        self.cantidad=cantidad
        self.nombre=nombre
        self.paciente=paciente       
#-----------------------------------------------------
    def getCantidad(self):
        return self.cantidad
    
    def getNombre(self):
        return self.nombre
    
    def getPaciente(self):
        return self.paciente
    
   

#-----------------------------------------------------
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPaciente(self, precio):
        self.paciente = paciente
    
    def setCantidad(self, cantidad):
        self.cantidad=cantidad
    

