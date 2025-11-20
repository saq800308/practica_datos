#importa archivos necesarios
from Persona import Persona
from typing import List

#se crea la clase Lista

class Lista(Persona):
    #se define las caracteristicas de Lista
    def __init__(self,listapersona):
        self.listapersona=listapersona
    
    #def agregar(self,documento):
        #nombre=input("\ningresa nombre: ")
        #ciudad=input("ingresa ciudad: ")
        #documento=input("ingresa numero de documento: ")
        #edad=int(input("ingresa edad: "))
        #pe=Persona(documento,nombre,edad,ciudad)
        #for persona in self.listapersona:
            #if persona.documento != documento:
                #return pe=Persona(documento,nombre,edad,ciudad)
            #else:
                #print("esta persona ya existe")

    #se crea la funcion de mostrarlista 
    def mostrarlista(self)->Persona:
        x=0
        for persona in self.listapersona:
            x+=1
            print(x,". Nonbre:",persona.nombre," edad:",persona.edad," N. documento:",persona.documento," ciudad:",persona.ciudad)

    def consultar(self)->Persona:
        for persona in self.listapersona:
            buscardor=input("ingresa nombre o documento")
            if persona.nombre == buscardor:
                print("Nonbre:",persona.nombre," edad:",persona.edad," N. documento:",persona.documento," ciudad:",persona.ciudad)
            elif persona.documento == buscardor:
                print("Nonbre:",persona.nombre," edad:",persona.edad," N. documento:",persona.documento," ciudad:",persona.ciudad)  
            else:
                print("no se encontro persona")