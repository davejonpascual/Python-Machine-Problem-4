from math import sin
from math import cos
from math import radians
from math import sqrt
import numpy as np 
import matplotlib.pyplot as plt 


h = float(input('What is the initial height (in m)?'))
v = float(input('What is the initial velocity (in m/s)? '))
theta = float(input('What is the angle(in degrees) with repect to x? '))
ax = float(input('How fast is the object moving in the x-direction(in m/s^2)? '))
ay = float(input('How fast is the object moving in the y-direction(in m/s^2)? '))

if ay == 0:
    print('If the vertical acceleration is zero, then there is no free fall!' )

Vx = (v)*(cos(radians(theta)));
Vy = (v)*(sin(radians(theta)));

axi = 0;
ayi = 9.8; 

t = ((Vy) + (sqrt(((Vy)**2)+(2*ayi*h))))/(ayi)
r = (Vx*t)
s = (Vy)**2/(2*ayi)
hmax= h + s

T = np.linspace(0,t,100)

x = (Vx*T)
y = ((h)+(Vy*T)-((ayi*(T**2))/(2)))

Ti = np.linspace(0,t,100)
xi = (Vx*Ti) + ((1/2)*(ax)*T**2);
yi = ((h) + (Vy*Ti) + ((ay*(Ti**2))/2));


x = (Vx*Ti)
y = ((h)+(Vy*Ti)-((ayi*(Ti**2))/(2)))

plt.plot (x,y, label= 'Ideal' )
plt.plot(xi,yi, label= 'Non-Ideal')
plt.xlabel('Movement in x', )
plt.ylabel('Movement in y')
plt.title('Non/ideal Motion')
plt.legend()
plt.grid (True)
plt.show()

    

