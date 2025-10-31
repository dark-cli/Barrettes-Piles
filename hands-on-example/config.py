"""
Configuration file for barrette FEA analysis
All parameters can be modified here
"""

# Barrette Geometry
BARRETTE_LENGTH = 1.0      # m - length (strong direction)
BARRETTE_WIDTH = 0.8       # m - width
BARRETTE_DEPTH = 15.0      # m - embedment depth

# Soil Domain Size (multiples of barrette dimensions)
DOMAIN_LATERAL = 5.0       # multiples of barrette characteristic dimension
DOMAIN_DEPTH = 2.0         # multiples of embedment depth below base

# Material Properties - Concrete (Barrette)
E_CONCRETE = 30e6          # kN/m² - Young's modulus
NU_CONCRETE = 0.15         # Poisson's ratio
GAMMA_CONCRETE = 24.0      # kN/m³ - unit weight

# Material Properties - Soil
E_SOIL = 10000             # kN/m² - Young's modulus
NU_SOIL = 0.3              # Poisson's ratio
GAMMA_SOIL = 18.0          # kN/m³ - unit weight

# Mesh Density (number of elements)
MESH_DENSITY_X = 20        # elements in x-direction
MESH_DENSITY_Y = 20        # elements in y-direction
MESH_DENSITY_Z = 30        # elements in z-direction

# Loading
LOAD_INCREMENTS = [100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]  # kN
# Alternative: uniform increments
# LOAD_INCREMENTS = [i * 500 for i in range(1, 17)]  # 500, 1000, 1500, ... 8000 kN

# Output Settings
SAVE_RESULTS = True
PLOT_RESULTS = True

