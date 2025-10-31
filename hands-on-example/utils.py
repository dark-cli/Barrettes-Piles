"""
Utility functions for barrette FEA analysis
"""

import numpy as np

# Import FEniCS if available
try:
    from fenics import *
    FENICS_AVAILABLE = True
except ImportError:
    FENICS_AVAILABLE = False
    # Define placeholder functions for testing
    def epsilon(v): pass
    def sym(grad): pass
    def as_tensor(*args): pass
    def MeshFunction(*args): pass
    def cells(*args): pass


def construct_D_matrix(E, nu):
    """
    Construct linear elastic constitutive matrix [D] for 3D analysis
    
    Parameters:
    -----------
    E : float
        Young's modulus (kN/m²)
    nu : float
        Poisson's ratio
    
    Returns:
    --------
    D : numpy array
        6x6 constitutive matrix for 3D (Voigt notation)
        Order: [εxx, εyy, εzz, γxy, γyz, γzx]
    """
    # Lame parameters
    lambda_param = E * nu / ((1 + nu) * (1 - 2*nu))
    mu = E / (2 * (1 + nu))
    
    # Build D matrix (isotropic elastic)
    D = np.array([
        [lambda_param + 2*mu, lambda_param, lambda_param, 0, 0, 0],
        [lambda_param, lambda_param + 2*mu, lambda_param, 0, 0, 0],
        [lambda_param, lambda_param, lambda_param + 2*mu, 0, 0, 0],
        [0, 0, 0, mu, 0, 0],
        [0, 0, 0, 0, mu, 0],
        [0, 0, 0, 0, 0, mu]
    ])
    
    return D


def epsilon_fenics(v):
    """
    Compute strain tensor from displacement field (FEniCS function)
    
    Parameters:
    -----------
    v : Function or TrialFunction
        Displacement field
    
    Returns:
    --------
    eps : Tensor
        Strain tensor
    """
    if not FENICS_AVAILABLE:
        raise ImportError("FEniCS is required for this function")
    return sym(grad(v))


def sigma_fenics(u, D_matrix):
    """
    Compute stress tensor from displacement field using constitutive matrix (FEniCS function)
    
    Parameters:
    -----------
    u : Function or TrialFunction
        Displacement field
    D_matrix : numpy array
        6x6 constitutive matrix
    
    Returns:
    --------
    sig : Tensor
        Stress tensor in Voigt notation
    """
    if not FENICS_AVAILABLE:
        raise ImportError("FEniCS is required for this function")
    
    # Get strain
    eps = epsilon_fenics(u)
    
    # Extract strain components
    eps_xx = eps[0, 0]
    eps_yy = eps[1, 1]
    eps_zz = eps[2, 2]
    eps_xy = eps[0, 1] + eps[1, 0]  # Engineering shear strain
    eps_yz = eps[1, 2] + eps[2, 1]
    eps_zx = eps[0, 2] + eps[2, 0]
    
    # Apply constitutive relation (simplified for linear elastic)
    # For FEniCS, we use the tensor form directly
    # This is a simplified implementation
    sig_xx = D_matrix[0, 0] * eps_xx + D_matrix[0, 1] * eps_yy + D_matrix[0, 2] * eps_zz
    sig_yy = D_matrix[1, 0] * eps_xx + D_matrix[1, 1] * eps_yy + D_matrix[1, 2] * eps_zz
    sig_zz = D_matrix[2, 0] * eps_xx + D_matrix[2, 1] * eps_yy + D_matrix[2, 2] * eps_zz
    sig_xy = D_matrix[3, 3] * eps_xy
    sig_yz = D_matrix[4, 4] * eps_yz
    sig_zx = D_matrix[5, 5] * eps_zx
    
    # Construct stress tensor
    sig = as_tensor([[sig_xx, sig_xy, sig_zx],
                     [sig_xy, sig_yy, sig_yz],
                     [sig_zx, sig_yz, sig_zz]])
    
    return sig


def extract_settlement(u, point):
    """
    Extract vertical displacement (settlement) at a point
    
    Parameters:
    -----------
    u : Function
        Displacement field solution
    point : tuple or list
        Coordinates (x, y, z)
    
    Returns:
    --------
    settlement : float
        Vertical displacement (negative = settlement)
    """
    try:
        u_at_point = u(point)
        if hasattr(u_at_point, '__len__') and len(u_at_point) >= 3:
            return u_at_point[2]  # z-component
        else:
            return float(u_at_point)
    except:
        # If point is not exactly on mesh, use nearest point
        return u(point[0], point[1], point[2])[2]


def create_barrette_region(mesh, barrette_center, barrette_dimensions):
    """
    Create marker for barrette region
    
    Parameters:
    -----------
    mesh : Mesh
        FEniCS mesh
    barrette_center : tuple
        Center coordinates (x, y, z)
    barrette_dimensions : tuple
        Dimensions (length, width, depth)
    
    Returns:
    --------
    marker : MeshFunction
        Marker function identifying barrette region
    """
    if not FENICS_AVAILABLE:
        raise ImportError("FEniCS is required for this function")
    
    marker = MeshFunction("size_t", mesh, mesh.topology().dim())
    marker.set_all(0)  # 0 = soil
    
    # Mark barrette region
    L, W, D = barrette_dimensions
    x_c, y_c, z_c = barrette_center
    
    # Define barrette bounds
    x_min = x_c - L/2
    x_max = x_c + L/2
    y_min = y_c - W/2
    y_max = y_c + W/2
    z_min = z_c - D
    z_max = z_c
    
    # Mark cells in barrette
    for cell in cells(mesh):
        mp = cell.midpoint()
        if (x_min <= mp.x() <= x_max and 
            y_min <= mp.y() <= y_max and 
            z_min <= mp.z() <= z_max):
            marker[cell] = 1  # 1 = barrette
    
    return marker

