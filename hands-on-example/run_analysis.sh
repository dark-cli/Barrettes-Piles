#!/bin/bash
# Run CalculiX barrette analysis and export to VTK
# This script generates input file, runs analysis, and converts results to VTK

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CALCULIX_DIR="$SCRIPT_DIR/../tools/calculix"
CCX_EXE="$CALCULIX_DIR/CalculiX/ccx_2.22/src/ccx_2.22"
INPUT_DIR="$SCRIPT_DIR/input"
RESULTS_DIR="$SCRIPT_DIR/results"
INPUT_FILE="$INPUT_DIR/barrette_analysis.inp"
RESULTS_FILE="$RESULTS_DIR/barrette_analysis.frd"
VTK_FILE="$RESULTS_DIR/barrette_analysis.vtk"

# Create directories
mkdir -p "$INPUT_DIR" "$RESULTS_DIR"

echo "=========================================="
echo "Barrette Analysis - CalculiX"
echo "=========================================="
echo ""

# Clean input and results directories
echo "[1/5] Cleaning previous analysis files..."
rm -f "$INPUT_DIR"/*.inp 2>/dev/null || true
rm -f "$RESULTS_DIR"/*.{frd,dat,12d,vtk,sta,cvg,log} 2>/dev/null || true
rm -f "$RESULTS_DIR"/barrette_analysis.[0-9][0-9].vtk 2>/dev/null || true
echo "   ✓ Previous files cleaned"
echo ""

# Step 2: Generate input file
echo "[2/5] Generating CalculiX input file..."
cd "$SCRIPT_DIR"
python3 create_barrette_inp.py

if [ ! -f "$INPUT_FILE" ]; then
    echo "ERROR: Failed to generate input file"
    exit 1
fi

echo "   ✓ Input file generated: input/barrette_analysis.inp"
echo ""

# Step 3: Run CalculiX
echo "[3/5] Running CalculiX analysis..."
if [ ! -f "$CCX_EXE" ]; then
    echo "ERROR: CalculiX executable not found at: $CCX_EXE"
    echo "Please check CalculiX installation"
    exit 1
fi

# Change to CalculiX directory and run (CalculiX expects input file in working directory)
cd "$(dirname "$CCX_EXE")"
# Copy input file to CalculiX directory temporarily (CalculiX looks in current dir)
cp "$INPUT_FILE" ./barrette_analysis.inp
"$CCX_EXE" -i barrette_analysis 2>&1 | tee "$RESULTS_DIR/calculix_output.log"
# Move results back to results directory
mv -f barrette_analysis.frd barrette_analysis.dat barrette_analysis.12d "$RESULTS_DIR/" 2>/dev/null || true
# Clean up temporary input file
rm -f barrette_analysis.inp

if [ ! -f "$RESULTS_FILE" ]; then
    echo "ERROR: Analysis failed - no results file created"
    exit 1
fi

echo "   ✓ Analysis complete"
echo ""

# Step 4: Convert FRD to VTK
echo "[4/5] Converting results to VTK format..."
cd "$SCRIPT_DIR"

# Check for ccx2paraview
if python3 -c "import ccx2paraview" 2>/dev/null; then
    CONVERTER="python3 -m ccx2paraview"
elif command -v ccx2paraview &> /dev/null; then
    CONVERTER="ccx2paraview"
else
    echo "   ⚠️  ccx2paraview not found. Installing..."
    pip3 install --user ccx2paraview > /dev/null 2>&1
    if python3 -c "import ccx2paraview" 2>/dev/null; then
        CONVERTER="python3 -m ccx2paraview"
    else
        echo "ERROR: Failed to install ccx2paraview"
        echo "Install manually: pip3 install ccx2paraview"
        exit 1
    fi
fi

# Convert FRD to VTK (working in results directory)
cd "$RESULTS_DIR"
echo "   Running: $CONVERTER \"barrette_analysis.frd\" vtk"
$CONVERTER barrette_analysis.frd vtk > /dev/null 2>&1 || true
cd "$SCRIPT_DIR"

# Verify VTK file was created
VTK_CREATED=false
cd "$RESULTS_DIR"
if [ -f "barrette_analysis.vtk" ]; then
    VTK_CREATED=true
    echo "   ✓ VTK file created: results/barrette_analysis.vtk"
else
    # Try alternative naming
    ALT_VTK="barrette_analysis_0001.vtk"
    if [ -f "$ALT_VTK" ]; then
        mv "$ALT_VTK" "barrette_analysis.vtk"
        VTK_CREATED=true
        echo "   ✓ VTK file created: results/barrette_analysis.vtk"
    else
        echo "   ⚠️  Warning: VTK conversion may have failed"
        echo "   Check if ccx2paraview worked correctly"
    fi
fi
cd "$SCRIPT_DIR"

# Add material IDs to VTK files for better visualization
if [ "$VTK_CREATED" = true ] && [ -f "$SCRIPT_DIR/add_material_ids.py" ] && [ -f "$INPUT_FILE" ]; then
    echo "   Adding material IDs to VTK files for ParaView visualization..."
    # Add MaterialID to each step file
    for vtk_step in "$RESULTS_DIR"/barrette_analysis.[0-9][0-9].vtk; do
        if [ -f "$vtk_step" ]; then
            python3 "$SCRIPT_DIR/add_material_ids.py" "$INPUT_FILE" "$vtk_step" "$vtk_step" >/dev/null 2>&1
        fi
    done
    # Also add to main file if it exists
    if [ -f "$VTK_FILE" ]; then
        python3 "$SCRIPT_DIR/add_material_ids.py" "$INPUT_FILE" "$VTK_FILE" "$VTK_FILE" >/dev/null 2>&1
    fi
    echo "   ✓ Material IDs added to all VTK files"
fi


echo ""
echo "[5/5] Complete!"
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  📁 File Organization:"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "  Input files:"
echo "    - input/barrette_analysis.inp (CalculiX input file)"
echo ""
echo "  Results files:"
echo "    - results/barrette_analysis.01.vtk through .11.vtk (VTK files for each load step)"
echo "    - results/barrette_analysis.vtk (single file: step 11 / 8000 kN)"
echo "    - results/barrette_analysis.frd (CalculiX results file)"
echo "    - results/barrette_analysis.dat (data file)"
echo "    - results/barrette_analysis.12d (12d file)"
echo "    - results/calculix_output.log (log file)"
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  🎯 RECOMMENDED: Open ALL .vtk files in ParaView"
echo "     Select all 11 files from results/ → ParaView treats them as time series!"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "  Steps:"
echo "    1. paraview"
echo "    2. File → Open"
echo "    3. Navigate to: results/"
echo "    4. Select ALL: barrette_analysis.01.vtk through .11.vtk"
echo "    5. Click OK → Time slider appears automatically!"
echo ""
echo "  Features:"
echo "    • Use time slider to switch between load cases (1-11)"
echo "    • Click play button for animation"
echo "    • Color by MaterialID to see barrette vs soil"
echo "    • Watch how displacement increases with load"
echo ""
echo "  See OPEN_IN_PARAVIEW.md for detailed instructions"

