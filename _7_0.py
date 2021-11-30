import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2, 5, 0.01)
plt.plot(x, x*np.sin(5*x))
plt.grid(color = 'r', 
         linestyle = '-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plotting graphs')
plt.show()
