# Quick Start Guide

Get started with the barrette analysis in one simple step:

## Run Analysis

```bash
./run_analysis.sh
```

This script:
1. Generates the CalculiX input file (`input/barrette_analysis.inp`)
2. Runs the CalculiX analysis
3. Converts results to VTK format
4. Adds material IDs for visualization

## View Results

After running `./run_analysis.sh`, all results are in the `results/` folder.

**Open in ParaView:**
```bash
cd results
paraview
# Then: File → Open → Select ALL .vtk files (barrette_analysis.01.vtk through .11.vtk)
```

**Key Files:**
- `input/barrette_analysis.inp` - CalculiX input file (generated)
- `results/barrette_analysis.01.vtk` through `.11.vtk` - VTK files for each load step
- `results/barrette_analysis.vtk` - Single file (last load step)
- `results/barrette_analysis.frd` - CalculiX results file

**ParaView Tips:**
- Select all VTK files → ParaView creates time series automatically!
- Use time slider to switch between load cases
- Color by MaterialID to see barrette vs soil
- Apply "Warp by Vector" filter to see deformed shape

## Modify Parameters

Edit `config.py` to change:
- Barrette dimensions
- Material properties
- Mesh density
- Load values

Then run: `./run_analysis.sh` (it will regenerate the input file automatically)

That's it! 🎉
