##http://localhost:3000/Pacientes
from flask import Flask, jsonify, request
from flask_cors import CORS
from Pacientes import Pacientes
from Doctores import Doctores
from Enfermeras import Enfermeras
from Medicamentos import Medicamentos
from Citas import Citas
from Carrito import Carrito
from Enfermedades import Enfermedades
import json

IngresarP = []

IngresarM=[]

IngresarD=[]

IngresarE=[]

IngresarCitas=[]

CompraCarrito=[]

IngresarEnfer=[]






xd = Flask(__name__)
CORS(xd) 

@xd.route('/Compra', methods=['GET'])
def MostrarCompra():
    global CompraCarrito
    Datos = []

    for i in CompraCarrito:
        objeto = {
            'Cantidad': i.getCantidad(),
            'Nombre': i.getNombre(),
            'Paciente': i.getPaciente()
        }
        Datos.append(objeto)    
    return(jsonify(Datos))


@xd.route('/enfermedad', methods=['POST'])
def Agregarenfermerdad():
    global IngresarEnfer
    v=False
    cantidad = request.json['Cantidad']
    nombre = request.json['Nombre']

    for i in range(len(IngresarEnfer)):
        if nombre== IngresarEnfer[i].getNombre():
            cant= int(IngresarEnfer[i].getCantidad())
            cant1=int(cantidad)
            tot=cant+cant1
            IngresarEnfer[i].setCantidad(tot)
            v=True
            return jsonify({'Mensaje':'Se agrego la compra'})
            
    
    if v==False:
        new=Enfermedades(cantidad,nombre)
        IngresarEnfer.append(new)
        return jsonify({'Mensaje':'Se agregaron los medicamentos'})



@xd.route('/enfermedad', methods=['GET'])
def Mostrarenfermerdad():
    global CompraCarrito
    Datos = []

    for i in IngresarEnfer:
        objeto = {
            'Cantidad': i.getCantidad(),
            'Nombre': i.getNombre()
        }
        Datos.append(objeto)    
    return(jsonify(Datos))


@xd.route('/Compra', methods=['POST'])
def AgregarCompra():
    global CompraCarrito
    v=False
    cantidad = request.json['Cantidad']
    nombre = request.json['Nombre']
    paciente = request.json['Paciente']
    for i in range(len(CompraCarrito)):
        if nombre== CompraCarrito[i].getNombre():
            cant= int(CompraCarrito[i].getCantidad())
            cant1=int(cantidad)
            tot=cant+cant1
            CompraCarrito[i].setCantidad(tot)
            v=True
            return jsonify({'Mensaje':'Se agrego la compra'})
            
    
    if v==False:
        new=Carrito(cantidad,nombre,paciente)
        CompraCarrito.append(new)
        return jsonify({'Mensaje':'Se agregaron los medicamentos'})



@xd.route('/C', methods=['GET'])
def MostrarCitas():
    global IngresarCitas
    Datos = []

    for i in IngresarCitas:
        objeto = {
            'IdPaciente': i.getIdp(),
            'NombreP': i.getNombrep(),
            'ApellidoP': i.getApellidop(),
            'Fecha': i.getFecha(),
            'Hora': i.getHora(),
            'Motivo': i.getMotivo(),
            'Estado': i.getEstado(),
            'Doctor': i.getDoctor(),
            'Iddoctor': i.getIddoctor()
        }
        Datos.append(objeto)    
    return(jsonify(Datos))

@xd.route('/C', methods=['POST'])
def AgregarCita():
    global IngresarCitas
    ip = request.json['IPaciente']
    nomp = request.json['NombreP']
    apep = request.json['ApellidoP']
    fe = request.json['Fecha']
    ho=request.json['Hora']
    mo=request.json['Motivo']
    es=request.json['Estado']
    dc=request.json['Doctor']
    idc=request.json['Iddoctor']

    ncita= Citas(ip,nomp,apep,fe,ho,mo,es,dc,idc)
    IngresarCitas.append(ncita)
    return jsonify({'Mensaje':'Cita creada',})


@xd.route('/C/<string:nombre>', methods=['PUT'])
def EstadoCita(nombre):
    global IngresarCitas
    for i in range(len(IngresarCitas)):
        if nombre == IngresarCitas[i].getIdp():
            IngresarCitas[i].setEstado(request.json['Estado'])
            IngresarCitas[i].setDoctor(request.json['Doctor'])
            IngresarCitas[i].setIddoctor(request.json['Iddoctor'])

            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})
  

