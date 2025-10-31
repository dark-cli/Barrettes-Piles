"""
Linear Elastic Finite Element Analysis of Barrette Piles
Using FEniCS

This script performs linear elastic FEA analysis of a barrette pile
subjected to vertical loading.

Limitations:
- Linear elastic analysis only (no plasticity)
- Uniform mesh (no adaptive refinement)
- Simplified material model
"""

# Check for required dependencies
try:
    from fenics import *
except ImportError:
    print("=" * 60)
    print("ERROR: FEniCS is not installed")
    print("=" * 60)
    print("\nPlease install FEniCS using one of the following methods:")
    print("\n1. Using conda (recommended):")
    print("   conda install -c conda-forge fenics")
    print("\n2. Using Docker:")
    print("   docker pull quay.io/fenicsproject/stable")
    print("\n3. See FEniCS documentation:")
    print("   https://fenicsproject.org/download/")
    print("\n" + "=" * 60)
    exit(1)

try:
    import numpy as np
    import matplotlib.pyplot as plt
    import os
except ImportError as e:
    print(f"ERROR: Missing required package: {e}")
    print("Install with: pip install numpy matplotlib")
    exit(1)

from config import *
from utils import construct_D_matrix, extract_settlement, create_barrette_region

# Suppress FEniCS output
try:
    set_log_level(ERROR)
except:
    pass  # If set_log_level not available, continue

# Define epsilon function locally
def epsilon(v):
    """Compute strain tensor from displacement field"""
    return sym(grad(v))

print("=" * 60)
print("Barrette Pile FEA Analysis - Linear Elastic")
print("=" * 60)

# ============================================================================
# Step 1: Geometry and Mesh
# ============================================================================
print("\n[1/7] Setting up geometry and mesh...")

# Calculate domain dimensions
# Use characteristic dimension (largest lateral dimension) for consistent lateral extension
char_dim = max(BARRETTE_LENGTH, BARRETTE_WIDTH)
domain_x = char_dim * DOMAIN_LATERAL  # Same extension in all lateral directions
domain_y = char_dim * DOMAIN_LATERAL
domain_z_top = 0.0
domain_z_bottom = -(BARRETTE_DEPTH * (1 + DOMAIN_DEPTH))

# Verify domain size adequacy
depth_below_base = abs(domain_z_bottom) - BARRETTE_DEPTH
lateral_x_ratio = domain_x / char_dim
lateral_y_ratio = domain_y / char_dim
depth_ratio = depth_below_base / BARRETTE_DEPTH

print(f"   Domain size: {domain_x:.1f} x {domain_y:.1f} x {abs(domain_z_bottom):.1f} m")
print(f"   Mesh density: {MESH_DENSITY_X} x {MESH_DENSITY_Y} x {MESH_DENSITY_Z} elements")
print(f"\n   [Domain Adequacy Check]")
print(f"      Lateral X: {lateral_x_ratio:.1f}× char_dim (recommended: 3-5×)")
print(f"      Lateral Y: {lateral_y_ratio:.1f}× char_dim (recommended: 3-5×)")
print(f"      Below base: {depth_ratio:.1f}× embedment depth (recommended: 2-3×)")
if 3 <= lateral_x_ratio <= 5 and 3 <= lateral_y_ratio <= 5 and 2 <= depth_ratio <= 3:
    print(f"      ✓ Domain size is adequate")
else:
    if lateral_x_ratio < 3 or lateral_y_ratio < 3:
        print(f"      ⚠️  Warning: Lateral domain may be too small")
    if depth_ratio < 2:
        print(f"      ⚠️  Warning: Depth below base may be too small")

mesh = BoxMesh(Point(0, 0, domain_z_bottom),
               Point(domain_x, domain_y, domain_z_top),
               MESH_DENSITY_X, MESH_DENSITY_Y, MESH_DENSITY_Z)

print(f"   Total elements: {mesh.num_cells()}")
print(f"   Total nodes: {mesh.num_vertices()}")

# ============================================================================
# Step 3: Material Properties and Regions
# ============================================================================
print("\n[3/7] Setting up material properties...")

# Barrette center (at center of domain in x-y, top at ground surface)
barrette_center = (domain_x/2, domain_y/2, 0.0)
barrette_dims = (BARRETTE_LENGTH, BARRETTE_WIDTH, BARRETTE_DEPTH)

# Create region markers
marker = create_barrette_region(mesh, barrette_center, barrette_dims)

# Define measures for integration
dx = Measure('dx', domain=mesh, subdomain_data=marker)

# Create constitutive matrices
D_soil = construct_D_matrix(E_SOIL, NU_SOIL)
D_concrete = construct_D_matrix(E_CONCRETE, NU_CONCRETE)

print(f"   Soil: E = {E_SOIL/1000:.0f} MPa, ν = {NU_SOIL:.2f}")
print(f"   Concrete: E = {E_CONCRETE/1e6:.0f} GPa, ν = {NU_CONCRETE:.2f}")

