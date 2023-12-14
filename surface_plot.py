import numpy as np
from numpy import pi, cos, sin, tan
import matplotlib.pyplot as plt

def parametrized_surface_plot(xf: str, yf: str, zf: str):
    
    """
    Plots a parametric surface based on the given expressions for x, y, and z.

    Parameters:
    - xf (str): Expression for the x-coordinate in terms of u and v.
    - yf (str): Expression for the y-coordinate in terms of u and v.
    - zf (str): Expression for the z-coordinate in terms of u and v.
    """
    
    try:
        
        # Parameter & Meshgrid
        u = np.linspace(0, 2 * np.pi, 250)
        v = np.linspace(0, 2 * np.pi, 250)
        u, v = np.meshgrid(u, v)  # Creates a grid of the generated u and v values

        # Point Generation using vectorized operations
        x = eval(xf)
        y = eval(yf)
        z = eval(zf)

        # Plot the surface
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='inferno')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Parametric Surface')
        plt.show()
        
    except Exception:
        print("Error")