@xd.route('/Me', methods=['GET'])
def MostrarMedicinas():
    global IngresarM
    Datos = []

    for i in IngresarM:
        objeto = {
            'Nombre': i.getNombre(),
            'Precio': i.getPrecio(),
            'Descripcion': i.getDescripcion(),
            'Cantidad': i.getCantidad(),
            'Codigo': i.getCodigo()
        }
        Datos.append(objeto)    
    return(jsonify(Datos))

##********************************************************************************************
@xd.route('/Me/<string:nombre>', methods=['GET'])
def Medicinax(nombre):
    global IngresarM
    

    for i in IngresarM:
        if i.getCodigo()==nombre:
            objeto = {
                'Nombre': i.getNombre(),
                'Precio': i.getPrecio(),
                'Descripcion': i.getDescripcion(),
                'Cantidad': i.getCantidad(),
                'Codigo': i.getCodigo()

            }               
            return(jsonify(objeto)) 

##*********************************************************************************************
@xd.route('/Me', methods=['POST'])
def AgregarMedicina():
    global IngresarM
    v=False
    nombre = request.json['Nombre']
    apellido = request.json['Precio']
    fecha = request.json['Descripcion']
    sexo = request.json['Cantidad']
    codigo=request.json['Codigo']
    for i in range(len(IngresarM)):
        if nombre== IngresarM[i].getNombre():
            cant= int(IngresarM[i].getCantidad())
            cant1=int(sexo)
            tot=cant+cant1
            IngresarM[i].setCantidas(str(tot))
            v=True
            
    
    if v==False:
        new=Medicamentos(nombre,apellido,fecha,sexo,codigo)
        IngresarM.append(new)
    return jsonify({'Mensaje':'Se agregaron los medicamentos'})

##*************************************************************************************************
@xd.route('/Me/<string:nombre>', methods=['DELETE'])
def EliminarMedicina(nombre):
    global IngresarM
    for i in range(len(IngresarM)):
        if nombre == IngresarM[i].getCodigo():
            del IngresarM[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})    
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})


@xd.route('/Me/<string:nombre>', methods=['PUT'])
def ActualizarMedicina(nombre):
    global IngresarM
    for i in range(len(IngresarM)):
        if nombre == IngresarM[i].getCodigo():
            IngresarM[i].setNombre(request.json['Nombre'])
            IngresarM[i].setPrecio(request.json['Precio'])
            IngresarM[i].setDescripcion(request.json['Descripcion'])
            IngresarM[i].setCantidas(request.json['Cantidad'])

 
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})


@xd.route('/MeCa/<string:nombre>', methods=['PUT'])
def ActualizarMedicinaCantidad(nombre):
    global IngresarM
    cantidad = request.json['Cantidad']
    for i in range(len(IngresarM)):
        if nombre == IngresarM[i].getCodigo():
            cant= int(IngresarM[i].getCantidad())
            cant1=int(cantidad)
            tot=cant-cant1
            IngresarM[i].setCantidas(str(tot))
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})
##***************************************************************************************************

@xd.route('/En', methods=['GET'])
def MostrarEnfermeras():
    global IngresarE
    Datos = []

    for i in IngresarE:
        objeto = {
            'Nombre': i.getNombre(),
            'Apellido': i.getApellido(),
            'Fecha': i.getFecha(),
            'Sexo': i.getSexo(),
            'NombreUsuario': i.getNombreU(),
            'Contrasena': i.getContra(),
            'Telefono': i.getTel()
        }
        Datos.append(objeto)    
    return(jsonify(Datos))



@xd.route('/Doc', methods=['GET'])
def MostrarDoctores():
    global IngresarD
    Datos1 = []

    for i in IngresarD:
        objeto1 = {
            'Nombre': i.getNombre(),
            'Apellido': i.getApellido(),
            'Fecha': i.getFecha(),
            'Sexo': i.getSexo(),
            'NombreUsuario': i.getNombreU(),
            'Contrasena': i.getContra(),
            'Especialidad': i.getEspecialidad(),
            'Telefono': i.getTel()
        }
        Datos1.append(objeto1)    
    return(jsonify(Datos1))


