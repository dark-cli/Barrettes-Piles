# Quick Start Guide

Get started with the barrette analysis in 3 simple steps:

## Step 1: Generate Input File

```bash
python3 create_barrette_inp.py
```

This creates `barrette_analysis.inp` with your model configuration.

## Step 2: Run Analysis

```bash
./run_analysis.sh
```

Or manually:
```bash
cd ../tools/calculix/CalculiX/ccx_2.22/src
./ccx_2.22 -i ../../../../hands-on-example/barrette_analysis
```

## Step 3: View Results

After running `./run_analysis.sh`, you'll have `barrette_analysis.vtk`.

**Open in ParaView:**
```bash
paraview barrette_analysis.vtk
```

**Or any VTK viewer:**
- The VTK file contains all results (displacements, stresses, strains)
- Use ParaView filters to visualize different components
- Apply "Warp by Vector" to see deformed shape

## Modify Parameters

Edit `config.py` to change:
- Barrette dimensions
- Material properties
- Mesh density
- Load values

Then regenerate: `python3 create_barrette_inp.py`

That's it! 🎉
