import socket
import time
#import numpy as np
import math
import cmath
import random
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy as np


def complexMod(a,b):
    x = (a.real - b.real)**2
    y = (a.imag - b.imag)**2
    
    mod = math.sqrt(x+y)
    #print("The modulus of " + str(x) + " and " + str(y) + " is " + str(mod))
    return mod

def rzeta(s: complex, epsilon: float):

    difference = float('inf')
    previous = 0
    psum = 0
    ppsum = 0

    n = 0 #initialize zero

    while difference >= epsilon:
        ppsum = 0
        for k in range(0, n + 1):
            complexcomponent = cmath.exp(-s * cmath.log(k+1))
            
            ppsum = ppsum + (-1)**k * (math.factorial(n)/(math.factorial(k)*math.factorial(n-k))) * complexcomponent
            #print("ppsum " + str(ppsum))
        
        psum = (1/(2**(n+1))) * ppsum + psum
        difference = complexMod(psum, previous)
        
        previous = psum
        
        n = n + 1
        
        #print("psum " + str(psum))

    power = (1-s) * cmath.log(2)
    denom = 1 - cmath.exp(power)
    answer = (1/denom) * psum
    return answer
    #answer = complex(round(answer.real,10),round(answer.imag,10)) #round to 10 dec
    #print("psum is " + str(answer) + " after " + str(n) + " sums")

def f(x):
    return x**2

xplot = []
yplot = [] #initialize the plotting points
plt.ion()
plt.grid(linestyle='-', linewidth=1)
plt.xlabel("real")
plt.ylabel("imaginary")
graph = plt.plot(xplot,yplot)[0]
plt.xlim(-2,3)
plt.ylim(-2,2)
plt.pause(0.01)

x = np.linspace(0,35, 1000)
#plt.plot(x,f(x),color = 'red')
for i in x:
    rz = rzeta(complex(0.5,i),0.0000001)
    xplot.append(rz.real)
    yplot.append(rz.imag)
    
    graph.remove()
    plt.xlabel("i = " + str(round(i,1)))
    # plotting newer graph
    graph = plt.plot(xplot,yplot,color = 'g')[0]
    #plt.xlim(min(xplot),max(xplot))
    #plt.ylim(min(yplot),max(yplot))
    plt.pause(0.02)
    
plt.pause(10)
    
#plt.plot(xplot,yplot,color = 'green')
#plt.show()
# graph = plt.plot(x,f(x))
# plt.ylim(-1,1)
# plt.pause(0.01)

