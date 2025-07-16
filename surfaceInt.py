import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# i have define a simple vector field F = [x, y, 1]
def vector_field(x, y):
    Fx = x
    Fy = y
    Fz = 1
    return Fx, Fy, Fz

# here Define the surface: flat square in the xy-plane, z = 0
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

# now let's compute the vector field at each point on the surface
Fx, Fy, Fz = vector_field(X, Y)

# area element vector (dA): for xy-plane, it points in the z direction (0, 0, 1)
dA_x = np.zeros_like(X)
dA_y = np.zeros_like(Y)
dA_z = np.ones_like(Z)

# compute dot product of F and dA = Fx*dAx + Fy*dAy + Fz*dAz = Fz (since dAx and dAy are zero)
dot_product = Fx * dA_x + Fy * dA_y + Fz * dA_z  # This simplifies to just Fz = 1

# Compute total flux (approximate surface integral as sum)
dA_magnitude = 4 / (X.size)  # Area of square is 4, divided by number of elements
flux = np.sum(dot_product * dA_magnitude)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface (xy-plane)
ax.plot_surface(X, Y, Z, alpha=0.3, color='cyan', rstride=1, cstride=1, edgecolor='k')

# Plot the vector field (arrows coming out of surface)
ax.quiver(X, Y, Z, Fx, Fy, Fz, length=0.2, normalize=True, color='r')

# Labels and view
ax.set_title('Surface Integral: Vector Field Flow Through a Flat Surface')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(elev=30, azim=45)

flux
plt.show()