
class Medicamentos: 
    def __init__(self,nombre,precio, descripcion, cantidad,codigo):
        self.nombre = nombre
        self.precio = precio
        self.descripcion=descripcion
        self.cantidad=cantidad
        self.codigo=codigo
        
#-----------------------------------------------------
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio

    def getDescripcion(self):
        return self.descripcion
    
    def getCantidad(self):
        return self.cantidad
    
    def getCodigo(self):
        return self.codigo
    
   

#-----------------------------------------------------
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPrecio(self, precio):
        self.precio = precio
    

    def setDescripcion(self, descripcion):
        self.descripcion=descripcion
    
    def setCantidas(self, cantidad):
        self.cantidad=cantidad
    

