import numpy as np
from matplotlib import pyplot as plt

x= np.linspace(-3e-15,3e-15,1000)
y1=x
y2= (1-x)-1
plt.plot(x,y1,'blue')
plt.plot(x,y2,'green')
plt.show()