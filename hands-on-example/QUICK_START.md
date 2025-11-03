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

## Step 3: Visualize Results

```bash
./visualize_results.sh
```

This will:
1. Automatically convert results to VTK format (using CGX)
2. Open ParaView with your results

**In ParaView:**
- Use filters to view displacements, stresses, etc.
- Apply "Warp by Vector" to see deformed shape
- Change coloring to visualize different results

## Modify Parameters

Edit `config.py` to change:
- Barrette dimensions
- Material properties
- Mesh density
- Load values

Then regenerate: `python3 create_barrette_inp.py`

That's it! 🎉
