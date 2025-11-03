#!/usr/bin/env python3
"""
Generate CalculiX input file for barrette analysis
Recreates the hands-on-example model
"""

# Parameters from hands-on-example config.py
BARRETTE_LENGTH = 1.0      # m
BARRETTE_WIDTH = 0.8       # m
BARRETTE_DEPTH = 15.0      # m
DOMAIN_LATERAL = 5.0       # multiples
DOMAIN_DEPTH = 2.0         # multiples
E_CONCRETE = 30e6          # kN/m²
NU_CONCRETE = 0.15
GAMMA_CONCRETE = 24.0      # kN/m³
E_SOIL = 10000             # kN/m²
NU_SOIL = 0.3
GAMMA_SOIL = 18.0          # kN/m³
MESH_DENSITY_X = 20
MESH_DENSITY_Y = 20
MESH_DENSITY_Z = 30
LOAD_INCREMENTS = [100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]  # kN

# Calculate domain dimensions
char_dim = max(BARRETTE_LENGTH, BARRETTE_WIDTH)
domain_x = char_dim * DOMAIN_LATERAL
domain_y = char_dim * DOMAIN_LATERAL
domain_z_top = 0.0
domain_z_bottom = -(BARRETTE_DEPTH * (1 + DOMAIN_DEPTH))

print("Generating CalculiX input file for barrette analysis...")
print(f"Barrette: {BARRETTE_LENGTH}m × {BARRETTE_WIDTH}m × {BARRETTE_DEPTH}m deep")
print(f"Domain: {domain_x}m × {domain_y}m × {abs(domain_z_bottom)}m deep")

# Barrette center and bounds
barrette_x_center = domain_x / 2
barrette_y_center = domain_y / 2
barrette_x_min = barrette_x_center - BARRETTE_LENGTH / 2
barrette_x_max = barrette_x_center + BARRETTE_LENGTH / 2
barrette_y_min = barrette_y_center - BARRETTE_WIDTH / 2
barrette_y_max = barrette_y_center + BARRETTE_WIDTH / 2

# Create mesh grid
nx = MESH_DENSITY_X + 1
ny = MESH_DENSITY_Y + 1
nz = MESH_DENSITY_Z + 1

# Generate nodes
nodes = []
node_id = 1
for k in range(nz):
    z = domain_z_bottom + (domain_z_top - domain_z_bottom) * k / (nz - 1)
    for j in range(ny):
        y = 0.0 + domain_y * j / (ny - 1)
        for i in range(nx):
            x = 0.0 + domain_x * i / (nx - 1)
            nodes.append((node_id, x, y, z))
            node_id += 1

# Generate elements (8-node hexahedral)
elements = []
element_id = 1
for k in range(MESH_DENSITY_Z):
    for j in range(MESH_DENSITY_Y):
        for i in range(MESH_DENSITY_X):
            # Node indices for this element
            n1 = k * nx * ny + j * nx + i + 1
            n2 = k * nx * ny + j * nx + (i + 1) + 1
            n3 = k * nx * ny + (j + 1) * nx + (i + 1) + 1
            n4 = k * nx * ny + (j + 1) * nx + i + 1
            n5 = (k + 1) * nx * ny + j * nx + i + 1
            n6 = (k + 1) * nx * ny + j * nx + (i + 1) + 1
            n7 = (k + 1) * nx * ny + (j + 1) * nx + (i + 1) + 1
            n8 = (k + 1) * nx * ny + (j + 1) * nx + i + 1
            
            # Determine if this is barrette or soil
            # Check center of element
            elem_x = (i + 0.5) * domain_x / MESH_DENSITY_X
            elem_y = (j + 0.5) * domain_y / MESH_DENSITY_Y
            elem_z = domain_z_bottom + (k + 0.5) * (domain_z_top - domain_z_bottom) / MESH_DENSITY_Z
            
            is_barrette = (barrette_x_min <= elem_x <= barrette_x_max and
                          barrette_y_min <= elem_y <= barrette_y_max and
                          elem_z >= -BARRETTE_DEPTH)
            
            material = 1 if is_barrette else 2  # 1=concrete, 2=soil
            
            elements.append((element_id, n1, n2, n3, n4, n5, n6, n7, n8, material))
            element_id += 1

