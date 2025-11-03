# CalculiX Barrette Example

This directory contains a complete CalculiX model that recreates the hands-on-example barrette analysis.

## Files

1. **`create_barrette_inp.py`** - Python script that generates the CalculiX input file
2. **`barrette_analysis.inp`** - Generated CalculiX input file (ready to run)
3. **`barrette_model.cgx`** - CGX geometry script (for visualization/preprocessing)
4. **`BARRETTE_EXAMPLE.md`** - Detailed documentation

## Quick Start

### 1. Generate the Input File

The input file is already generated, but if you modify parameters, regenerate it:

```bash
cd "/home/max/Documents/master/Barrettes Piles/tools/calculix"
python3 create_barrette_inp.py
```

### 2. Run the Analysis

```bash
cd CalculiX/ccx_2.22/src
./ccx_2.22 -i ../../../barrette_analysis
```

### 3. Visualize Results in CGX

```bash
cd "/home/max/Documents/master/Barrettes Piles/tools/calculix"
./cgx -v barrette_analysis.frd
```

In CGX, you can:
- View displacements: Type `plot u all`
- View stresses: Type `plot sy all`
- Rotate, zoom, pan with mouse
- Export images

## Model Summary

- **13,671 nodes** and **12,000 elements**
- **Barrette**: 1.0m × 0.8m × 15.0m deep
- **Domain**: 5.0m × 5.0m × 45.0m deep
- **Materials**: Concrete (E=30 GPa) and Soil (E=10 MPa)
- **Load**: 100 kN vertical pressure on barrette top

## Using CGX for Preprocessing (Alternative)

If you want to use CGX interactively to build models:

```bash
./cgx -b barrette_model.cgx
```

Then in CGX window, you can type commands to modify the model. This is more for learning/exploration - the Python script approach is more practical for this example.

## Next Steps

- Modify `create_barrette_inp.py` to change parameters
- Add non-linear material models (Mohr-Coulomb)
- Run multiple load increments
- Compare results with hands-on-example output

