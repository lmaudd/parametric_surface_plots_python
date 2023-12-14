import sympy as sp
from scipy.integrate import dblquad

def parametric_surface_mass(x_expression: int, y_expression: int, z_expression: int, density_expression: int, u_range=[0, 1], v_range=[0, 1]):
   
    try:

        u, v = sp.symbols('u v')

        # Define parametric equations and density function
        x = sp.sympify(x_expression)
        y = sp.sympify(y_expression)
        z = sp.sympify(z_expression)
        density = sp.sympify(density_expression)

        # Calculate the partial derivatives of x, y, and z with respect to u
        dxu = sp.diff(x, u)
        dyu = sp.diff(y, u)
        dzu = sp.diff(z, u)

        # Calculate the partial derivatives of x, y, and z with respect to v
        dxv = sp.diff(x, v)
        dyv = sp.diff(y, v)
        dzv = sp.diff(z, v)

        # Mass determination
        cross_product = sp.Matrix([dyu*dzv - dzu*dyv, dzu*dxv - dxu*dzv, dxu*dyv - dyu*dxv]) # Cross product of partials
        cross_magnitude = cross_product.norm() # Magnitude of cross product
        mass_integral = sp.integrate(density * cross_magnitude, (u, u_range[0], u_range[1]), (v, v_range[0], v_range[1])) # Define integral
        mass = sp.N(mass_integral)  # Evaluate the numerical result
        
        return mass

    except Exception:
        print("Error")
    

# Example usage:
parametric_surface_mass("u * cos(v)", "4 - u**2", "u * sin(v)", "u + v")


def parametric_surface_mass_numerical(x_expression, y_expression, z_expression, density_expression, u_range=[0, 1], v_range=[0, 1]):
   
    try: 
        u, v = sp.symbols('u v')

        # Create expressions
        x = sp.sympify(x_expression)
        y = sp.sympify(y_expression)
        z = sp.sympify(z_expression)
        density = sp.sympify(density_expression)

        # Symbolic expressions to numeric functions (hopefully save time and allow code to run to completion???)
        x_func = sp.lambdify((u, v), x, 'numpy')
        y_func = sp.lambdify((u, v), y, 'numpy')
        z_func = sp.lambdify((u, v), z, 'numpy')
        density_func = sp.lambdify((u, v), density, 'numpy')

        # Computes the values of x, y, z, and density at each points 
        def integrand(u, v):
            x_val = x_func(u, v)
            y_val = y_func(u, v)
            z_val = z_func(u, v)
            density_val = density_func(u, v)
            return density_val * sp.sqrt(x_val**2 + y_val**2 + z_val**2)

        # Compute integration
        mass, _ = dblquad(integrand, u_range[0], u_range[1], v_range[0], v_range[1])

        return mass

    except Exception:
        print("Error")

# Example usage:
mass_numerical = parametric_surface_mass_numerical("u * cos(v)", "4 - u**2", "u * sin(v)", "u + v", [0, 2*sp.pi], [0, 2*sp.pi])