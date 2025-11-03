# Hands-On Example: Barrette Pile Analysis with CalculiX

This folder contains a practical implementation of finite element analysis for barrette piles using **CalculiX**, a free and open-source FEA solver.

## Overview

This example demonstrates:
- Linear elastic FEA analysis of barrette piles
- Soil-structure interaction modeling
- Load-displacement behavior under vertical loading
- Preprocessing, solving, and post-processing workflow

**Important Limitations:**
- ✅ **Linear elastic analysis only** - No plasticity or soil failure modeling
- ✅ **Uniform mesh** - No adaptive refinement in high-stress areas
- ✅ **Simplified material models** - Linear elastic soil and concrete
- ✅ **Suitable for:** Learning, preliminary analysis, service load analysis
- ❌ **Not suitable for:** Ultimate bearing capacity, failure analysis

## Requirements

### Software Dependencies

- **CalculiX**: FEA solver (CCX) and pre/post-processor (CGX)
  - Already installed in: `../tools/calculix/`
  - See installation in: `../tools/calculix/README.md`
- **Python 3.7+**: For generating input files
- **NumPy**: For numerical operations (optional, only if extending scripts)

### Installation

1. **CalculiX is already installed** in `../tools/calculix/`

2. **Install Python dependencies** (if not already installed):
   ```bash
   pip install numpy
   ```

## File Structure

```
hands-on-example/
├── config.py                  # Configuration parameters (edit this!)
├── create_barrette_inp.py     # Generates CalculiX input file
├── barrette_analysis.inp      # Generated CalculiX input file
├── run_analysis.sh            # Script to run analysis
├── visualize_results.sh       # Script to visualize results
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── results/                   # Output directory
    ├── barrette_analysis.frd  # Results file (after running)
    └── barrette_analysis.dat   # Output data file
```

## Quick Start

### Option 1: Run Everything (Easiest)

```bash
# Generate input file and run analysis
./run_analysis.sh

# Visualize results
./visualize_results.sh
```

### Option 2: Step-by-Step

1. **Edit configuration** (optional):
   ```bash
   # Edit config.py to modify parameters
   nano config.py
   ```

2. **Generate CalculiX input file**:
   ```bash
   python3 create_barrette_inp.py
   ```

3. **Run analysis**:
   ```bash
   cd ../tools/calculix/CalculiX/ccx_2.22/src
   ./ccx_2.22 -i ../../../../hands-on-example/barrette_analysis
   ```

4. **Visualize results**:
   ```bash
   cd ../../../..
   ./visualize_results.sh
   ```

## Configuration

Edit `config.py` to modify:

**Geometry:**
- `BARRETTE_LENGTH`: Length of barrette (m)
- `BARRETTE_WIDTH`: Width of barrette (m)
- `BARRETTE_DEPTH`: Embedment depth (m)

**Material Properties:**
- `E_SOIL`: Young's modulus of soil (kN/m²)
- `NU_SOIL`: Poisson's ratio of soil
- `E_CONCRETE`: Young's modulus of concrete (kN/m²)
- `NU_CONCRETE`: Poisson's ratio of concrete

**Mesh:**
- `MESH_DENSITY_X/Y/Z`: Number of elements in each direction

**Loading:**
- `LOAD_INCREMENTS`: List of load values (kN)

## Understanding the Workflow

### 1. Input File Generation (`create_barrette_inp.py`)

This Python script:
- Reads parameters from `config.py`
- Generates nodes and elements
- Defines materials (concrete and soil)
- Applies boundary conditions
- Sets up loading
- Creates CalculiX `.inp` file

### 2. Analysis Execution (CalculiX CCX)

The solver:
- Reads the `.inp` file
- Assembles global stiffness matrix
- Solves linear system
- Outputs results to `.frd` and `.dat` files

### 3. Visualization (ParaView)

The results are visualized using **ParaView**:
- Runs `./visualize_results.sh`
- Automatically converts CalculiX `.frd` files to VTK format
- High-quality visualization with excellent graphics
- Advanced filtering capabilities
- Export publication-quality images and animations

**Note:** The script automatically uses CGX to export to VTK format, then opens ParaView.

## Model Details

### Geometry
- Barrette: 1.0m × 0.8m × 15.0m deep (rectangular)
- Domain: 5.0m × 5.0m × 45.0m deep
- Barrette centered in domain

### Mesh
- **13,671 nodes** and **12,000 elements**
- Uniform hexahedral mesh (C3D8 elements)
- 20 × 20 × 30 elements

### Boundary Conditions
- **Bottom**: Fixed (all displacements = 0)
- **Lateral faces**: Roller supports (zero horizontal displacement)
- **Top**: Free (except where barrette load is applied)

### Materials
- **Concrete**: Linear elastic (E = 30 GPa, ν = 0.15)
- **Soil**: Linear elastic (E = 10 MPa, ν = 0.3)

### Loading
- Vertical pressure applied to barrette top surface
- Default: 100 kN (first increment from `LOAD_INCREMENTS`)

## Interpreting Results

### Output Files

- **`barrette_analysis.dat`**: Text output with summary
- **`barrette_analysis.frd`**: Binary results file for visualization

### Viewing Results in ParaView

After running `./visualize_results.sh`, ParaView will open with your results.

**In ParaView:**
- Use filters to view displacements, stresses, etc.
- Apply "Warp by Vector" filter to see deformed shape
- Change coloring to visualize different result components
- Use slice/clip filters to see internal results
- Export high-quality images and animations

The script automatically converts CalculiX `.frd` files to VTK format using CGX before opening ParaView.

## Extending the Example

### Add Multiple Load Steps

Edit `create_barrette_inp.py` to add multiple `*STEP` blocks for different load increments.

### Add Non-Linear Material

For Mohr-Coulomb soil model, modify the material definition:

```python
f.write("*MATERIAL,NAME=SOIL\n")
f.write("*ELASTIC\n")
f.write(f"{E_SOIL},{NU_SOIL}\n")
f.write("*PLASTIC\n")
f.write("*MOHR COULOMB\n")
f.write(f"{COHESION},{FRICTION_ANGLE}\n")  # c', φ'
```

### Refine Mesh

Increase `MESH_DENSITY_X/Y/Z` in `config.py` for finer mesh (takes longer to solve).

## Comparison with FEniCS Version

This CalculiX version replaces the previous FEniCS implementation:

**Advantages:**
- ✅ Industry-standard ABAQUS-like input format
- ✅ Can extend to non-linear materials (Mohr-Coulomb built-in)
- ✅ Can use commercial preprocessors (FreeCAD, Gmsh)
- ✅ No Python dependencies for solver (standalone executable)

**Similarities:**
- Same geometry and material parameters
- Same boundary conditions
- Same linear elastic analysis approach

## Troubleshooting

### CalculiX not found
- Check that CalculiX is installed: `ls ../tools/calculix/CalculiX/ccx_2.22/src/ccx_2.22`
- Add to PATH or use full path in scripts

### CGX window doesn't open
- Check display: `echo $DISPLAY`
- Try: `DISPLAY=:0 ./cgx -v barrette_analysis.frd`

### Analysis fails
- Check input file syntax: `head barrette_analysis.inp`
- Verify boundary conditions are properly defined
- Check material properties are reasonable

## References

- CalculiX Documentation: http://www.dhondt.de/
- Main Guide: `../02-geotechnical-analysis/finite-element-analysis.md`
- CalculiX Installation: `../tools/calculix/README.md`

## Notes

- This is a **simplified educational example**
- For production analysis, use validated commercial software or extend with proper non-linear models
- Always validate results against established methods
- Consult with experienced geotechnical engineers for design decisions
