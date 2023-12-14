import sympy as sp
from scipy.integrate import dblquad, quad

def parametric_surface_area(x_expression: str, y_expression: str, z_expression:str , u_limits, v_limits):
    """
    Calculate the surface area of a parametric surface defined by the equations x(u, v), y(u, v), z(u, v).

    Parameters:
    - x_expression (str): Parametric equation for x in terms of u and v.
    - y_expression (str): Parametric equation for y in terms of u and v.
    - z_expression (str): Parametric equation for z in terms of u and v.
    - u_limits (list): Limits of integration for the parameter u, e.g., [u_min, u_max].
    - v_limits (list): Limits of integration for the parameter v, e.g., [v_min, v_max].

    Returns:
    - surface_area (float): Surface area of the parametric surface.
    """

    try:
        
        u, v = sp.symbols('u v') # Create symbols for our parameters

        # Convert the function input for x, y, and z into a "sympy" expression. Allows for manipulations like partial derivative and "matrix"
        x = sp.sympify(x_expression)
        y = sp.sympify(y_expression)
        z = sp.sympify(z_expression)

        # Partial derivatives of x, y, and z with respect to u and v
        x_u = sp.diff(x, u)
        y_u = sp.diff(y, u)
        z_u = sp.diff(z, u)

        x_v = sp.diff(x, v)
        y_v = sp.diff(y, v)
        z_v = sp.diff(z, v)

        # Find Vectors in u and v directions
        vector_u = sp.Matrix([x_u, y_u, z_u]) # Form vector 'u' using partial derivatives of x, y, and z w/ respect to u
        vector_v = sp.Matrix([x_v, y_v, z_v]) # Form vector 'v' using partial derivatives of x, y, and z w/ respect to v

        # Determine Surface Area
        cross_product = vector_u.cross(vector_v) # Compute v cross u: finds vector perpendicular to both u and v
        cross_magnitude = cross_product.norm() # Calculate magnitude of the cross product: area of the parallelogram formed by vector_u and vector_v
        integrand = cross_magnitude # Integrand for double integration is the magnitude of the cross product
        surface_area, _ = dblquad(sp.lambdify((u, v), integrand), u_limits[0], u_limits[1], lambda u: v_limits[0], lambda u: v_limits[1])

        return surface_area
    
    except Exception:
        print("Error")

def parametric_curve_length(x_expression: str, y_expression: str, u_limits):
    """
    Calculate the arc length of a parametric curve defined by the equations x(u), y(u).

    Parameters:
    - x_expression (str): Parametric equation for x in terms of u.
    - y_expression (str): Parametric equation for y in terms of u.
    - u_limits (list): Limits of integration for the parameter u, e.g., [u_min, u_max].

    Returns:
    - curve_length (float): Arc length of the parametric curve.
    """

    try:
        
        u = sp.symbols('u')  # Create a symbol for the parameter

        # Convert the function input for x and y into "sympy" expressions.
        x = sp.sympify(x_expression)
        y = sp.sympify(y_expression)

        # Partial derivatives of x and y with respect to u
        x_u = sp.diff(x, u)
        y_u = sp.diff(y, u)

        # Form vector in the u direction
        vector_u = sp.Matrix([x_u, y_u])

        # Determine Curve Length
        integrand = vector_u.norm()  # Integrand for single integration is the magnitude of the vector
        curve_length, _ = quad(sp.lambdify(u, integrand), u_limits[0], u_limits[1])

        return curve_length

    except Exception:
        print("Error")