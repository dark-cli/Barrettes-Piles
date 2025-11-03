"""
Configuration file for barrette FEA analysis
All parameters can be modified here
"""

# Barrette Geometry
BARRETTE_LENGTH = 3.0      # m - length (strong direction)
BARRETTE_WIDTH = 1.5       # m - width
BARRETTE_DEPTH = 10.0      # m - embedment depth

# Soil Domain Size (fixed dimensions in meters)
DOMAIN_X = 20.0            # m - domain width in X direction
DOMAIN_Y = 20.0            # m - domain width in Y direction
DOMAIN_Z = 30.0            # m - total domain depth (from ground level to bottom)

# Material Properties - Concrete (Barrette)
E_CONCRETE = 30e6          # kN/m² - Young's modulus
NU_CONCRETE = 0.15         # Poisson's ratio
GAMMA_CONCRETE = 24.0      # kN/m³ - unit weight

# Material Properties - Soil
E_SOIL = 10000             # kN/m² - Young's modulus
NU_SOIL = 0.3              # Poisson's ratio
GAMMA_SOIL = 18.0          # kN/m³ - unit weight

# Mohr-Coulomb Plasticity Parameters
COHESION = 15.0            # kN/m² - effective cohesion c'
FRICTION_ANGLE = 25.0      # degrees - effective friction angle φ'
DILATATION_ANGLE = 0.0     # degrees - dilation angle (0 = non-associative flow)

# Mesh Density (number of elements)
MESH_DENSITY_X = 20        # elements in x-direction
MESH_DENSITY_Y = 20        # elements in y-direction
MESH_DENSITY_Z = 20        # elements in z-direction (uniform density in all directions)

# Loading
LOAD_INCREMENTS = [100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]  # kN
# Alternative: uniform increments
# LOAD_INCREMENTS = [i * 500 for i in range(1, 17)]  # 500, 1000, 1500, ... 8000 kN

# Output Settings
SAVE_RESULTS = True
PLOT_RESULTS = True

