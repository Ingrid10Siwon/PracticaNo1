import sys
import json
import Carga
#import Seleccionar
import Cargar

print('--------------Bienvenido------------------------')
while True: 
    print("---------------------------------------------------------------------")
    print("Ingrese un comando") 
    opcion= input ("Comando: ")
    ##menu a entrar en cada una 
    
    if (opcion.casefold() == 'CARGAR'.casefold()):
        Carga.cargaArchivo()
        #cargar()
        
        pass 

    if opcion.casefold()=="SELECCIONAR".casefold():
        Carga.seleccionar()
        pass 
    if (opcion.casefold() == "Maximo".casefold()):
        Carga.maximo()
        pass
    if (opcion.casefold() == "MINIMO".casefold()):
        pass
    if (opcion.casefold() == "SUMA".casefold()):
        pass
    if (opcion.casefold() == "CUENTA".casefold()):
        Carga.listarArchivo()
        pass
    if (opcion.casefold() == "REPORTAR".casefold()):
        Carga.reporte()
        pass
    #else:
     #   sys.exit()
      #  pass
    if opcion.casefold() != 'CARGAR'.casefold() and opcion.casefold() != "SELECCIONAR".casefold() and opcion.casefold() != "Maximo".casefold() and opcion.casefold() != "SUMA".casefold() and opcion.casefold() != "CUENTA".casefold() and opcion.casefold() != "REPORTAR".casefold() and opcion.casefold() != "MINIMO".casefold():
        print("Salir, hasta luego")
        sys.exit()
        break       
    









