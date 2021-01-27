import sys
import time
import calculadora

#For dato
datosPrueba = [4,3,2,1,0,"hola", 4.0]

for n1 in datosPrueba:
    for n2 in datosPrueba:
        resultado = calculadora.suma(n1, n2)
        print(n1,"+", n2, "=", resultado)
