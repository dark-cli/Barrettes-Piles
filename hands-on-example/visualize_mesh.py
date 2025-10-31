"""
Mesh Visualization Script for Barrette Pile FEA

This script generates and visualizes the mesh without running the full analysis.
Useful for checking mesh quality and geometry before running expensive computations.

Usage:
    python visualize_mesh.py
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

import os  # Import early for display checking

# Set matplotlib backend BEFORE importing pyplot (critical!)
import matplotlib
if os.environ.get('DISPLAY') is not None:
    try:
        matplotlib.use('TkAgg')  # Try TkAgg first (works on most systems)
    except Exception:
        try:
            matplotlib.use('Qt5Agg')  # Fallback to Qt5
        except Exception:
            pass  # Use default

try:
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
except ImportError as e:
    print(f"ERROR: Missing required package: {e}")
    print("Install with: pip install numpy matplotlib")
    exit(1)

from config import *
from utils import create_barrette_region

# Suppress FEniCS output
try:
    set_log_level(ERROR)
except:
    pass

print("=" * 60)
print("Barrette Pile Mesh Visualization")
print("=" * 60)

# ============================================================================
# Step 1: Geometry and Mesh
# ============================================================================
print("\n[1/3] Setting up geometry and mesh...")

# Calculate domain dimensions
char_dim = max(BARRETTE_LENGTH, BARRETTE_WIDTH)
domain_x = char_dim * DOMAIN_LATERAL
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
# Step 2: Identify Barrette Region
# ============================================================================
print("\n[2/3] Identifying barrette region...")

barrette_center = (domain_x/2, domain_y/2, 0.0)
barrette_dims = (BARRETTE_LENGTH, BARRETTE_WIDTH, BARRETTE_DEPTH)

# Create region markers
marker = create_barrette_region(mesh, barrette_center, barrette_dims)

# Count barrette elements
barrette_elements_count = 0
for cell in cells(mesh):
    if marker[cell] == 1:
        barrette_elements_count += 1

print(f"   Barrette dimensions: {BARRETTE_LENGTH} x {BARRETTE_WIDTH} x {BARRETTE_DEPTH} m")
print(f"   Barrette elements: {barrette_elements_count}")
print(f"   Soil elements: {mesh.num_cells() - barrette_elements_count}")

# ============================================================================
# Step 3: Visualization
# ============================================================================
print("\n[3/3] Generating 3D mesh visualization...")

# Barrette center and dimensions for visualization
barrette_x_center = domain_x / 2
barrette_y_center = domain_y / 2
x_min = barrette_x_center - BARRETTE_LENGTH / 2
x_max = barrette_x_center + BARRETTE_LENGTH / 2
y_min = barrette_y_center - BARRETTE_WIDTH / 2
y_max = barrette_y_center + BARRETTE_WIDTH / 2
z_top = 0.0
z_bottom = -BARRETTE_DEPTH

# Create 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Draw barrette as transparent box
barrette_vertices = [
    [(x_min, y_min, z_bottom), (x_max, y_min, z_bottom), (x_max, y_max, z_bottom), (x_min, y_max, z_bottom)],
    [(x_min, y_min, z_top), (x_max, y_min, z_top), (x_max, y_max, z_top), (x_min, y_max, z_top)],
    [(x_min, y_min, z_bottom), (x_max, y_min, z_bottom), (x_max, y_min, z_top), (x_min, y_min, z_top)],
    [(x_min, y_max, z_bottom), (x_max, y_max, z_bottom), (x_max, y_max, z_top), (x_min, y_max, z_top)],
    [(x_min, y_min, z_bottom), (x_min, y_max, z_bottom), (x_min, y_max, z_top), (x_min, y_min, z_top)],
    [(x_max, y_min, z_bottom), (x_max, y_max, z_bottom), (x_max, y_max, z_top), (x_max, y_min, z_top)]
]
barrette_faces = Poly3DCollection(barrette_vertices, alpha=0.3, facecolor='red', edgecolor='darkred', linewidth=2)
ax.add_collection3d(barrette_faces)

# Draw domain boundary as wireframe
domain_corners = [
    (0, 0, domain_z_bottom), (domain_x, 0, domain_z_bottom),
    (domain_x, domain_y, domain_z_bottom), (0, domain_y, domain_z_bottom),
    (0, 0, 0), (domain_x, 0, 0),
    (domain_x, domain_y, 0), (0, domain_y, 0)
]
domain_edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # Bottom
    [4, 5], [5, 6], [6, 7], [7, 4],  # Top
    [0, 4], [1, 5], [2, 6], [3, 7]   # Vertical
]
for edge in domain_edges:
    p1 = domain_corners[edge[0]]
    p2 = domain_corners[edge[1]]
    ax.plot3D([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'b-', alpha=0.3, linewidth=1)

# Sample mesh nodes for visualization (to avoid overcrowding)
sample_nodes = []
sample_count = 0
max_nodes_plot = 5000  # Limit nodes for performance
for vertex in vertices(mesh):
    if sample_count < max_nodes_plot or sample_count % 10 == 0:
        try:
            pt = vertex.point()
            # Handle different point representations
            if hasattr(pt, '__len__'):
                if len(pt) >= 3:
                    sample_nodes.append([pt[0], pt[1], pt[2]])
                else:
                    sample_nodes.append([pt.x(), pt.y(), pt.z()])
            else:
                sample_nodes.append([pt.x(), pt.y(), pt.z()])
        except:
            pass
    sample_count += 1

if len(sample_nodes) > 0:
    nodes_array = np.array(sample_nodes)
    ax.scatter(nodes_array[:, 0], nodes_array[:, 1], nodes_array[:, 2], 
              c='gray', s=0.5, alpha=0.3)

# Labels and settings
ax.set_xlabel('X (m)', fontsize=10)
ax.set_ylabel('Y (m)', fontsize=10)
ax.set_zlabel('Z (m)', fontsize=10)
ax.set_title('3D Mesh Visualization\nRed = Barrette, Blue = Domain Boundary, Gray = Mesh Nodes', fontsize=12)

# Set limits
ax.set_xlim([0, domain_x])
ax.set_ylim([0, domain_y])
ax.set_zlim([domain_z_bottom, 0])

# Set equal aspect ratio (real proportions)
x_range = domain_x
y_range = domain_y
z_range = abs(domain_z_bottom)
max_range = max(x_range, y_range, z_range)

# Set box aspect to maintain real proportions
try:
    # For newer matplotlib versions (3.3+)
    ax.set_box_aspect([x_range/max_range, y_range/max_range, z_range/max_range])
except AttributeError:
    # For older matplotlib versions, use set_aspect manually
    scale_x = max_range / x_range
    scale_y = max_range / y_range
    scale_z = max_range / z_range
    ax.set_xlim([0, domain_x * scale_x])
    ax.set_ylim([0, domain_y * scale_y])
    ax.set_zlim([domain_z_bottom * scale_z, 0])

# Add legend
import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', alpha=0.3, label='Barrette')
blue_line = mpatches.Patch(color='blue', alpha=0.3, label='Domain Boundary')
ax.legend(handles=[red_patch, blue_line], loc='upper right')

plt.tight_layout()

# Create results directory if it doesn't exist
os.makedirs('results', exist_ok=True)

# Check if display is available for interactive plotting
display_available = False
backend_name = matplotlib.get_backend().lower()

# Check for X11 display
has_display = os.environ.get('DISPLAY') is not None

# Non-interactive backends (can't show windows)
# Note: 'agg' alone is non-interactive, but 'TkAgg', 'Qt5Agg', etc. ARE interactive
non_interactive_exact = ['agg', 'pdf', 'svg', 'ps', 'pgf', 'cairo']
interactive_backends = ['tkagg', 'qt5agg', 'qt4agg', 'gtk3agg', 'gtk4agg', 'macosx', 'wxagg']

# Backend is interactive if it's explicitly in the interactive list
# or it's not exactly 'agg' and contains a known GUI toolkit
is_interactive_backend = (
    backend_name in interactive_backends or
    (backend_name != 'agg' and any(ib in backend_name for ib in ['tk', 'qt', 'gtk', 'wx', 'macosx']))
)

if has_display and is_interactive_backend:
    # Double-check by trying to create a test figure
    try:
        test_fig = plt.figure(figsize=(1, 1))
        plt.close(test_fig)
        display_available = True
    except Exception as e:
        display_available = False
        print(f"   [Debug] Backend test failed: {e}")
else:
    if not has_display:
        print(f"   [Debug] No DISPLAY environment variable set")
    if not is_interactive_backend:
        print(f"   [Debug] Backend '{backend_name}' is not interactive")

# Save static image (always)
mesh_plot_file = 'results/mesh_3d.png'
plt.savefig(mesh_plot_file, dpi=300, bbox_inches='tight')
print(f"   ✓ Saved mesh visualization: {mesh_plot_file}")

# Show interactive 3D plot if display is available
if display_available:
    print("\n   🖼️  Opening interactive 3D plot window...")
    print("   (You can rotate, zoom, and pan the plot)")
    print("   (Close the window when done)\n")
    plt.show(block=True)  # block=True keeps the window open until closed
else:
    print("\n   ℹ️  No display detected - saved image only")
    print("   (If you have a display, check DISPLAY environment variable)")
    print("   (For remote access, use X11 forwarding: ssh -X or ssh -Y)")
    plt.close(fig)  # Close to free memory

# Also save as interactive HTML if plotly available
try:
    import plotly.graph_objects as go
    
    fig_plotly = go.Figure()
    
    # Barrette bottom
    fig_plotly.add_trace(go.Scatter3d(
        x=[x_min, x_max, x_max, x_min, x_min],
        y=[y_min, y_min, y_max, y_max, y_min],
        z=[z_bottom, z_bottom, z_bottom, z_bottom, z_bottom],
        mode='lines',
        name='Barrette',
        line=dict(color='red', width=5),
        showlegend=True
    ))
    # Barrette top
    fig_plotly.add_trace(go.Scatter3d(
        x=[x_min, x_max, x_max, x_min, x_min],
        y=[y_min, y_min, y_max, y_max, y_min],
        z=[z_top, z_top, z_top, z_top, z_top],
        mode='lines',
        name='Barrette Top',
        line=dict(color='red', width=5),
        showlegend=False
    ))
    
    # Mesh nodes (sampled)
    if len(sample_nodes) > 0:
        fig_plotly.add_trace(go.Scatter3d(
            x=nodes_array[:, 0],
            y=nodes_array[:, 1],
            z=nodes_array[:, 2],
            mode='markers',
            name='Mesh Nodes',
            marker=dict(size=2, color='gray', opacity=0.5),
            showlegend=True
        ))
    
    # Calculate aspect ratio for real proportions
    fig_plotly.update_layout(
        title='3D Mesh Visualization (Interactive)',
        scene=dict(
            xaxis_title='X (m)',
            yaxis_title='Y (m)',
            zaxis_title='Z (m)',
            xaxis=dict(range=[0, domain_x]),
            yaxis=dict(range=[0, domain_y]),
            zaxis=dict(range=[domain_z_bottom, 0]),
            aspectmode='manual',
            aspectratio=dict(
                x=x_range/max_range, 
                y=y_range/max_range, 
                z=z_range/max_range
            )
        ),
        width=1200,
        height=800
    )
    
    html_file = 'results/mesh_3d_interactive.html'
    fig_plotly.write_html(html_file)
    print(f"   ✓ Saved interactive visualization: {html_file}")
except ImportError:
    print("   (Install plotly for interactive HTML visualization: pip install plotly)")

plt.close(fig)  # Close to avoid display issues in headless mode

print("\n" + "=" * 60)
print("Mesh Visualization Complete!")
print("=" * 60)
print(f"\nSummary:")
print(f"  Total elements: {mesh.num_cells()}")
print(f"  Total nodes: {mesh.num_vertices()}")
print(f"  Barrette elements: {barrette_elements_count}")
print(f"  Soil elements: {mesh.num_cells() - barrette_elements_count}")
print(f"\nVisualization files:")
print(f"  - {mesh_plot_file}")
if 'html_file' in locals():
    print(f"  - {html_file}")