# Note: For mesh-only visualization, run visualize_mesh.py separately
# This avoids unnecessary overhead when running the full analysis

# ============================================================================
# Step 2: Define Function Space
# ============================================================================
print("\n[2/7] Defining function space...")
V = VectorFunctionSpace(mesh, 'P', 1)  # First-order Lagrange elements
print(f"   Degrees of freedom: {V.dim()}")

# ============================================================================
# Step 4: Variational Formulation
# ============================================================================
print("\n[4/7] Setting up variational form...")

u = TrialFunction(V)
v = TestFunction(V)

# Strain tensors
eps_u = epsilon(u)
eps_v = epsilon(v)

# Stress for soil (using simplified approach - actual implementation would use tensor form)
# For linear elastic, we use inner product of strain
# sigma = 2*mu*epsilon + lambda*tr(epsilon)*I

# Lame parameters for soil
mu_soil = E_SOIL / (2 * (1 + NU_SOIL))
lambda_soil = E_SOIL * NU_SOIL / ((1 + NU_SOIL) * (1 - 2*NU_SOIL))

# Lame parameters for concrete
mu_concrete = E_CONCRETE / (2 * (1 + NU_CONCRETE))
lambda_concrete = E_CONCRETE * NU_CONCRETE / ((1 + NU_CONCRETE) * (1 - 2*NU_CONCRETE))

# Variational form: a(u,v) = integral(sigma(u) : epsilon(v))
# For isotropic linear elastic: sigma = lambda*tr(eps)*I + 2*mu*eps
a_soil = 2*mu_soil*inner(eps_u, eps_v)*dx(0) + lambda_soil*tr(eps_u)*tr(eps_v)*dx(0)
a_concrete = 2*mu_concrete*inner(eps_u, eps_v)*dx(1) + lambda_concrete*tr(eps_u)*tr(eps_v)*dx(1)
a = a_soil + a_concrete

print("   Variational form defined")

# ============================================================================
# Step 5: Boundary Conditions
# ============================================================================
print("\n[5/7] Applying boundary conditions...")

bcs = []

# Bottom boundary: fixed (u = 0)
def bottom_boundary(x, on_boundary):
    return on_boundary and near(x[2], domain_z_bottom, 1e-6)

bc_bottom = DirichletBC(V, Constant((0.0, 0.0, 0.0)), bottom_boundary)
bcs.append(bc_bottom)

# Lateral boundaries: roller (zero horizontal displacement)
def left_boundary(x, on_boundary):
    return on_boundary and near(x[0], 0.0, 1e-6)

def right_boundary(x, on_boundary):
    return on_boundary and near(x[0], domain_x, 1e-6)

def front_boundary(x, on_boundary):
    return on_boundary and near(x[1], 0.0, 1e-6)

def back_boundary(x, on_boundary):
    return on_boundary and near(x[1], domain_y, 1e-6)

bc_left = DirichletBC(V.sub(0), Constant(0.0), left_boundary)  # ux = 0
bc_right = DirichletBC(V.sub(0), Constant(0.0), right_boundary)  # ux = 0
bc_front = DirichletBC(V.sub(1), Constant(0.0), front_boundary)  # uy = 0
bc_back = DirichletBC(V.sub(1), Constant(0.0), back_boundary)  # uy = 0

bcs.extend([bc_left, bc_right, bc_front, bc_back])

print(f"   Applied {len(bcs)} boundary conditions")

# ============================================================================
# Step 6: Loading and Solution
# ============================================================================
print("\n[6/7] Applying loads and solving...")

# Barrette top surface area
A_barrette = BARRETTE_LENGTH * BARRETTE_WIDTH

# Barrette top center point for settlement extraction
barrette_top_center = (domain_x/2, domain_y/2, 0.0)

# Store results
loads_applied = []
settlements = []

# Define barrette top surface for loading (only apply load here, not entire domain)
# Barrette center and dimensions
barrette_x_center = domain_x / 2
barrette_y_center = domain_y / 2
barrette_x_min = barrette_x_center - BARRETTE_LENGTH / 2
barrette_x_max = barrette_x_center + BARRETTE_LENGTH / 2
barrette_y_min = barrette_y_center - BARRETTE_WIDTH / 2
barrette_y_max = barrette_y_center + BARRETTE_WIDTH / 2

class BarretteTopSurface(SubDomain):
    def inside(self, x, on_boundary):
        # Only mark the barrette top surface (at z=0, within barrette x-y bounds)
        return (on_boundary and 
                near(x[2], 0.0, 1e-6) and
                barrette_x_min <= x[0] <= barrette_x_max and
                barrette_y_min <= x[1] <= barrette_y_max)

barrette_top = BarretteTopSurface()
boundaries = MeshFunction("size_t", mesh, mesh.topology().dim() - 1)
boundaries.set_all(0)  # 0 = no load
barrette_top.mark(boundaries, 1)  # 1 = barrette top (load applied here)
ds = Measure('ds', domain=mesh, subdomain_data=boundaries)

