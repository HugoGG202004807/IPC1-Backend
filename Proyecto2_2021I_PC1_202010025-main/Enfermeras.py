
class Enfermeras: 
    def __init__(self,nombre,apellido, fecha, sexo, nombreu, contra, tel):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha=fecha
        self.sexo=sexo
        self.nombreu=nombreu
        self.contra=contra
        self.tel=tel
#-----------------------------------------------------
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getFecha(self):
        return self.fecha
    
    def getSexo(self):
        return self.sexo
    
    def getNombreU(self):
        return self.nombreu

    def getContra(self):
        return self.contra

    def getTel(self):
        return self.tel

#-----------------------------------------------------
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    

    def setFecha(self, fecha):
        self.fecha=fecha
    
    def setSexo(self, sexo):
        self.sexo=sexo
    
    def setNombreU(self, nombreu):
        self.nombreu=nombreu

    def setContra(self, contra):
        self.contra=contra

    def setTel(self, tel):
        self.tel=tel

