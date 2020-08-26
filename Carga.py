import json


#    file=[ ]
#   n=input("Ingrese la ruta")
#    print("Leer archivo")
#    leer=json.loads(open(n).read())
#    print(leer)
def readJson():
    cadena=[]
    n=input("Ingrese el nombre del archivo")
    file = open('archivo1.json',)
    data = json.load(file)
    file.close()
    print(data)
    return data 
      
#dict=readJson()
#for element in dict:
#    print(element)



