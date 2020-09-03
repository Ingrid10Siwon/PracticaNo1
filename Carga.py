import json
import Cargar 
import os
import sys
import webbrowser
from string import Template

global Lista
Lista = list()

class Archivo:
    texto=""
    #cantidad = ""

def cargaArchivo():
    a=Archivo()
    print("Ingrese el nombre del archivo ")
    ruta = input("CARGAR ")
    a.texto= ruta.split(", ")
    #----a.cantidad=  a.rut.split(", ")
    Lista.append(a.texto)
    posicion = len(a.texto)
    #print(posicion)
    print("Se cargaron todos los archivos")      
    #print(Lista)
    #posicion = len(a.cantidad)
    #print(Lista)
    #cont = 0
dict = Lista

def seleccionar():
    #print("Todos los archivos")
    sele = input("SELECCIONAR ")
    if sele.casefold() == '*'.casefold():
        for a in dict:
            cont = 0
            while cont < len(a):
                mando = a[cont]
                file = open(mando)
                data = json.load(file)
                file.close()
                print (data)
                cont = cont +1
            #return data        
##Primera condicion------------------------------------------------------------------------------------------  
    elif sele.casefold()=="nombre, edad".casefold() or "edad, nombre".casefold():
        res1= input("DONDE ")
        if res1.casefold()=="nombre".casefold():
            res=input("= ")
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["nombre"] == res:
                            print("Nombre          " , "Edad   ")
                            print( i["nombre"] ,"     ",  i["edad"])

        elif res1.casefold()=="edad".casefold():
            res2=int(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["edad"] == res2:
                            print("Nombre          " , "Edad     ")
                            print( i["nombre"] ,"     ",  i["edad"])

        elif res1.casefold()=="activo".casefold():
            res3=bool(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["activo"] == res3:
                            print("Nombre          " , "Edad     ")
                            print( i["nombre"] ,"     ",  i["edad"])

        elif res1.casefold()=="promedio".casefold():
            res4=float(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["promedio"] == res4:
                            print("Nombre          " , "Edad     ")
                            print( i["nombre"] ,"     ",  i["edad"])
   #*******+ 
    elif sele.casefold()=="nombre, activo".casefold() or "activo, nombre".casefold():
        res5= input("DONDE ")
        if res5.casefold()=="nombre".casefold():
            res6=input("= ")
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["nombre"] == res6:
                            print("este es diferente")
                            print("Nombre          " , "Activo   ")
                            print( i["nombre"] ,"     ",  i["activo"])
                    #cont = cont +1   
                    # 
        elif res5.casefold()=="edad".casefold():
            res7=int(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["edad"] == res7:
                            print("Nombre          " , "Activo   ")
                            print( i["nombre"] ,"     ",  i["activo"])

        elif res5.casefold()=="activo".casefold():
            res8=bool(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["activo"] == res8:
                            print("Nombre          " , "Activo   ")
                            print( i["nombre"] ,"     ",  i["activo"])
        elif res5.casefold()=="promedio".casefold():
            res9=float(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["promedio"] == res9:
                            print("Nombre          " , "Activo   ")
                            print( i["nombre"] ,"     ",  i["activo"]) 

#***********
    elif sele.casefold()=="nombre, promedio".casefold() or "promedio, nombre".casefold():
        res1= input("DONDE ")
        if res1.casefold()=="nombre".casefold():
            res=input("= ")
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["nombre"] == res:
                            print("Nombre          " , "Promedio   ")
                            print( i["nombre"] ,"     ",  i["promedio"])
                    #cont = cont +1   
                    # 
        elif res1.casefold()=="edad".casefold():
            res2=int(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["edad"] == res2:
                            print("Nombre          " , "Promedio   ")
                            print( i["nombre"] ,"     ",  i["promedio"])

        elif res1.casefold()=="activo".casefold():
            res2=bool(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["activo"] == res2:
                            print("Nombre          " , "Promedio   ")
                            print( i["nombre"] ,"     ",  i["promedio"])
        elif res1.casefold()=="promedio".casefold():
            res2=float(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["promedio"] == res2:
                            print("Nombre          " , "Promedio   ")
                            print( i["nombre"] ,"     ",  i["promedio"]) 

# segunda condicion-----------------------------------------------------------------------------------------------------------
    elif sele.casefold()=="nombre, activo, edad".casefold() or "activo, nombre, edad".casefold() or "edad, nombre, activo".casefold() or "edad, activo, nombre" or "activo, edad, nombre" or "nombre, edad, activo":
        res1= input("DONDE ")
        if res1.casefold()=="nombre".casefold():
            res=input("= ")
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["nombre"] == res:
                            print("Nombre          " , "Edad          ", "Activo")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["activo"])
                    #cont = cont +1   
                    # 
        elif res1.casefold()=="edad".casefold():
            res2=int(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["edad"] == res2:
                            print("Nombre          " , "Edad          ", "Activo")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["activo"])

        elif res1.casefold()=="activo".casefold():
            res2=bool(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["activo"] == res2:
                            print("Nombre          " , "Edad          ", "Activo")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["activo"])
        elif res1.casefold()=="promedio".casefold():
            res2=float(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["promedio"] == res2:
                            print("Nombre          " , "Edad          ", "Activo")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["activo"])

#**************
    elif sele.casefold()=="nombre, edad, promedio".casefold() or "nombre, promedio, edad".casefold() or "edad, nombre, promedio".casefold() or "promedio, nombre, edad" or "promedio, edad, nombre" or "edad, promedio, nombre":
        res1= input("DONDE ")
        if res1.casefold()=="nombre".casefold():
            res=input("= ")
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["nombre"] == res:
                            print("Nombre          " , "Edad          ", "Promedio")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["promedio"])
                    #cont = cont +1   
                    # 
        elif res1.casefold()=="edad".casefold():
            res2=int(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["edad"] == res2:
                            print("Nombre          " , "Edad          ", "Promedio")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["promedio"])

        elif res1.casefold()=="activo".casefold():
            res2=bool(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["activo"] == res2:
                            print("Nombre          " , "Edad          ", "Promedio")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["promedio"])
        elif res1.casefold()=="promedio".casefold():
            res2=float(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["promedio"] == res2:
                            print("Nombre          " , "Edad          ", "Promedio")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["promedio"])
#**********-
    elif sele.casefold()=="edad, activo, promedio".casefold() or "activo, promedio, edad".casefold() or "edad, promedio, activo".casefold() or "promedio, activo, edad" or "promedio, edad, activo" or "activo, edad, promedio":
        res1= input("DONDE ")
        if res1.casefold()=="nombre".casefold():
            res=input("= ")
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["nombre"] == res:
                            print("Edad          " , "Activo          ", "Promedio")
                            print( i["Edad"] ,"     ",  i["activo"],"    ",i["promedio"])
                    #cont = cont +1   
                    # 
        elif res1.casefold()=="edad".casefold():
            res2=int(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["edad"] == res2:
                            print("Edad          " , "Activo          ", "Promedio")
                            print( i["Edad"] ,"     ",  i["activo"],"    ",i["promedio"])

        elif res1.casefold()=="activo".casefold():
            res2=bool(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["activo"] == res2:
                            print("Edad          " , "Activo          ", "Promedio")
                            print( i["Edad"] ,"     ",  i["activo"],"    ",i["promedio"])
        elif res1.casefold()=="promedio".casefold():
            res2=float(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["promedio"] == res2:
                            print("Edad          " , "Activo          ", "Promedio")
                            print( i["Edad"] ,"     ",  i["activo"],"    ",i["promedio"])                  

#**********-
    elif sele.casefold()=="promedio, activo, nombre".casefold() or "nombre, activo, promedio".casefold() or "nombre, promedio, activo".casefold() or "promedio, nombre, activo" or "activo, promedio, nombre" or "activo, nombre, promedio":
        res1= input("DONDE ")
        if res1.casefold()=="nombre".casefold():
            res3=input("= ")
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["nombre"] == res3:
                            print("Nombre          " , "Activo          ", "Promedio")
                            print( i["nombre"] ,"     ",  i["activo"],"    ",i["promedio"])
                    #cont = cont +1   
                    # 
        elif res1.casefold()=="edad".casefold():
            res3=int(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["edad"] == res3:
                            print("Nombre          " , "Activo          ", "Promedio")
                            print( i["nombre"] ,"     ",  i["activo"],"    ",i["promedio"])

        elif res1.casefold()=="activo".casefold():
            res3=bool(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["activo"] == res3:
                            print("Nombre          " , "Activo          ", "Promedio")
                            print( i["nombre"] ,"     ",  i["activo"],"    ",i["promedio"])
        elif res1.casefold()=="promedio".casefold():
            res3=float(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["promedio"] == res3:
                            print("Nombre          " , "Activo          ", "Promedio")
                            print( i["nombre"] ,"     ",  i["activo"],"    ",i["promedio"])          


# tercera condicion--------------------------------------------------------------------------------------------------------    

    elif sele.casefold() == "nombre, edad, activo, promedio".casefold() or "nombre, edad, promedio, activo".casefold() or "promedio, nombre, activo, edad".casefold() or "nombre, activo, promedio, edad".casefold() or "edad, nombre, promedio, activo".casefold() or "nombre, activo, edad, promedio".casefold() or "nombre, promedio, edad, activo".casefold() or "nombre, promedio, activo, edad".casefold():
        res1= input("DONDE ")
        if res1.casefold()=="nombre".casefold():
            res=input("= ")
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["nombre"] == res:
                            print("Nombre          " , "Edad          ", "Activo           ","Promedio")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["activo"]),"    ", i["promedio"]
                    #cont = cont +1   
                    # 
        elif res1.casefold()=="edad".casefold():
            res2=int(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["edad"] == res2:
                            print("Nombre          " , "Edad          ", "Activo           ","Promedio")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["activo"]),"    ", i["promedio"]

        elif res1.casefold()=="activo".casefold():
            res2=bool(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["activo"] == res2:
                            print("Nombre          " , "Edad          ", "Activo           ","Promedio")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["activo"]),"    ", i["promedio"]
        elif res1.casefold()=="promedio".casefold():
            res2=float(input("= "))
            for a in dict:
                cont=0
                while cont < len(a):
                    mando = a[cont]
                    file = open(mando)
                    data= json.load(file)
                    file.close()
                    cont = cont +1 

                    for i in data:
                        if i["promedio"] == res2:
                            print("Nombre          " , "Edad          ", "Activo           ","Promedio")
                            print( i["nombre"] ,"     ",  i["edad"],"    ",i["activo"]),"    ", i["promedio"]       
      

    else:
        print("No se encontro")   



    

        

def listarArchivo():
    for a in dict:


        cont =0
        while cont < len(a):
            mando = a[cont]
            file= open(mando)
            data=json.load(file)
            file.close()
            cont = cont + 1   

            #pos=len(mando) 

            for i in data:
                pos= len(i)
                print(pos)

                #print("Hay ", pos ," registros")
            #print("Hay ",pos," registros")     

#*_[*[*[*[*[*[[*[[*[*[*[*[*[*[*[*[*[*[*[*[[*[*[*[*[*[*[*[*[*[*[[*[*[*[*[*[*[*[*[*[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]        

def maximo():
    sele = input("MAXIMO ")
    if sele.casefold() == "edad".casefold():
        for a in dict:
            cont =0
            while cont < len(a):
                mando = a[cont]
                file= open(mando)
                data=json.load(file)
                file.close()

                for i in data:
                    cole=i["edad"]
                    #a=max(cole)
                    #num = i["edad"]
                    #cuantos = len(nueva_lista)
                    #num.sort()
                    #print(num[0])
                    #maxi= max(nueva_lista)
                    #print(maxi)
                    print(cole)
                    #d=max(data)
                    #print(d)
                cont = cont +1      
               
        pass

#*_*_*_**_*_*_**_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*__*_*__*_*_*_*__*_*
def minimo():
    print("valor minimo")
    
                
                   
                    
#*_*_*_**_*_*_**_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*__*_*__*_*_*_*__*_*
def reporte():    
    print("REPORTAR N")
    #repo = input("REPORTE ")
    #fila=len(Lista)
    print("abriendo el archivo")
    f = open("practica.html")
    src=Template(f.read())
    for a in dict:
        cont=0
        while cont <len(a):
            mando = a[cont]
            file=open(mando)
            data = json.load(file)
            print(data)
            file.close()
                #print(data)
           # cont = cont +1
            for i in data:
                n=i["nombre"]
                e=i["edad"]
                a=i["activo"]
                p=i["promedio"]
                #filein = open('practica.html')
                #src=Template(filein.read())
                d={'nombre':n, 'edad':e,'activo': a, 'promedio':p}
                result = src.substitute(d)

                try:
                    os.mkdir("carga")
                    filein2= open('Carga/'+str(d)+'.html', 'w')
                    filein2.writelines(result)
                    print("Creando")
                except  OSError:
                    ("Los datos")
                    if os.path.exists('Carga'):
                        filein2= open('Carga/'+'201700399'+'.html','a')
                        filein2.writelines(result)
            cont = cont +1            

def reportar():
    filein = open('practica.html')

    src=Template(filein.read())
    for a in dict:
        cont=0
        while cont <len(a):
            mando = a[cont]
            file=open(mando)
            data = json.load(file)
            file.close()
                #print(data)
            #cont = cont +1  
            n=data["nombre"]
            e=data["edad"]
            a=data["activo"]
            p=data["promedio"]

            filein = open('practica.html')
            src=Template(filein.read())
            d={'nombre':n, 'edad':e,'activo': a, 'promedio':p}
            result = src.substitute(d)
            try :
                os.mkdir("Carga")
                filein2= open('Carga/'+str(d)+'.html','a')
                filein2.writelines(result)
                print("Creando")
            except OSError:
                if os.path.exists('Carga'):
                    filein2= open('Carga/'+'201700399'+'.html','a')
                    filein2.writelines(result)
            cont = cont +1          

                        


   # d = {'nombre':'Carlos', 'edad':'21','activo':'true','saldo':'10','nombre2':'Priscyla','edad2':'17','activo2':'false','saldo2':'50', 'nombre3':'Mauricio','edad3':'25','activo3':'true','saldo3':'90', 'nombre4':'Daniela','edad4':'16','activo4':'false','saldo4':'90',
    #'nombre5':'Juan','edad5':'30','activo5':'false','saldo5':'100', 'nombre6':'Cristina','edad6':'19','activo6':'true','saldo6':'200', 'nombre7':'Irma','edad7':'27','activo7':'false','saldo7':'1000', 'nombre8':'David','edad8':'31','activo8':'true','saldo8':'40',
    #'nombre9':'Lesly','edad9':'24','activo9':'true','saldo9':'25', 'nombre10':'Alejandra','edad10':'45','activo10':'false','saldo10':'85'}
    #result = src.substitute(d)

#    try:
#        os.mkdir("Tarea4")
#        filein2= open('Tarea4/'+'201700399'+'.html','a')
#        filein2.writelines(result)
#        print("Creando")
#    except OSError:
#        if os.path.exists('Tarea4'):

#            filein2= open('Tarea4/'+'201700399'+'.html','a')
#            filein2.writelines(result)
    #nombreArchivo = "file:///C:/Users/logas/Documents/python/Tarea4/201700399.html"
#    archivo="file:///C:/Users/logas/Documents/GitHub/201700399_TareasLFP/Tarea%204/Tarea4/201700399.html"
#    webbrowser.open_new_tab(archivo)    