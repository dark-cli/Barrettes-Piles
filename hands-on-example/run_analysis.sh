#!/bin/bash
# Run CalculiX barrette analysis and export to VTK
# This script generates input file, runs analysis, and converts results to VTK

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CALCULIX_DIR="$SCRIPT_DIR/../tools/calculix"
CCX_EXE="$CALCULIX_DIR/CalculiX/ccx_2.22/src/ccx_2.22"
RESULTS_FILE="$SCRIPT_DIR/barrette_analysis.frd"
VTK_FILE="$SCRIPT_DIR/barrette_analysis.vtk"

echo "=========================================="
echo "Barrette Analysis - CalculiX"
echo "=========================================="
echo ""

# Step 1: Generate input file
echo "[1/4] Generating CalculiX input file..."
cd "$SCRIPT_DIR"
python3 create_barrette_inp.py

if [ ! -f "barrette_analysis.inp" ]; then
    echo "ERROR: Failed to generate input file"
    exit 1
fi

echo "   ✓ Input file generated: barrette_analysis.inp"
echo ""

# Step 2: Run CalculiX
echo "[2/4] Running CalculiX analysis..."
if [ ! -f "$CCX_EXE" ]; then
    echo "ERROR: CalculiX executable not found at: $CCX_EXE"
    echo "Please check CalculiX installation"
    exit 1
fi

# Change to CalculiX directory and run
cd "$(dirname "$CCX_EXE")"
mkdir -p "$SCRIPT_DIR/results"
"$CCX_EXE" -i "$SCRIPT_DIR/barrette_analysis" 2>&1 | tee "$SCRIPT_DIR/results/calculix_output.log"

if [ ! -f "$RESULTS_FILE" ]; then
    echo "ERROR: Analysis failed - no results file created"
    exit 1
fi

echo "   ✓ Analysis complete"
echo ""

# Step 3: Convert FRD to VTK
echo "[3/4] Converting results to VTK format..."
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

# Convert FRD to VTK
echo "   Running: $CONVERTER \"$RESULTS_FILE\" vtk"
$CONVERTER "$RESULTS_FILE" vtk > /dev/null 2>&1 || true

# Verify VTK file was created
VTK_CREATED=false
if [ -f "$VTK_FILE" ]; then
    VTK_CREATED=true
    echo "   ✓ VTK file created: barrette_analysis.vtk"
else
    # Try alternative naming
    ALT_VTK="${RESULTS_FILE%.frd}_0001.vtk"
    if [ -f "$ALT_VTK" ]; then
        mv "$ALT_VTK" "$VTK_FILE"
        VTK_CREATED=true
        echo "   ✓ VTK file created: barrette_analysis.vtk"
    else
        echo "   ⚠️  Warning: VTK conversion may have failed"
        echo "   Check if ccx2paraview worked correctly"
    fi
fi

# Add material IDs to VTK files for better visualization
if [ "$VTK_CREATED" = true ] && [ -f "$SCRIPT_DIR/add_material_ids.py" ] && [ -f "$SCRIPT_DIR/barrette_analysis.inp" ]; then
    echo "   Adding material IDs to VTK files for ParaView visualization..."
    # Add MaterialID to each step file
    for vtk_step in "$SCRIPT_DIR"/barrette_analysis.[0-9][0-9].vtk; do
        if [ -f "$vtk_step" ]; then
            python3 "$SCRIPT_DIR/add_material_ids.py" "$SCRIPT_DIR/barrette_analysis.inp" "$vtk_step" "$vtk_step" >/dev/null 2>&1
        fi
    done
    # Also add to main file if it exists
    if [ -f "$VTK_FILE" ]; then
        python3 "$SCRIPT_DIR/add_material_ids.py" "$SCRIPT_DIR/barrette_analysis.inp" "$VTK_FILE" "$VTK_FILE" >/dev/null 2>&1
    fi
    echo "   ✓ Material IDs added to all VTK files"
fi


echo ""
echo "[4/4] Complete!"
echo ""
echo "Output files:"
echo "  - barrette_analysis.01.vtk through .11.vtk (VTK files for each load step)"
echo "  - barrette_analysis.vtk (single file: step 11 / 8000 kN)"
echo "  - barrette_analysis.frd (CalculiX results file)"
echo "  - barrette_analysis.dat (data file)"
echo "  - results/calculix_output.log (log file)"
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  🎯 RECOMMENDED: Open ALL .vtk files in ParaView"
echo "     Select all 11 files → ParaView treats them as time series!"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "  Steps:"
echo "    1. paraview"
echo "    2. File → Open"
echo "    3. Select ALL: barrette_analysis.01.vtk through .11.vtk"
echo "    4. Click OK → Time slider appears automatically!"
echo ""
echo "  Features:"
echo "    • Use time slider to switch between load cases (1-11)"
echo "    • Click play button for animation"
echo "    • Color by MaterialID to see barrette vs soil"
echo "    • Watch how displacement increases with load"
echo ""
echo "  See OPEN_IN_PARAVIEW.md for detailed instructions"

