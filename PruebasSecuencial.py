import numpy as np 
  
#matriz1 = ([1, 6, 5],
        #[3 ,4, 8],
        #[2, 12, 3]) 
#matriz2 = ([3, 4],
        #[5, 6],
        #[6, 5]) 

import random
d = int(input("determine n:"))
matriz1 =[[0 for x in range(d)]
               for y in range(d)]

matriz2 =[[0 for x in range(d)]
               for y in range(d)]

print ("\n MATRIZ ALEATORIA 1:") 
for i in range(0, d):
      for j in range(0, d):
        matriz1[i][j] = int(random.randint(1,10))
        print(matriz1)

print ("\n MATRIZ ALEATORIA 2:") 
for x in range(0, d):
      for y in range(0, d):
        matriz2[x][y] = int(random.randint(1,10))
        print(matriz2)
  
resultado = np.dot(matriz1,matriz2) 
  
  
print ("\n RESULTADO:","\n",resultado) 