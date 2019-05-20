# -*- coding: utf-8 -*-
"""
Created on Sun May 19 01:42:46 2019

@author: Eduardo Coutinho
"""




import matplotlib.pyplot as plt
import numpy as np
import math
"""
# unit area ellipse
rx, ry = 3., 1.
area = rx * ry * np.pi
theta = np.arange(0, 2 * np.pi + 0.01, 0.1)

verts = np.column_stack([rx / area * np.cos(theta), ry / area * np.sin(theta)])

x, y, s, c = np.random.rand(4, 30)
s *= 10**2.

fig, ax = plt.subplots()
ax.scatter(x, y, s, c, marker=verts)

plt.show()
x = [1, 2, 3, 4, 5 ,6 ,7, 8 ,9 , 10]
y = [11, 12, 13,14,15,16,17,18,19,20]


"""
        
class PontoCartesiano:

    
    def __init__(self, distancia, angulo):
        
        self.distancia = float(distancia)
        self.angulo = float(angulo)
        

    
    
    def get_distancia_A(self):
        return math.sin(self.angulo) * self.distancia
     
    def get_distancia_B(self):
        return math.cos(self.angulo) * self.distancia
    
    def getX(self):
       
        return  0 - self.get_distancia_B()
    
    def getY(self):
       
        return 0 - self.get_distancia_A()
    
    
arr = []
x = []
y = []


for k in range(1,361):
    radianos = math.radians(k*1)
    print(radianos)
    arr.append(PontoCartesiano(50 ,radianos))
    
    
 
for ar in arr:
    print(ar.getX())
    x.append(ar.getX())
    y.append(ar.getY())



plt.plot(x, y, color='green')
plt.scatter(x,y, color='red')
plt.show()

