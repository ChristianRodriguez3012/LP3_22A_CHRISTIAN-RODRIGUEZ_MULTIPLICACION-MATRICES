##Para el uso de threads se ha reutilizado parte del código de multiplicación secuencial
##Cada función será asignada a un thread (si está disponible) para cumplir su función
##Se crearon funciones de prueba para poder ver el funcionamiento paso a paso de los threads, estas funciones aun pueden ser activadas, solo se debe borrar un "#" de cada oración que tenga doble numeral ("##").

##Importando Librerias necesarias: Random y Numpy
from random import randint
import numpy as np 

##Definiendo N para generar las matrices 1 y 2
VariableN = int(input("DEFINIR N: "))

##Generando la matriz 1
print ("\n MATRIZ 1:")
def llenar_matriz1(n):
    matriz1 = []
    for r in range(n):
        fila = []
        for c in range(n):
            ##Determinando el rango de los valores, entre 0 y 10
            fila.append(randint(1, 10))        
        matriz1.append(fila)    
    return (matriz1)
resultadoA = llenar_matriz1(VariableN)
print(resultadoA)

##Generando la matriz 2
print ("\n MATRIZ 2:")
from random import randint
def llenar_matriz2(n):
    matriz2 = []
    for r in range(n):
        fila = []
        for c in range(n):
            ##Determinando el rango de los valores, entre 0 y 10
            fila.append(randint(1, 10))       
        matriz2.append(fila)   
    return (matriz2)

resultadoB = llenar_matriz2(VariableN)
print(resultadoB)

##Multiplicación de matrices 
resultado = np.dot(resultadoA,resultadoB)   


##Librerias para el uso de Threads y su reconocimiento
import time
import logging

##Creacion del Thread Pool
from concurrent.futures import Executor, ThreadPoolExecutor


##Para poder observar el nombre del thread en funcionamiento
#logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


##funcion creada para corroborar el uso y correcta función de los threads
#def super_task (a,b):
    ##El time.sleep simula una funcion de coste computacional alto con espera de 1 segundo para emular ese esfuerzo.
    #time.sleep(1)
    #logging.info(f'Se finalizó la multiplicación de matrices con valores {a} -  {b}!!\n')


if __name__ == '__main__':
##Observando tareas enviadas a los threads
    Executor = ThreadPoolExecutor (max_workers=3)
    Executor.submit(print("\nEL THREAD ESTÁ EN:\n",llenar_matriz1))
    Executor.submit(print("\nEL THREAD ESTÁ EN:\n",llenar_matriz2))
    Executor.submit (print("\nRESULTADO:\n",resultado))