import sys
import time
import calculadora

#For dato
datosPrueba = [4,3,2,1,0,"hola", 4.0]
'''
print("Metadato")
for x in range(0,len(datosPrueba)):
    print(x)
    print("Anterior: ", x-1)
    print("S: ", x+1)

print("Dato")
for x in datosPrueba:
    print(x)
    print("A:", x-1)
    print("S:", x+1)
'''
print("Dato mediante metadato")
for x in range(0, len(datosPrueba)):
    print(datosPrueba[x])

    if x > 0:
        print("A:", datosPrueba[x-1])
    elif x == 0:
        print("A no existe")
    else:
        pass
        
    if x < (len(datosPrueba) - 1):
        print("S:", datosPrueba[x+1])
    elif x == (len(datosPrueba)):
        print("S no eiste")
