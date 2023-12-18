import socket
import time
#import numpy as np
import math
import cmath
import random
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

s = socket.socket()
s.connect(("127.0.0.1",1000))

def complexMod(a,b):
    x = (a.real - b.real)**2
    y = (a.imag - b.imag)**2
    
    mod = math.sqrt(x+y)
    #print("The modulus of " + str(x) + " and " + str(y) + " is " + str(mod))
    return mod

#just testing out the connection

message = "69 70;"
s.send(message.encode('utf-8'))
'''
time.sleep(2)

#testing complex operations
while True:
    a = complex(2,2)
    real = int(random.random()*25)
    power = a * cmath.log(real)
    b = cmath.exp(power)
    print(b.real)
    print(b.imag)
    message = str(int(b.real*100)) + " " + str(int(b.imag * 10)) + ";"
    print(message)

    s.send(message.encode('utf-8'))
    time.sleep(3)
'''

printStatements = True

epsilon = 0.0003
#instead of calculating the exact convergent value, we will run this until the the difference between the adjacent partial sums to be smaller than epsilon here
xplot = []
yplot = [] #initialize the plotting points
plt.ion()
plt.xlabel("real")
plt.ylabel("imaginary")

graph = plt.plot(xplot,yplot)[0]
plt.ylim(-1,1)
plt.pause(0.01)

while True:
    difference = float('inf') #initialize float at infinity
    previous = 0 #initialize the previous sum

    real = random.random() * -1 + 2.2 #the real component will be (1,3], the function is lot more fun when it takes a bit longer to converge
    imaginary = int(random.random() * 21 - 10) #imag componenent an int between [-10,10]
    while imaginary == 0: 
        imaginary = int(random.random() * 21 - 10) #don't want imag component to be zero
    
    xplot.clear()
    yplot.clear()

    sleeptime = 4
    
    n = 1 #our little boy that will grow
    while difference >= epsilon:
        z = complex(real,imaginary)
        power = z * cmath.log(n) #we calculate the power as we would in e^alpha log z form
        denom = cmath.exp(power) #this function does e^power
        
        psum = previous + 1/denom #calculate the new partial sum
        
        difference = complexMod(psum,previous) #log the difference
        previous = psum
        
        sleeptime = 2.5 * (math.log(difference) + 8)/8
        
        if sleeptime < 0.03:
            sleeptime = 0.03

        
        n = n+1 #increment n
        
        message = str(round(psum.real,5)) + " " + str(round(psum.imag,5)) + " " + str(float(int(sleeptime*1000))/1000) + ";"
        s.send(message.encode('utf-8'))

        xplot.append(psum.real)
        yplot.append(psum.imag)
        
        #to see how the difference changes with each incremenation
        #xplot.append(n-1)
        #yplot.append(math.log(difference))
        #goes from 0 -> -8

        graph.remove()
        
        # plotting newer graph
        graph = plt.plot(xplot,yplot,color = 'g')[0]
        plt.xlim(min(xplot),max(xplot))
        plt.ylim(min(yplot),max(yplot))
        plt.pause(0.05)
        
        
        if printStatements:
            print("Sleep for " + str(sleeptime))
            print("Iteration: " + str((n-1)))
            print("Partial sum is " + str(psum))
            print("Length is " + str(difference))
            print("Difference is: " + str(difference))
                
            plt.draw()
        
        time.sleep(sleeptime)
        
    if printStatements:
        print("Our z is " + str(real) + " + i" + str(imaginary))

        