print(f"   Load increments: {len(LOAD_INCREMENTS)}")
print(f"   Barrette top area: {A_barrette:.2f} m²")

# Verify how many surface elements are on barrette top
num_surface_facets = 0
for facet in facets(mesh):
    if boundaries[facet] == 1:
        num_surface_facets += 1
print(f"   Barrette top surface facets (elements): {num_surface_facets}")

for i, load in enumerate(LOAD_INCREMENTS):
    print(f"   Solving for load {i+1}/{len(LOAD_INCREMENTS)}: {load} kN...", end=" ")
    
    # Apply load on barrette top (uniform pressure)
    # Pressure = Force / Area (kN/m²)
    load_pressure = load / A_barrette  # kN/m²
    
    # Define loading vector (negative z-direction = downward)
    # Load is applied ONLY on barrette top surface (marked as 1)
    # FEniCS automatically distributes: L = ∫ p * v dS
    # Each surface element receives: force = pressure × element_area
    # Total force = pressure × total_surface_area = (load/A_barrette) × A_barrette = load ✓
    L = dot(Constant((0.0, 0.0, -load_pressure)), v) * ds(1)
    
    # Verify total applied load (for first load only)
    if i == 0:
        # Compute actual surface area of marked facets
        # Simply integrate 1.0 over the surface: area = ∫ 1 dS
        actual_area = assemble(Constant(1.0) * ds(1))
        
        # Expected total force = pressure × actual_area
        expected_total_force = load_pressure * actual_area
        
        print(f"\n      [Load Verification]")
        print(f"         Number of surface facets: {num_surface_facets}")
        print(f"         Actual barrette top surface area: {actual_area:.4f} m²")
        print(f"         Expected area: {A_barrette:.4f} m²")
        print(f"         Pressure: {load_pressure:.2f} kN/m²")
        print(f"         Total force (pressure × area): {expected_total_force:.2f} kN (target: {load:.2f} kN)")
        print(f"         Load per facet ≈ {expected_total_force/num_surface_facets:.2f} kN/facet")
        
        if abs(actual_area - A_barrette) > 0.01 * A_barrette:
            print(f"         ⚠️  Note: Surface area differs from expected (mesh discretization)")
        if abs(expected_total_force - load) > 0.01 * load:
            print(f"         ⚠️  WARNING: Total force mismatch!")
    
    # Solve
    u = Function(V)
    solve(a == L, u, bcs)
    
    # Extract settlement at barrette top center
    settlement = extract_settlement(u, barrette_top_center)
    settlements.append(settlement)
    loads_applied.append(load)
    
    print(f"Settlement: {settlement*1000:.2f} mm")

# ============================================================================
# Step 7: Post-Processing
# ============================================================================
print("\n[7/7] Post-processing results...")

# Convert to arrays
loads_array = np.array(loads_applied)
settlements_array = np.array(settlements)

# Plot load-displacement curve
if PLOT_RESULTS:
    plt.figure(figsize=(10, 6))
    plt.plot(settlements_array * 1000, loads_array / 1000, 'b-o', linewidth=2, markersize=6)
    plt.xlabel('Settlement (mm)', fontsize=12)
    plt.ylabel('Load (MN)', fontsize=12)
    plt.title('Load-Settlement Curve - Barrette Pile (Linear Elastic)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if SAVE_RESULTS:
        plot_file = 'results/load_settlement_curve.png'
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        print(f"   Saved plot: {plot_file}")
    plt.show()

# Save results to file
if SAVE_RESULTS:
    results_file = 'results/results.txt'
    with open(results_file, 'w') as f:
        f.write("Barrette Pile FEA Analysis Results\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Barrette dimensions: {BARRETTE_LENGTH} x {BARRETTE_WIDTH} x {BARRETTE_DEPTH} m\n")
        f.write(f"Soil E = {E_SOIL} kN/m², ν = {NU_SOIL}\n")
        f.write(f"Concrete E = {E_CONCRETE} kN/m², ν = {NU_CONCRETE}\n\n")
        f.write("Load (kN)\tSettlement (mm)\n")
        f.write("-" * 40 + "\n")
        for load, settlement in zip(loads_array, settlements_array):
            f.write(f"{load:.0f}\t\t{settlement*1000:.2f}\n")
    print(f"   Saved results: {results_file}")

# Summary
print("\n" + "=" * 60)
print("Analysis Complete!")
print("=" * 60)
print(f"\nSummary:")
print(f"  Total load increments: {len(LOAD_INCREMENTS)}")
print(f"  Maximum load: {max(loads_applied)} kN")
print(f"  Maximum settlement: {min(settlements)*1000:.2f} mm")
print(f"\nNote: This is LINEAR ELASTIC analysis only.")
print(f"      Results are valid for service loads but do not")
print(f"      capture soil failure or ultimate capacity.")

