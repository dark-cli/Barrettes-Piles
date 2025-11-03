#!/bin/bash
# Visualize CalculiX results using ParaView
# Uses ccx2paraview to convert .frd to .vtk format

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RESULTS_FILE="$SCRIPT_DIR/barrette_analysis.frd"

echo "=========================================="
echo "Visualize Results with ParaView"
echo "=========================================="
echo ""

# Check if results file exists
if [ ! -f "$RESULTS_FILE" ]; then
    echo "ERROR: Results file not found: $RESULTS_FILE"
    echo ""
    echo "Please run the analysis first:"
    echo "  ./run_analysis.sh"
    exit 1
fi

# Check if ParaView is installed
if ! command -v paraview &> /dev/null; then
    echo "ParaView is not installed."
    echo ""
    echo "Install ParaView:"
    echo "  sudo dnf install paraview"
    echo "  # or"
    echo "  flatpak install org.paraview.ParaView"
    echo ""
    exit 1
fi

# Check for ccx2paraview (preferred method)
if python3 -c "import ccx2paraview" 2>/dev/null; then
    CONVERTER="python3 -m ccx2paraview"
    CONVERTER_CMD="python3 -m ccx2paraview"
elif command -v ccx2paraview &> /dev/null; then
    CONVERTER="ccx2paraview"
    CONVERTER_CMD="ccx2paraview"
else
    echo "⚠️  ccx2paraview not found. Trying alternative method..."
    echo ""
    echo "Installing ccx2paraview..."
    echo "  pip3 install ccx2paraview"
    echo ""
    
    if pip3 install --user ccx2paraview 2>&1 | grep -q "Successfully installed"; then
        CONVERTER="python3 -m ccx2paraview"
        CONVERTER_CMD="python3 -m ccx2paraview"
        echo "✓ ccx2paraview installed successfully"
    else
        echo ""
        echo "Installation failed. Using CGX as fallback..."
        CONVERTER="cgx"
        CALCULIX_DIR="$SCRIPT_DIR/../tools/calculix"
        CGX_EXE="$CALCULIX_DIR/cgx"
        
        if [ ! -f "$CGX_EXE" ]; then
            echo "ERROR: Neither ccx2paraview nor CGX found."
            echo ""
            echo "Please install ccx2paraview:"
            echo "  pip3 install ccx2paraview"
            exit 1
        fi
    fi
fi

echo "Converting .frd to .vtk format..."
echo "Using: $CONVERTER"
echo ""

cd "$SCRIPT_DIR"

if [ "$CONVERTER" != "cgx" ]; then
    # Use ccx2paraview - requires format argument (vtk or vtu)
    echo "Running: $CONVERTER_CMD \"$RESULTS_FILE\" vtk"
    cd "$SCRIPT_DIR"
    $CONVERTER_CMD "$RESULTS_FILE" vtk 2>&1 | grep -v "^$" || true
    
    # Find VTK files created - ccx2paraview creates file with same base name
    # ccx2paraview creates: barrette_analysis.vtk (same name as .frd, but .vtk extension)
    BASE_NAME=$(basename "$RESULTS_FILE" .frd)
    VTK_FILE="$SCRIPT_DIR/${BASE_NAME}.vtk"
    
    # If not found, search for any .vtk file
    if [ ! -f "$VTK_FILE" ]; then
        VTK_FILE=$(find "$SCRIPT_DIR" -maxdepth 1 -name "*.vtk" -type f | head -1)
    fi
    
    # Last resort - try patterns with numbers
    if [ -z "$VTK_FILE" ] || [ ! -f "$VTK_FILE" ]; then
        VTK_FILE="${RESULTS_FILE%.frd}_0001.vtk"
    fi
else
    # Fallback to CGX
    echo "Using CGX to export (this may open a window briefly)..."
    CGX_CMDS="$SCRIPT_DIR/export_to_vtk_temp.fbl"
    cat > "$CGX_CMDS" << 'EOF'
plot ea all
show ea all
send all abq
quit
EOF
    "$CGX_EXE" -v "$RESULTS_FILE" < "$CGX_CMDS" > /dev/null 2>&1 || true
    sleep 3
    pkill -f "cgx.*$RESULTS_FILE" 2>/dev/null || true
    rm -f "$CGX_CMDS"
    
    # CGX creates .inp files, not .vtk - this won't work well
    VTK_FILE=""
fi

# Check if VTK file exists
if [ -z "$VTK_FILE" ] || [ ! -f "$VTK_FILE" ]; then
    echo ""
    echo "ERROR: VTK conversion failed. No .vtk files found."
    echo ""
    echo "Searching for VTK files..."
    find "$SCRIPT_DIR" -maxdepth 1 -name "*.vtk" -type f
    
    echo ""
    echo "Files in directory:"
    ls -lh "$SCRIPT_DIR"/*.{frd,dat} 2>/dev/null | head -5 || true
    echo ""
    echo "Try manual conversion:"
    echo "  cd \"$SCRIPT_DIR\""
    echo "  ccx2paraview \"$RESULTS_FILE\""
    echo "  ls -lh *.vtk"
    exit 1
fi

# Verify file exists and get absolute path
if [ ! -f "$VTK_FILE" ]; then
    echo "ERROR: VTK file not found: $VTK_FILE"
    exit 1
fi

# Get absolute path to avoid space issues
# Use python to get absolute path reliably, handling spaces
VTK_FILE_ABS=$(python3 -c "import os; print(os.path.abspath('$VTK_FILE'))" 2>/dev/null)

# Verify absolute path exists
if [ ! -f "$VTK_FILE_ABS" ]; then
    VTK_FILE_ABS="$VTK_FILE"
fi

echo "✓ VTK file created: $(basename "$VTK_FILE")"
echo "  Full path: $VTK_FILE_ABS"
echo ""

# Verify file exists before opening
if [ ! -f "$VTK_FILE_ABS" ]; then
    echo "ERROR: VTK file does not exist: $VTK_FILE_ABS"
    echo "Please check if conversion succeeded."
    exit 1
fi

echo "Opening ParaView..."
echo ""

# Open ParaView - properly quote path with spaces
cd "$SCRIPT_DIR"

# Create a simple script to launch ParaView with the file
# This avoids shell quoting issues with spaces in paths
LAUNCH_SCRIPT="/tmp/launch_paraview.sh"
cat > "$LAUNCH_SCRIPT" << EOF
#!/bin/bash
paraview "$VTK_FILE_ABS"
EOF
chmod +x "$LAUNCH_SCRIPT"

"$LAUNCH_SCRIPT" &
sleep 1
rm -f "$LAUNCH_SCRIPT"

echo "ParaView is opening with your results..."
echo ""
echo "In ParaView:"
echo "  ✓ Your model should be loaded automatically"
echo "  ✓ Use Filters menu to view displacements/stresses"
echo "  ✓ Apply 'Warp by Vector' to see deformed shape"
echo "  ✓ Use coloring to visualize different result components"
echo ""
