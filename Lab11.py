import matplotlib.pyplot as plt

from numpy import *
import sympy as sp
import numpy as np

from math import *

def taylor(x):
    y = 0
    d1 = sp.diff(f, x)
    d2 = sp.diff(d1, x)
    d3 = sp.diff(d2, x)
    d4 = sp.diff(d3, x)
    print('d1 = ', d1)
    print('d2 = ', d2)
    print('d3 = ', d3)
    print('d4 = ', d4)
    x = 0
    d01 = -4*sin(4*x)-1
    d02 = -16*cos(4*x)
    d03 = 64*sin(4*x)
    f0 = sp.cos(4*x)-x+1
    print('d01 = ' ,d01)
    print('d02 = ' ,d02)
    print('d03 = ' ,d03)
    
    y = f0 + d01*t + d02 *(t-0) ** 2/2 + d03*(t-0) ** 3/6
    print ('y= ', y)
    return y

x = sp.symbols('x')
t = sp.symbols('t')
f = sp.cos(4*x)-x+1
taylorr = taylor(x)

p1 = sp.plot(f,(x, -5, 5), label="Taylor") 
plt.grid(True)
plt.show()
