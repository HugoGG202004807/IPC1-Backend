class Citas: 
    def __init__(self,idp,nombrep,apellidop,fecha, hora, motivo, estado,doctor,iddoctor):
        self.idp=idp
        self.nombrep = nombrep
        self.apellidop = apellidop
        self.fecha = fecha
        self.hora=hora
        self.motivo=motivo
        self.estado=estado
        self.doctor=doctor
        self.iddoctor=iddoctor
        
#-----------------------------------------------------
    def getIdp(self):
        return self.idp

    def getNombrep(self):
        return self.nombrep
    
    def getApellidop(self):
        return self.apellidop

    def getFecha(self):
        return self.fecha
    
    def getHora(self):
        return self.hora

    def getMotivo(self):
        return self.motivo
    
    def getEstado(self):
        return self.estado

    def getDoctor(self):
        return self.doctor
    
    def getIddoctor(self):
        return self.iddoctor
    
   

#-----------------------------------------------------
    def setEstado(self, estado):
        self.estado = estado

    def setDoctor(self, doctor):
        self.doctor = doctor 

    def setIddoctor(self, iddoctor):
        self.iddoctor = iddoctor
    
    
