class Enfermedades:   
    def __init__(self,cantidad,nombre):
        self.cantidad=cantidad
        self.nombre=nombre
     
#-----------------------------------------------------
    def getCantidad(self):
        return self.cantidad
    
    def getNombre(self):
        return self.nombre

   

#-----------------------------------------------------
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setCantidad(self, cantidad):
        self.cantidad=cantidad