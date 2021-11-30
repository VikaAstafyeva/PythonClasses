from numpy import *
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
x= array([0,0.2,0.5,0.9,1.5], dtype=float)
y= array([1.75,2.68,1.24,0.72,1.35], dtype=float)
spl = UnivariateSpline(x,y)
xs = linspace(-1,3,1000)
plt.plot(x,y,'ro',xs,  spl(xs), 'g')
plt.grid(color = 'r', 
         linestyle = '-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spline')
plt.show()
