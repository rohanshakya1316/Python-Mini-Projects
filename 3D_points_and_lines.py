import numpy as np

import matplotlib.pyplot as plt 

# Data for a three dimensional line
ax = plt.axes(projection = '3d')

z = np.linspace(0, 15, 1000)

x = np.sin(z)

y = np.cos(z)

ax.plot3D(x, y, z, 'black')

# Data for three dimensional scatterred points 
z = 15 * np.random.random(100)

x = np.sin(z) + 0.1 * np.random.random(100)

y = np.cos(z) + 0.1 * np.random.random(100)

ax.scatter3D(x, y, z, c = z, cmap = 'Greens')

plt.show()