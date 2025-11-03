#!/bin/bash
# Run CalculiX barrette analysis
# This script generates the input file and runs the analysis

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CALCULIX_DIR="$SCRIPT_DIR/../tools/calculix"
CCX_EXE="$CALCULIX_DIR/CalculiX/ccx_2.22/src/ccx_2.22"

echo "=========================================="
echo "Barrette Analysis - CalculiX"
echo "=========================================="
echo ""

# Step 1: Generate input file
echo "[1/3] Generating CalculiX input file..."
cd "$SCRIPT_DIR"
python3 create_barrette_inp.py

if [ ! -f "barrette_analysis.inp" ]; then
    echo "ERROR: Failed to generate input file"
    exit 1
fi

echo "   ✓ Input file generated: barrette_analysis.inp"
echo ""

# Step 2: Run CalculiX
echo "[2/3] Running CalculiX analysis..."
if [ ! -f "$CCX_EXE" ]; then
    echo "ERROR: CalculiX executable not found at: $CCX_EXE"
    echo "Please check CalculiX installation"
    exit 1
fi

# Change to CalculiX directory and run
cd "$(dirname "$CCX_EXE")"
"$CCX_EXE" -i "$SCRIPT_DIR/barrette_analysis" 2>&1 | tee "$SCRIPT_DIR/results/calculix_output.log"

echo ""
echo "[3/3] Analysis complete!"
echo ""
echo "Output files:"
echo "  - barrette_analysis.frd (results file)"
echo "  - barrette_analysis.dat (data file)"
echo "  - results/calculix_output.log (log file)"
echo ""
echo "To visualize results, run: ./visualize_results.sh"

