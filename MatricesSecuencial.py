print("MULTIPLICACIÓN DE MATRICES (SECUENCIAL)")
print("por: Christian Rodriguez")

#Importando Librerias necesarias: Random y Numpy (tambien time)
from random import randint
from re import X
import numpy as np 
#Libreria para cronometrar los tiempos de ejecución
from timeit import default_timer
#Libreria para editar archivos
import os
import time

#Definiendo N para generar las matrices 1 y 2
VariableN = int(input("DEFINIR N: "))


#iniciar Cronometro SECUENCIAL
inicioSec = default_timer()


#Generando la matriz 1
print ("\n MATRIZ 1:")
def llenar_matriz1(n):
    matriz1 = []
    for r in range(n):
        fila = []
        for c in range(n):
            #Determinando el rango de los valores, entre 0 y 10
            fila.append(randint(1, 10))        
        matriz1.append(fila)    
    return (matriz1)
resultadoA = llenar_matriz1(VariableN)

#Invocando e imprimiendo Funcion
print(resultadoA)



#Generando la matriz 2
print ("\n MATRIZ 2:")
from random import randint
def llenar_matriz2(n):
    matriz2 = []
    for r in range(n):
        fila = []
        for c in range(n):
            #Determinando el rango de los valores, entre 0 y 10
            fila.append(randint(1, 10))       
        matriz2.append(fila)   
    return (matriz2)
resultadoB = llenar_matriz2(VariableN)
print(resultadoB)


#Multiplicación de matrices 
resultado = np.dot(resultadoA,resultadoB)   
print ("RESULTADO:","\n",resultado) 

#finalizar Cronometro SECUENCIAL
finSec = default_timer()

#Imprimiento Cronometro SECUENCIAL
print ("TIEMPO DE EJECUCIÓN:", finSec-inicioSec)

infoSecuencial = [finSec-inicioSec]

#Fecha y Hora del cálculo
Formato = "%c"
FyHSecuencial = str(time.strftime(Formato))
print ("FECHA Y HORA DE EJECUCIÓN:", FyHSecuencial)

#Guardando tiempos de ejecución
print ("GUARDANDO RESULTADOS EN 'RegistroSecuencial.dat'")
#el "a" anexa todos los resultados, mientras que "w" solo guarda el último resultado
ArchivoSecuencial= open("RegistroSecuencial.dat", "a")
ArchivoSecuencial.write("\n El ultimo tiempo registrado es:")
ArchivoSecuencial.write(str(infoSecuencial))
ArchivoSecuencial.write("\n Fecha y hora: ")
ArchivoSecuencial.write(str(FyHSecuencial))
ArchivoSecuencial.close()

#Guardaremos unicamente los tiempos en otro archivo ".dat" de nombre "TimeSecuencial.dat"
TimeSecuencial= open("TimeSecuencial.dat", "a")
TimeSecuencial.write(str(infoSecuencial))
TimeSecuencial.close()
