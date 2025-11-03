# CalculiX GUI Options for Linux

## Current Status

- ✅ **CCX (Solver)**: Built and working
- ❌ **CGX (Built-in GUI)**: Not available for direct download

## GUI Options

### Option 1: FreeCAD FEM Workbench (Recommended for Linux)

FreeCAD is a native Linux application with FEM workbench that can interface with CalculiX.

**Installation:**
```bash
# Check if available in repositories or install from Flatpak
flatpak install org.freecadweb.FreeCAD
```

**Usage:**
- Create geometry in FreeCAD
- Use FEM workbench to mesh and set up analysis
- Export to CalculiX `.inp` format
- Run CalculiX from command line
- Import results back to FreeCAD for visualization

### Option 2: PrePoMax (Via Wine)

PrePoMax is a modern pre/post-processor for CalculiX.

**Download:**
- Visit: https://prepomax.fs.um.si/
- Download Windows version

**Run with Wine:**
```bash
wine PrePoMax.exe
```

### Option 3: Command-Line Workflow

You can create CalculiX input files manually or with Python scripts:

1. **Create `.inp` files** (ABAQUS format)
2. **Run CalculiX**: `./ccx_2.22 -i jobname`
3. **Visualize results**: Use ParaView or other tools that read `.frd` files

### Option 4: ParaView for Visualization

ParaView can read CalculiX `.frd` result files:

```bash
# Install ParaView
sudo dnf install paraview
# or
flatpak install org.paraview.ParaView
```

Then visualize your `.frd` files with:
```bash
paraview barrette.frd
```

## Quick Start Without GUI

You can create simple input files and run them:

1. Create a text file `test.inp`
2. Run: `./ccx_2.22 -i test`
3. Check results in `test.frd` (can visualize with ParaView)

## Recommended Workflow for Barrettes

For barrette analysis, recommended approach:
1. **Preprocessing**: Use Gmsh or FreeCAD to create geometry and mesh
2. **Material Setup**: Edit `.inp` file to add Mohr-Coulomb soil properties
3. **Solver**: Run CalculiX from command line
4. **Postprocessing**: Visualize with ParaView or import to FreeCAD

Would you like help setting up any of these options?

