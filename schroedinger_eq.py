# Repositorys
import numpy as np
from scipy.special import sph_harm
import matplotlib.pyplot as plt
import matplotlib as matplotlib
from mpl_toolkits.mplot3d import Axes3D
import cmath


# Create Diagramm
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Variables
l = 1
m = 0
phi = np.linspace(0, np.pi, 150)
theta = phi = np.linspace(0, 2*np.pi, 150)

# Variables for linear combination
# l2 = 1
# m2 = -1
# t = 0

# Calculate  linear combination
X = abs(sph_harm(m, l, theta, phi)
        ) * np.outer(np.cos(phi), np.sin(theta))
Y = abs(sph_harm(m, l, theta, phi)
        ) * np.outer(np.sin(phi), np.sin(theta))
Z = abs(sph_harm(m, l, theta, phi)) * \
    np.outer(np.ones(np.size(phi)), np.cos(theta))

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, color='b')

plt.show()
