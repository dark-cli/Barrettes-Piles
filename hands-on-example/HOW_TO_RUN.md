# How to Run the Analysis and View Results

## Method 1: Using Scripts (Easiest)

### Run the Analysis

```bash
cd "/home/max/Documents/master/Barrettes Piles/hands-on-example"
./run_analysis.sh
```

This script will:
1. Generate the CalculiX input file (`barrette_analysis.inp`)
2. Run the CalculiX solver
3. Create output files in the `results/` directory

**Expected output:**
- `barrette_analysis.frd` - Results file for visualization
- `barrette_analysis.dat` - Data output file
- `results/calculix_output.log` - Log file

### Visualize Results

```bash
./visualize_results.sh
```

This opens CGX (CalculiX GraphiX) to view your results.

## Method 2: Manual Steps

### Step 1: Generate Input File

```bash
cd "/home/max/Documents/master/Barrettes Piles/hands-on-example"
python3 create_barrette_inp.py
```

This creates `barrette_analysis.inp`.

### Step 2: Run CalculiX Solver

```bash
cd "../tools/calculix/CalculiX/ccx_2.22/src"
./ccx_2.22 -i "../../../../hands-on-example/barrette_analysis"
```

The analysis will run and create:
- `barrette_analysis.frd` (in hands-on-example directory)
- `barrette_analysis.dat` (in hands-on-example directory)

### Step 3: Visualize Results

```bash
cd "../../../.."
cd "hands-on-example"
../tools/calculix/cgx -v barrette_analysis.frd
```

## Viewing Results in CGX

Once CGX opens, you'll see a 3D graphics window. Type these commands at the bottom:

### Basic Commands

```
plot ea all          # Show all elements
plot u all           # View displacements (vector)
plot uy all          # View Y-direction displacements (scalar)
plot s all           # View all stress components
plot sy all          # View Y-direction (vertical) stress
plot sz all          # View Z-direction stress
```

### View Controls

```
rot x 30             # Rotate 30° around X-axis
rot y 45             # Rotate 45° around Y-axis
rot z 60             # Rotate 60° around Z-axis
zoom 2               # Zoom in (factor of 2)
zoom 0.5             # Zoom out (factor of 0.5)
cent all             # Center view on all elements
```

### Sectioning (Hide Parts)

```
send all abq         # Export current view to ABAQUS format
hide ea all           # Hide all elements
show ea EBARRETTE     # Show only barrette elements
show ea ESOIL         # Show only soil elements
```

### Exit

```
quit                 # Exit CGX
```

## Understanding the Output

### Displacements (`plot u all`)

- Shows how much each node has moved
- Color indicates magnitude
- Red = large displacement, blue = small displacement
- For barrette analysis, expect largest displacements at the top

### Stresses (`plot sy all`)

- Shows stress in Y-direction (vertical)
- Color indicates magnitude
- Red = high stress (compressive or tensile)
- Blue = low stress
- For barrette analysis, expect high stresses at barrette tip and near load application

### Expected Results

For a 100 kN load on the barrette:
- **Settlement**: ~2-5 mm (vertical displacement at top)
- **Stress concentration**: At barrette tip and corners
- **Stress distribution**: Gradually decreases with depth in soil

## Troubleshooting

### "Command not found" errors

Make sure scripts are executable:
```bash
chmod +x run_analysis.sh visualize_results.sh
```

### CGX window doesn't open

Check display:
```bash
echo $DISPLAY
```

If empty, try:
```bash
DISPLAY=:0 ./visualize_results.sh
```

### Analysis takes too long

The model has 12,000 elements, so it may take 1-5 minutes depending on your computer.

### No results file

Check that analysis completed successfully:
```bash
ls -lh barrette_analysis.frd
```

If file doesn't exist, check the log:
```bash
cat results/calculix_output.log
```

## Next Steps

- Modify `config.py` to change parameters
- Add more load increments
- Compare results with analytical solutions
- Extend to non-linear analysis (Mohr-Coulomb)

