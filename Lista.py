#importa archivos necesarios
from Persona import Persona
from typing import List

#se crea la clase Lista
#lista=[]#creamos la lista donde van a venir las personas

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
            edad=int(input("ingresa edad: "))
            if edad>0:
                break
            else:
                print("edad no valida")
        #verifica que listapersona no este vacio
        if self.listapersona:
            #si esta llena verifica que el documento no este repetido 
            for persona in self.listapersona:
                if persona.documento != documento:
                    pe=Persona(documento,nombre,edad,ciudad)
                    return lista.append(pe)
                else:
                    return print("esta persona ya existe")
        #si esta vacia solo los agrega       
        else:
            pe=Persona(documento,nombre,edad,ciudad)
            return lista.append(pe)

    #se crea la funcion de mostrar todas las personas de la lista 
    def mostrarlista(self)->Persona:
        x=0
        for persona in self.listapersona:
            x+=1
            print(x,". Nonbre:",persona.nombre," edad:",persona.edad," N. documento:",persona.documento," ciudad:",persona.ciudad)

    #funcion para consultar personas consultar persona 
    def consultar(self)->Persona:
        if self.listapersona:
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