print(f"Generated {len(nodes)} nodes and {len(elements)} elements")

# Find nodes on boundaries
bottom_nodes = []
top_nodes = []
left_nodes = []
right_nodes = []
front_nodes = []
back_nodes = []
barrette_top_nodes = []

for node_id, x, y, z in nodes:
    if abs(z - domain_z_bottom) < 1e-6:
        bottom_nodes.append(node_id)
    if abs(z - domain_z_top) < 1e-6:
        top_nodes.append(node_id)
        # Check if on barrette top
        if (barrette_x_min <= x <= barrette_x_max and
            barrette_y_min <= y <= barrette_y_max):
            barrette_top_nodes.append(node_id)
    if abs(x - 0.0) < 1e-6:
        left_nodes.append(node_id)
    if abs(x - domain_x) < 1e-6:
        right_nodes.append(node_id)
    if abs(y - 0.0) < 1e-6:
        front_nodes.append(node_id)
    if abs(y - domain_y) < 1e-6:
        back_nodes.append(node_id)

print(f"Boundary nodes: bottom={len(bottom_nodes)}, top={len(top_nodes)}, barrette_top={len(barrette_top_nodes)}")

# Write CalculiX input file
output_file = "barrette_analysis.inp"
with open(output_file, 'w') as f:
    f.write("*HEADING\n")
    f.write("Barrette Pile Analysis - Linear Elastic\n")
    f.write("Recreated from hands-on-example\n")
    f.write("*NODE,NSET=Nall\n")
    
    # Write nodes
    for node_id, x, y, z in nodes:
        f.write(f"{node_id},{x:.6f},{y:.6f},{z:.6f}\n")
    
    # Write node sets (write all nodes, one per line with comma)
    f.write("*NSET,NSET=Nbottom\n")
    for i, node_id in enumerate(bottom_nodes):
        f.write(f"{node_id}")
        if i < len(bottom_nodes) - 1:
            f.write(",\n")
        else:
            f.write("\n")
    
    f.write("*NSET,NSET=Ntop\n")
    for i, node_id in enumerate(top_nodes):
        f.write(f"{node_id}")
        if i < len(top_nodes) - 1:
            f.write(",\n")
        else:
            f.write("\n")
    
    f.write("*NSET,NSET=Nbarrette_top\n")
    for i, node_id in enumerate(barrette_top_nodes):
        f.write(f"{node_id}")
        if i < len(barrette_top_nodes) - 1:
            f.write(",\n")
        else:
            f.write("\n")
    
    f.write("*NSET,NSET=Nleft\n")
    for i, node_id in enumerate(left_nodes):
        f.write(f"{node_id}")
        if i < len(left_nodes) - 1:
            f.write(",\n")
        else:
            f.write("\n")
    
    f.write("*NSET,NSET=Nright\n")
    for i, node_id in enumerate(right_nodes):
        f.write(f"{node_id}")
        if i < len(right_nodes) - 1:
            f.write(",\n")
        else:
            f.write("\n")
    
    f.write("*NSET,NSET=Nfront\n")
    for i, node_id in enumerate(front_nodes):
        f.write(f"{node_id}")
        if i < len(front_nodes) - 1:
            f.write(",\n")
        else:
            f.write("\n")
    
    f.write("*NSET,NSET=Nback\n")
    for i, node_id in enumerate(back_nodes):
        f.write(f"{node_id}")
        if i < len(back_nodes) - 1:
            f.write(",\n")
        else:
            f.write("\n")
    
    # Write elements
    f.write("*ELEMENT,TYPE=C3D8,ELSET=EBARRETTE\n")
    for elem in elements:
        if elem[9] == 1:  # Concrete
            f.write(f"{elem[0]},{elem[1]},{elem[2]},{elem[3]},{elem[4]},{elem[5]},{elem[6]},{elem[7]},{elem[8]}\n")
    
    f.write("*ELEMENT,TYPE=C3D8,ELSET=ESOIL\n")
    for elem in elements:
        if elem[9] == 2:  # Soil
            f.write(f"{elem[0]},{elem[1]},{elem[2]},{elem[3]},{elem[4]},{elem[5]},{elem[6]},{elem[7]},{elem[8]}\n")
    
    # Material properties
    f.write("*MATERIAL,NAME=CONCRETE\n")
    f.write("*ELASTIC\n")
    f.write(f"{E_CONCRETE},{NU_CONCRETE}\n")
    f.write("*DENSITY\n")
    f.write(f"{GAMMA_CONCRETE}\n")
    
    f.write("*MATERIAL,NAME=SOIL\n")
    f.write("*ELASTIC\n")
    f.write(f"{E_SOIL},{NU_SOIL}\n")
    f.write("*DENSITY\n")
    f.write(f"{GAMMA_SOIL}\n")
    
    # Solid sections
    f.write("*SOLID SECTION,ELSET=EBARRETTE,MATERIAL=CONCRETE\n")
    f.write("*SOLID SECTION,ELSET=ESOIL,MATERIAL=SOIL\n")
    
    # Create node coordinate lookup dictionary (for efficiency)
    node_coord_dict = {node_id: (x, y, z) for node_id, x, y, z in nodes}
    
    # Define surface for barrette top (for pressure loading)
    # Find barrette elements with top face at z=0
    f.write("*SURFACE,TYPE=ELEMENT,NAME=Sbarrette_top\n")
    # For C3D8 hex elements, face S6 is the top face (nodes 5,6,7,8)
    barrette_top_elements = []
    for elem in elements:
        elem_id, n1, n2, n3, n4, n5, n6, n7, n8, mat = elem
        if mat == 1:  # Barrette element
            # Check if top face nodes are at z=0 and within barrette bounds
            # Top face uses nodes n5, n6, n7, n8
            for node_id in [n5, n6, n7, n8]:
                if node_id in node_coord_dict:
                    x, y, z = node_coord_dict[node_id]
                    # Check if this is top face at ground surface within barrette bounds
                    if abs(z - 0.0) < 1e-6:
                        if (barrette_x_min <= x <= barrette_x_max and
                            barrette_y_min <= y <= barrette_y_max):
                            barrette_top_elements.append(elem_id)
                            break
    
    # Write surface definition (face S6 = top face of hex element)
    for elem_id in barrette_top_elements:
        f.write(f"{elem_id},S6\n")
    
    # Boundary conditions
    f.write("*BOUNDARY\n")
    f.write("Nbottom,1,3\n")  # Fix all DOF at bottom (ux=uy=uz=0)
    f.write("Nleft,1,1\n")   # Fix x-displacement at left (ux=0)
    f.write("Nright,1,1\n") # Fix x-displacement at right (ux=0)
    f.write("Nfront,2,2\n")  # Fix y-displacement at front (uy=0)
    f.write("Nback,2,2\n")  # Fix y-displacement at back (uy=0)
    
    # Load step - apply first load increment
    load_value = LOAD_INCREMENTS[0] if LOAD_INCREMENTS else 1000  # First load increment (kN)
    barrette_area = BARRETTE_LENGTH * BARRETTE_WIDTH  # m²
    pressure = load_value / barrette_area  # kN/m² (positive = compressive downward)
    
    f.write("*STEP\n")
    f.write("*STATIC\n")
    f.write("*DLOAD\n")
    # Apply uniform pressure on barrette top surface
    # P = pressure magnitude (positive = compressive, downward in -Z direction)
    f.write(f"Sbarrette_top,P,{pressure}\n")
    f.write("*NODE FILE\n")
    f.write("U\n")  # Output displacements
    f.write("*EL FILE\n")
    f.write("S,E\n")  # Output stresses and strains
    f.write("*END STEP\n")

print(f"\nCalculiX input file created: {output_file}")
print(f"To run: cd CalculiX/ccx_2.22/src && ./ccx_2.22 -i ../../../barrette_analysis")

