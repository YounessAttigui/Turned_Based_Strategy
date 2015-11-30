 #-*- coding:utf8 -*-
from math import cos
import matplotlib.pyplot as plt
from numpy import *
from scipy.integrate import odeint
condinit=[1,0]
t=linspace(0,10,200)
def equadiff(y,t):
    return [y[1],-4*y[0]]

def oscillateur(t):
    return cos(2*t)

y=oscillateur(t)
xy=odeint(equadiff,condinit,t)
plt.subplot(2,1,1)
plt.grid()
plt.plot(t,xy[:,0],'o-',label='odeint')
plt.plot(t,y,'*',label='vraie')
plt.legend(loc=2)
plt.axis([0,10,-1.1,1.1])
plt.xlabel('t')
plt.ylabel('y')
plt.title("y''+ 4y = 0; y(0),y'(0)= 1.0,0.0; odeint 200 points")
plt.subplot(2,1,2)
plt.plot(xy[:,0],xy[:,1])
plt.title("Portrait de phase")
plt.show()
