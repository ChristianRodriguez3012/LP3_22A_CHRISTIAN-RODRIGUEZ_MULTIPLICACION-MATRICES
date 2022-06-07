import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15,15))
fig.tight_layout()
colores = ['blue','green','red','cyan','magenta','yellow','black','white']

for i in range (1,7):
    x = np.arange(0,16,2)
    y = pow(x,np.random.randint(0,6))+np.random.randint(0,10)*x+np.random.randint(-5, 10)
    ax = plt.subplot(2,3,i)
    ax.plot(x,y,color = colores[i])
    ax.set_xlabel('x')
    ax.set_xlabel('y')
    ax.set_title('Gráfica '+str(i))