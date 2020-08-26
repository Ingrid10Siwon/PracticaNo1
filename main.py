import sys
import json
import Carga

Carga.readJson()






while True:
    print("                                      ")
    print("**************** Menú ****************")
    print("1. Cargar ")
    print("2. Seleccionar ")
    print("3. Maximo ")
    print("4. Minimo ")
    print("5. Suma ")
    print("6. Cuenta ")
    print("7. Reportar ")
    print("8. Salir")
    print("***************************************")
    opcion = int(input("Seleccione una opción: "))


    if (opcion == 1):
        readJson()

        pass
        
    if (opcion == 2):
        pass
    if (opcion == 3):
        pass
    if (opcion == 4):
        pass
    if (opcion == 5):
        pass
    if (opcion == 6):
        pass
    if (opcion == 7):
        pass

    if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 6 and opcion != 7:
        print("Salir, hasta luego")
        sys.exit()
        break


def cargaArchivo(cadena):
     print("Carga de archivo, ingrese la ruta del archivo")
     cadena = input("Ingrese la rute del archivo: ")
        

def readJson():
    file = open('archivo.json')
    data = json.load(file)
    file.close()
    print(data)
    return data

dict=readJson()
for element in dict:
    print(element)


        