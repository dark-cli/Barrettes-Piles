# How to Start CalculiX CGX GUI

## Important: CGX Requires a File

CGX **must** be run with a file argument - it doesn't open a blank window.

## Ways to Start CGX

### Option 1: Build Mode (Create Model)
```bash
cd "/home/max/Documents/master/Barrettes Piles/tools/calculix"
./cgx -b start.cgx
```

The `-b` flag opens CGX in "build mode" where you can create geometry.

### Option 2: View Mode (Visualize Results)
```bash
./cgx -v results.frd
```

Opens CGX to view CalculiX results.

### Option 3: Read Solver Input
```bash
./cgx -c model.inp
```

Opens CGX to view/edit a CalculiX input file.

## Interactive Mode

Once CGX opens, you'll see:
- A **3D graphics window** for visualization
- A **command line** at the bottom where you type commands

## Common CGX Commands for Building Models

Type these commands in the CGX window:

```
# Create a point
pnt p1 0.0 0.0 0.0

# Create a line
line l1 p1 1.0 0.0 0.0

# Create a surface
surf s1 l1

# Generate mesh
elty all he8
mesh all

# Save
save model.fbd
```

## Example: Simple Start File

I've created `start.cgx` - a minimal file to get started. Run:

```bash
./cgx -b start.cgx
```

This should open the CGX window!

## Troubleshooting

If no window appears:
1. Make sure you have X11/display server running
2. Check: `echo $DISPLAY` (should show something like `:0` or `:0.0`)
3. Try: `DISPLAY=:0 ./cgx -b start.cgx`
4. CGX window might be hidden - check all windows/desktops

