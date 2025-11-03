# Barrette Analysis with CalculiX

This example recreates the hands-on-example barrette model in CalculiX format.

## Model Description

- **Barrette**: 1.0m × 0.8m × 15.0m deep (rectangular)
- **Domain**: 5.0m × 5.0m × 45.0m deep
- **Mesh**: 20 × 20 × 30 elements (12,000 elements, 13,671 nodes)
- **Materials**: 
  - Concrete: E = 30 GPa, ν = 0.15
  - Soil: E = 10 MPa, ν = 0.3

## Files Created

1. **`barrette_analysis.inp`** - Complete CalculiX input file
2. **`create_barrette_inp.py`** - Python script that generates the .inp file
3. **`barrette_model.cgx`** - CGX geometry script (for visualization)

## How to Use

### Step 1: Generate/Regenerate Input File

If you modify parameters, regenerate the input file:

```bash
cd "/home/max/Documents/master/Barrettes Piles/tools/calculix"
python3 create_barrette_inp.py
```

### Step 2: Run Analysis

```bash
cd CalculiX/ccx_2.22/src
./ccx_2.22 -i ../../../barrette_analysis
```

This will create:
- `barrette_analysis.dat` - Output data file
- `barrette_analysis.frd` - Results file for visualization

### Step 3: Visualize Results

**Option A: Using CGX**
```bash
cd "/home/max/Documents/master/Barrettes Piles/tools/calculix"
./cgx -v barrette_analysis.frd
```

**Option B: Using ParaView**
```bash
paraview barrette_analysis.frd
```

## Model Details

### Geometry
- Barrette centered in domain
- Barrette extends from ground surface (z=0) to z=-15m
- Domain extends 5× characteristic dimension in lateral directions
- Domain extends 2× embedment depth below barrette base

### Boundary Conditions
- **Bottom**: Fixed (all displacements = 0)
- **Lateral faces**: Roller supports (zero horizontal displacement)
- **Top**: Free (except where barrette load is applied)

### Loading
- Vertical pressure applied to barrette top surface
- First load increment: 100 kN (from LOAD_INCREMENTS list)

### Materials
- **Concrete**: Linear elastic (for barrette elements)
- **Soil**: Linear elastic (for soil elements)

## Notes

- This is a **linear elastic** analysis (same as hands-on-example)
- For non-linear analysis with Mohr-Coulomb soil, you would need to:
  1. Add `*PLASTIC` material definition for soil
  2. Use `*MOHR COULOMB` keyword with c' and φ' parameters
  3. Use `*STATIC` analysis with iterations

## Modifying Parameters

Edit `create_barrette_inp.py` to change:
- Barrette dimensions
- Material properties
- Mesh density
- Load values

Then regenerate: `python3 create_barrette_inp.py`

