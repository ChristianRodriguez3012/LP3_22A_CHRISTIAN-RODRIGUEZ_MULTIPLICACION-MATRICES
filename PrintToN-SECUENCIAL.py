print("MATRICES (HASTA N)")
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
VariableN = int(input("DEFINIR N: (MATRIZ NxN) "))
Iteracion = int(input("DEFINIR CANTIDAD DE MATRICES GENERADAS: "))
Limite = 0

#iniciar Cronometro SECUENCIAL
inicioEjec = default_timer()


for Limite in range (Iteracion):
    print ("\n MULTIPLICACION NUMERO: ", Limite+1)
    #Generando Matriz 1
    print ("\n MATRIZ: A ")
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
    print(resultadoA)


    #Generando la matriz 2
    print ("\n MATRIZ: B")
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

    Limite = Limite +1 

    #finalizar Cronometro
    finEjec = default_timer()
    #Imprimiento Cronometro
    print ("TIEMPO DE EJECUCIÓN:", finEjec-inicioEjec)
    resultadoA = llenar_matriz1(VariableN)
    #Rellenando TXT con las salidas
    infoPrintToN = [finEjec-inicioEjec]

    ##Fecha y Hora del cálculo
    Formato = "%c"
    FyH = str(time.strftime(Formato))
    #print ("FECHA Y HORA DE EJECUCIÓN:", FyH)

    ##Guardando tiempos de ejecución
    #print ("GUARDANDO RESULTADOS EN 'RegistroTiemposHastaN.dat'")
    ##el "a" anexa todos los resultados, mientras que "w" solo guarda el último resultado
    ArchivoPrintToN = open("RegistroTiemposHastaN-SECUENCIAL.dat", "a")
    ArchivoPrintToN.write("\n El ultimo tiempo registrado es:")
    ArchivoPrintToN.write(str(infoPrintToN))
    #ArchivoPrintToN.write("\n Fecha y hora: ")
    #ArchivoPrintToN.write(str(FyH))
    ArchivoPrintToN.close()

    #Guardaremos unicamente los tiempos en otro archivo ".dat" 
    TimePrintToN = open("TimePrintToN-SECUENCIAL.dat", "a")
    TimePrintToN.write(str(infoPrintToN))
    TimePrintToN.close()

#Invocando e imprimiendo Funcion
    print("ejecución finalizada")