#------------------------------------------------------------------------------------
#*************************PACIENTES************************************************
#------------------------------------------------------------------------------------
@xd.route('/Pacientes', methods=['GET'])
def MostrarPacientes():
    global IngresarP
    Datos = []

    for i in IngresarP:
        objeto = {
            'Nombre': i.getNombre(),
            'Apellido': i.getApellido(),
            'Fecha': i.getFecha(),
            'Sexo': i.getSexo(),
            'NombreUsuario': i.getNombreU(),
            'Contrasena': i.getContra(),
            'Especialidad': i.getEspecialidad(),
            'Telefono': i.getTel(),
            'Tipo': i.getPer(),
        }
        Datos.append(objeto)    
    return(jsonify(Datos))


#-------------------------------------------------------------------------------
@xd.route('/Pacientes/<string:nombre>', methods=['GET'])
def Pacientex(nombre):
    global IngresarP

    for i in IngresarP:

        if i.getNombreU()==nombre:
            objeto = {
                'Nombre': i.getNombre(),
                'Apellido': i.getApellido(),
                'Fecha': i.getFecha(),
                'Sexo': i.getSexo(),
                'NombreUsuario': i.getNombreU(),
                'Contrasena': i.getContra(),
                'Especialidad': i.getEspecialidad(),
                'Telefono': i.getTel(),
                'Tipo': i.getPer(),
            } 
            return(jsonify(objeto))

#------------------------------------------------------------------------------------
@xd.route('/Pacientes', methods=['POST'])
def AgregarPacientes():
    global IngresarP
    v=False
    nombre = request.json['Nombre']
    apellido = request.json['Apellido']
    fecha = request.json['Fecha']
    sexo = request.json['Sexo']
    nombreu = request.json['NombreU']
    contra = request.json['Contraseña']
    espe =request.json['Especialidad']
    tel = request.json['Teléfono']    
    tipo= request.json['Tipo']    
    for i in range(len(IngresarP)):
        if nombreu== IngresarP[i].getNombreU():
            v=True
            return jsonify({'Mensaje':'El nombre de usuario ya existe'})

    if v==False:
        nuevop = Pacientes(nombre,apellido, fecha, sexo, nombreu, contra, espe,tel,tipo)
        IngresarP.append(nuevop)
        return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})  

#------------------------------------------------------------------------------------
@xd.route('/Pacientes/<string:nombre>', methods=['PUT'])
def ActualizarPaciente(nombre):
    global IngresarP
    for i in range(len(IngresarP)):
        if nombre == IngresarP[i].getNombreU():
            IngresarP[i].setNombre(request.json['Nombre'])
            IngresarP[i].setApellido(request.json['Apellido'])
            IngresarP[i].setFecha(request.json['Fecha'])
            IngresarP[i].setSexo(request.json['Sexo'])
            IngresarP[i].setNombreU(request.json['NombreU'])
            IngresarP[i].setContra(request.json['Contraseña'])
            IngresarP[i].setEspecialidad(request.json['Especialidad'])
            IngresarP[i].setTel(request.json['Teléfono'])
            
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})      


@xd.route('/Pacientes1/<string:nombre>', methods=['PUT'])
def ActualizarPacienteSinRepetir(nombre):
    global IngresarP
    nombreu = request.json['NombreU']
    v=False
    
    for i in range(len(IngresarP)):
        if nombre == IngresarP[i].getNombreU():
            for j in range(len(IngresarP)):
                if nombreu==IngresarP[j].getNombreU():   
                        v=True                  
                        return jsonify({'Mensaje':'El Nombre de Usuario ya existe, intente otro'})
            if v== False:
                print(nombreu)
                print(IngresarP[i].getNombreU())
                IngresarP[i].setNombre(request.json['Nombre'])
                IngresarP[i].setApellido(request.json['Apellido'])
                IngresarP[i].setFecha(request.json['Fecha'])
                IngresarP[i].setSexo(request.json['Sexo'])
                IngresarP[i].setNombreU(request.json['NombreU'])
                IngresarP[i].setContra(request.json['Contraseña'])
                IngresarP[i].setEspecialidad(request.json['Especialidad'])
                IngresarP[i].setTel(request.json['Teléfono'])
                return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

#------------------------------------------------------------------------------------
@xd.route('/Pacientes/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    global IngresarP
    for i in range(len(IngresarP)):
        if nombre == IngresarP[i].getNombreU():
            del IngresarP[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})    
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})



if __name__ == "__main__":
    xd.run(host="0.0.0.0", port=3000, debug=True)