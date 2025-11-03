#!/usr/bin/env python3
"""
Add material IDs to VTK file based on element sets from CalculiX input file.
This allows ParaView to color barrette and soil differently.
"""

import sys
import os
import re

def read_element_sets(inp_file):
    """Read element sets from CalculiX input file."""
    barrette_elements = set()
    soil_elements = set()
    
    current_set = None
    
    with open(inp_file, 'r') as f:
        for line in f:
            line = line.strip()
            if '*ELEMENT' in line and 'EBARRETTE' in line:
                current_set = 'barrette'
            elif '*ELEMENT' in line and 'ESOIL' in line:
                current_set = 'soil'
            elif line.startswith('*') and current_set:
                current_set = None
            elif current_set == 'barrette' and line and line[0].isdigit():
                # Extract element ID (first number in comma-separated line)
                elem_id = int(line.split(',')[0])
                barrette_elements.add(elem_id)
            elif current_set == 'soil' and line and line[0].isdigit():
                elem_id = int(line.split(',')[0])
                soil_elements.add(elem_id)
    
    return barrette_elements, soil_elements

def add_material_ids_to_vtk(vtk_file, barrette_elements, output_file=None):
    """Add material ID array to VTK file."""
    if output_file is None:
        output_file = vtk_file
    
    # Read VTK file
    with open(vtk_file, 'r') as f:
        lines = f.readlines()
    
    # Find CELL_TYPES section to get actual cell count and insertion point
    cell_types_start = None
    cell_types_end = None
    num_cells = 0
    
    for i, line in enumerate(lines):
        if 'CELL_TYPES' in line:
            cell_types_start = i
            # Use CELL_TYPES count as it's the actual number of cells
            parts = line.split()
            num_cells = int(parts[1]) if len(parts) > 1 else 0
            # Find end of CELL_TYPES section (after all type numbers)
            # CELL_TYPES line + num_cells data lines
            cell_types_end = i + num_cells + 1
        elif 'POINT_DATA' in line or 'CELL_DATA' in line:
            # Stop at first data section if we haven't found end of CELL_TYPES yet
            if cell_types_end is None and cell_types_start is not None:
                # Estimate: CELL_TYPES line + num_cells
                cell_types_end = cell_types_start + num_cells + 1
            break
    
    if cell_types_start is None or num_cells == 0:
        print("ERROR: Could not find CELL_TYPES section or count cells in VTK file")
        return False
    
    if cell_types_end is None:
        cell_types_end = cell_types_start + num_cells + 1
    
    # Create material ID array
    # Read element IDs from VTK file (they should match CalculiX element IDs)
    # VTK element numbering starts at 0, CalculiX starts at 1
    material_ids = []
    
    # Find where element IDs might be stored, or use cell index + 1
    # For now, we'll use a lookup: if CalculiX element ID is in barrette set, mark as 1
    # Otherwise mark as 2 (soil)
    
    # Read element definitions to get IDs (if available)
    # Otherwise, assume VTK cell index i corresponds to CalculiX element i+1
    for i in range(num_cells):
        calc_element_id = i + 1  # VTK uses 0-based, CalculiX uses 1-based
        if calc_element_id in barrette_elements:
            material_ids.append(1)  # Barrette (concrete)
        else:
            material_ids.append(2)  # Soil
    
    # Write modified VTK file
    with open(output_file, 'w') as f:
        # Write everything up to and including CELL_TYPES section
        for i in range(cell_types_end):
            f.write(lines[i])
        
        # Check if CELL_DATA already exists after CELL_TYPES
        has_cell_data = False
        for i in range(cell_types_end, min(cell_types_end + 10, len(lines))):
            if 'CELL_DATA' in lines[i]:
                has_cell_data = True
                break
        
        # Insert CELL_DATA section right after CELL_TYPES
        if not has_cell_data:
            f.write(f"CELL_DATA {num_cells}\n")
        
        f.write("SCALARS MaterialID int 1\n")
        f.write("LOOKUP_TABLE default\n")
        for mat_id in material_ids:
            f.write(f"{mat_id}\n")
        f.write("\n")
        
        # Write rest of file (from after CELL_TYPES)
        for i in range(cell_types_end, len(lines)):
            # Skip existing CELL_DATA header if it exists
            if 'CELL_DATA' in lines[i] and not has_cell_data:
                continue
            f.write(lines[i])
    
    print(f"Added material IDs to: {output_file}")
    print(f"  Barrette elements (MaterialID=1): {sum(1 for m in material_ids if m == 1)}")
    print(f"  Soil elements (MaterialID=2): {sum(1 for m in material_ids if m == 2)}")
    
    return True

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 add_material_ids.py <input.inp> <results.vtk> [output.vtk]")
        sys.exit(1)
    
    inp_file = sys.argv[1]
    vtk_file = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    if not os.path.exists(inp_file):
        print(f"ERROR: Input file not found: {inp_file}")
        sys.exit(1)
    
    if not os.path.exists(vtk_file):
        print(f"ERROR: VTK file not found: {vtk_file}")
        sys.exit(1)
    
    print(f"Reading element sets from: {inp_file}")
    barrette_elements, soil_elements = read_element_sets(inp_file)
    print(f"Found {len(barrette_elements)} barrette elements and {len(soil_elements)} soil elements")
    
    print(f"\nProcessing VTK file: {vtk_file}")
    add_material_ids_to_vtk(vtk_file, barrette_elements, output_file)
    
    if output_file:
        print(f"\n✓ Created: {output_file}")
        print("Open this file in ParaView and color by 'MaterialID' to see barrette vs soil")

