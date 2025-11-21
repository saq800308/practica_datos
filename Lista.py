#importa archivos necesarios
from Persona import Persona
from typing import List

#se crea la clase Lista
class Lista(Persona):
    #se define las caracteristicas de Lista
    def __init__(self,listapersona):
        self.listapersona=listapersona
    
    def agregar(self,lista):
        #pide la informacion 
        nombre=input("\ningresa nombre: ")
        ciudad=input("ingresa ciudad: ")    
        documento=input("ingresa numero de documento: ")
        while True:
            edad=input("ingresa edad: ")
            if edad.isdigit():
                edad=int(edad)
                if edad>0:
                    break
            else:
                print("edad no valida")
        #verifica que listapersona no este vacio
        if self.listapersona:
            #si esta llena verifica que el documento no este repetido 
            while any(p.documento == documento for p in lista):
                documento=input("El documento ya existe, ingrese otro: ")
                pe=Persona(documento,nombre,edad,ciudad)             
            return lista.append(pe)
        #si esta vacia solo los agrega     
        else:
            pe=Persona(documento,nombre,edad,ciudad)
            return lista.append(pe)

    #se crea la funcion de mostrar todas las personas de la lista 
    def mostrarlista(self)->Persona:
        x=0
        if self.listapersona:#verifica que lista no este vacia 
            for persona in self.listapersona:
                x+=1
                print(x,". Nombre:",persona.nombre," edad:",persona.edad," N. documento:",persona.documento," ciudad:",persona.ciudad)
        else:
            print("No hay personas en la lista")

    #funcion para consultar personas consultar persona 
    def consultar(self)->Persona:
        if self.listapersona:#verifica que la lista no este vacia
            for persona in self.listapersona:#recorrela lista 
                buscardor=input("ingresa nombre o documento")#ingresa el documento o nombre a buscar 
                if persona.nombre == buscardor:
                    print("Nonbre:",persona.nombre," edad:",persona.edad," N. documento:",persona.documento," ciudad:",persona.ciudad)
                elif persona.documento == buscardor:
                    print("Nonbre:",persona.nombre," edad:",persona.edad," N. documento:",persona.documento," ciudad:",persona.ciudad)  
                else:
                    print("no se encontro persona")
        else:#funcion si la lista esta vacia 
            print("la lista esta vacia")
    def borrar(self,lista): #funcion borrar para borrar un elemento de la lista
        docu=input("Ingrese el numero de documento de la persona que desea borrar: ")
        for i,lis in enumerate(lista): #for que enumera los objetos para borrarlos con mas facilidad i es el numero de objeto y lis seria el objeto
            if docu==lis.documento: #si el documento a buscaar coicide con el documento del objeto entonces
                del lista[i] #se borra el objeto
                print("Persona borrada.")
            else:
                print("No existe esa persona.")
    def modificar(self,lista): #modifica todos los daaatos de un documento
        docu=input("Ingrese el numero de documento de la persona que desea modificar: ")
        for lis in lista: #se hace un ciclo que recorre todos los objetos de la listaa
            if docu==lis.documento: #si el documento ingresdao coincide con el del objeto entonces
                lis.nombre=input("Ingrese el nuevo nombre: ") #aca se piden todos los daatos nuevos del objeto
                lis.edad=input("Ingrese la nueva edad: ")
                while lis.edad.isdigit()==False: #comprueb que laa edad sea un numero y no letras
                    lis.edad=input("Edad no es numero, ingrese de nuevo: ")
                lis.documento=input("Ingrese el nuevo documento: ")
                lis.ciudad=input("Ingrese la nueva ciudad: ")
                print("Persona modificada.")
            else:
                print("No existe esa persona.")