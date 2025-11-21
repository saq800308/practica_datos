#importacion de archivos nesesarios 
from Persona import Persona
from Lista import Lista

lista=[]#creamos la lista donde van a venir las personas

#creamos el menu
while True:
    print("\nMENU")
    print("1. Agreagar persona")
    print("2. ver lista")
    print("3. Consultar persona")
    print("o. Salir")

    opcion=input("elige la opcion:")#variable para eligir la opccion

    l=Lista(lista)#llamamos la intancia de Lista
    
    #pedimos los datos para crear una persona en la lista
    if opcion=="1":
        l.agregar(lista)
        menu=input("Enter para continuar")
    
    #muestar todas las personas de la lista
    elif opcion=="2":
        l.mostrarlista()
        menu=input("Enter para continuar")

    #consulta una personade la lista
    elif opcion=="3":
        l.consultar()
        menu=input("Enter para continuar")

    #se sale del bucle
    elif opcion=="0":
        break
    
    #este elemento aparese si no se reconoce la opcion
    else:
        print("opcion no valida vuelve a intentarlo")
        menu=input("Enter para continuar")
