# How to Start CalculiX GUI (CGX)

## ✅ CGX is Installed!

**Location**: `/home/max/Documents/master/Barrettes Piles/tools/calculix/cgx`

## How to Start the GUI

### Option 1: Run from the calculix directory

```bash
cd "/home/max/Documents/master/Barrettes Piles/tools/calculix"
./cgx
```

### Option 2: Add to PATH (recommended)

Add this to your `~/.zshrc` or `~/.bashrc`:

```bash
export PATH=$PATH:"/home/max/Documents/master/Barrettes Piles/tools/calculix"
export PATH=$PATH:"/home/max/Documents/master/Barrettes Piles/tools/calculix/CalculiX/ccx_2.22/src"
```

Then you can run from anywhere:
```bash
cgx              # Start GUI
ccx_2.22 -i job  # Run solver
```

## What CGX Does

CGX (CalculiX GraphiX) provides a **graphical interface** where you can:

1. **Create geometry** - Draw or import 3D models
2. **Generate mesh** - Create finite element mesh
3. **Define materials** - Set up material properties (including Mohr-Coulomb for soil)
4. **Apply loads and boundary conditions** - Set up your analysis
5. **Export to CalculiX format** - Generate `.inp` files for the solver
6. **Visualize results** - View analysis results after running CCX

## Complete Workflow

1. **Start CGX**: `./cgx`
2. **Create your model** in the GUI (mostly command-driven, but with visual feedback)
3. **Export**: Save as `.inp` file
4. **Run solver**: `ccx_2.22 -i jobname` (from terminal)
5. **View results**: Load `.frd` file back into CGX to visualize

## Important Note

CGX is **mostly command-driven** - you type commands (like a CAD program from the 90s). But you get:
- Visual 3D graphics window
- Mouse interaction for selection
- Real-time visualization
- Results plotting

This is different from modern click-based GUIs, but it's the official CalculiX interface.

## Alternative: PrePoMax

For a more modern click-based GUI, you can use **PrePoMax** (runs via Wine on Linux).

