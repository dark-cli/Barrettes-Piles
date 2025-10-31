# Quick Start Guide

## Do I need to source anything?

**No!** The provided shell scripts handle everything automatically.

## Simple Usage

### 1. Visualize the mesh (fast, no analysis):
```bash
./run_visualize_mesh.sh
```

**What happens:**
- ✅ Generates and saves `results/mesh_3d.png` (always)
- ✅ Opens an **interactive 3D window** if you have a display (you can rotate, zoom, pan)
- ✅ Saves interactive HTML file if plotly is installed

**Interactive 3D Window:**
- If you're running locally with a display, a window will pop up
- You can rotate by clicking and dragging
- Zoom with scroll wheel or trackpad
- Pan by holding Shift and dragging
- Close the window when done (the script waits for you to close it)

### 2. Run the full FEA analysis:
```bash
./run_analysis.sh
```

That's it! The scripts automatically:
- ✅ Set up FEniCS environment variables (`PKG_CONFIG_PATH`)
- ✅ Use the correct Python interpreter from the conda environment
- ✅ Handle all the setup for you

## What if the scripts don't work?

If you get errors, you can run manually:

```bash
# Set environment variable (only needed once per terminal session)
export PKG_CONFIG_PATH="$HOME/.conda/envs/fenics-env/lib/pkgconfig:$PKG_CONFIG_PATH"

# Then run:
~/.conda/envs/fenics-env/bin/python visualize_mesh.py
# or
~/.conda/envs/fenics-env/bin/python barrette_fea.py
```

## No `.env` file needed

You don't need a `.env` file. The environment is managed by:
- Conda environment: `$HOME/.conda/envs/fenics-env`
- Environment variables set by the scripts

## Troubleshooting

**If you get "FEniCS is not installed":**
- Make sure FEniCS is installed in the conda environment
- Check: `~/.conda/envs/fenics-env/bin/python -c "import fenics; print('OK')"`

**If you get "Could not find DOLFIN pkg-config file":**
- Make sure `PKG_CONFIG_PATH` is set (the scripts do this automatically)
- Or export it manually: `export PKG_CONFIG_PATH="$HOME/.conda/envs/fenics-env/lib/pkgconfig:$PKG_CONFIG_PATH"`

