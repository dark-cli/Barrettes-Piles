# Hands-On Example: Linear Elastic FEA Analysis of Barrette Piles

This folder contains a practical Python implementation of finite element analysis for barrette piles using FEniCS.

## Overview

This example demonstrates:
- Linear elastic FEA analysis of barrette piles
- Soil-structure interaction modeling
- Load-displacement behavior under vertical loading
- Basic post-processing and visualization

**Important Limitations:**
- ✅ **Linear elastic analysis only** - No plasticity or soil failure modeling
- ✅ **Uniform mesh** - No adaptive refinement in high-stress areas
- ✅ **Simplified material models** - Linear elastic soil and concrete
- ✅ **Suitable for:** Learning, preliminary analysis, service load analysis
- ❌ **Not suitable for:** Ultimate bearing capacity, failure analysis

## Requirements

### Software Dependencies

- Python 3.7 or higher
- FEniCS (2019.1.0 or later)
- NumPy
- Matplotlib
- SciPy

### Installation

1. **Install FEniCS:**

   For Linux/macOS:
   ```bash
   conda install -c conda-forge fenics
   ```
   
   Or using Docker:
   ```bash
   docker pull quay.io/fenicsproject/stable
   ```

   For detailed installation instructions, see: https://fenicsproject.org/download/

2. **Install other dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## File Structure

```
hands-on-example/
├── barrette_fea.py        # Main analysis script
├── visualize_mesh.py      # Mesh visualization (standalone)
├── utils.py               # Utility functions
├── config.py              # Configuration parameters
├── test_setup.py          # Setup verification script
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── results/               # Output directory
    ├── load_settlement_curve.png
    ├── mesh_3d.png
    └── results.txt
```

## Quick Start

**TL;DR**: Just run the scripts - no setup needed!
```bash
./run_visualize_mesh.sh  # View mesh
./run_analysis.sh         # Run analysis
```

See [QUICK_START.md](./QUICK_START.md) for more details.

## Usage

### Basic Usage

1. **Verify setup** (recommended first step):
   ```bash
   python test_setup.py
   ```
   This will check all dependencies and configuration.

2. **Edit configuration** (optional):
   Open `config.py` and modify parameters as needed:
   - Barrette dimensions
   - Material properties
   - Load increments
   - Mesh density

3. **Visualize mesh** (optional, before running analysis):
   
   **Easiest way** (recommended):
   ```bash
   ./run_visualize_mesh.sh
   ```
   
   **Alternative** (if scripts don't work):
   ```bash
   export PKG_CONFIG_PATH="$HOME/.conda/envs/fenics-env/lib/pkgconfig:$PKG_CONFIG_PATH"
   ~/.conda/envs/fenics-env/bin/python visualize_mesh.py
   ```
   
   This generates a 3D visualization of the mesh without running the full analysis.
   
   **Output:**
   - Always saves: `results/mesh_3d.png` (static image)
   - If display available: Opens interactive 3D window (rotate, zoom, pan)
   - If plotly installed: `results/mesh_3d_interactive.html` (browser-based)

4. **Run analysis:**

   **Easiest way** (recommended):
   ```bash
   ./run_analysis.sh
   ```
   
   **Alternative** (if script doesn't work):
   ```bash
   export PKG_CONFIG_PATH="$HOME/.conda/envs/fenics-env/lib/pkgconfig:$PKG_CONFIG_PATH"
   ~/.conda/envs/fenics-env/bin/python barrette_fea.py
   ```
   
   **Note:** The shell scripts (`run_analysis.sh` and `run_visualize_mesh.sh`) automatically handle:
   - Setting up the FEniCS environment variables
   - Using the correct Python interpreter from the conda environment
   - You don't need to activate conda or source any files manually

5. **View results:**
   - Load-settlement curve: `results/load_settlement_curve.png`
   - Data: `results/results.txt`

### Configuration Options

Key parameters in `config.py`:

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

## Understanding the Code

### Main Components

1. **`barrette_fea.py`**: Main analysis script
   - Geometry and mesh generation
   - Material property assignment
   - Variational formulation
   - Boundary conditions
   - Loading and solving
   - Post-processing

2. **`utils.py`**: Helper functions
   - `construct_D_matrix()`: Creates constitutive matrix
   - `epsilon()`: Computes strain tensor
   - `sigma()`: Computes stress tensor
   - `extract_settlement()`: Extracts displacement at point
   - `create_barrette_region()`: Marks barrette elements

3. **`config.py`**: Configuration parameters
   - All analysis parameters in one place

### Mathematical Formulation

The analysis solves the linear elastic equilibrium equations:

$$[K]\{u\} = \{F\}$$

Where:
- $[K]$ = global stiffness matrix (assembled from elements)
- $\{u\}$ = displacement vector
- $\{F\}$ = force vector

The variational form uses the weak form of equilibrium:

$$\int_{\Omega} \boldsymbol{\sigma}(\mathbf{u}) : \boldsymbol{\epsilon}(\mathbf{v}) \, d\Omega = \int_{\Gamma} \mathbf{t} \cdot \mathbf{v} \, d\Gamma$$

For linear elastic materials:
$$\boldsymbol{\sigma} = \lambda \text{tr}(\boldsymbol{\epsilon}) \mathbf{I} + 2\mu \boldsymbol{\epsilon}$$

Where $\lambda$ and $\mu$ are Lame parameters.

## Interpreting Results

### Load-Settlement Curve

The output shows:
- **Load (kN)**: Applied vertical load
- **Settlement (mm)**: Vertical displacement at barrette top

**What to expect:**
- Linear relationship (since analysis is linear elastic)
- Settlement increases proportionally with load
- No "failure" or ultimate capacity (linear elastic only)

**Limitations:**
- Real soil behavior is non-linear
- This analysis does not capture:
  - Soil yielding or failure
  - Ultimate bearing capacity
  - Progressive failure mechanisms

### When to Use This Analysis

✅ **Suitable for:**
- Preliminary design estimates
- Service load analysis
- Relative comparisons (different geometries)
- Educational purposes
- Understanding FEA workflow

❌ **Not suitable for:**
- Ultimate bearing capacity determination
- Failure analysis
- Final design (without validation)

## Troubleshooting

### Common Issues

1. **FEniCS not found:**
   - Ensure FEniCS is properly installed
   - Check Python environment

2. **Memory errors:**
   - Reduce mesh density in `config.py`
   - Reduce number of load increments

3. **Convergence issues:**
   - This is linear analysis, should always converge
   - Check boundary conditions
   - Verify material properties are reasonable

4. **Results seem unreasonable:**
   - Verify material properties (especially $E$ values)
   - Check domain size is adequate
   - Ensure boundary conditions are correct

## Next Steps

To extend this example:

1. **Add non-linear material models:**
   - Implement Mohr-Coulomb plasticity
   - Add return mapping algorithm

2. **Improve mesh:**
   - Add adaptive refinement
   - Refine near barrette corners

3. **Add features:**
   - Consolidation analysis
   - Time-dependent loading
   - Group effects (multiple barrettes)

4. **Validation:**
   - Compare with analytical solutions
   - Validate against commercial software
   - Compare with field test data

## References

- FEniCS Project: https://fenicsproject.org/
- FEniCS Documentation: https://fenicsproject.org/documentation/
- See main guide: `../02-geotechnical-analysis/finite-element-analysis.md`

## Notes

- This is a **simplified educational example**
- For production analysis, use validated commercial software
- Always validate results against established methods
- Consult with experienced geotechnical engineers for design decisions

