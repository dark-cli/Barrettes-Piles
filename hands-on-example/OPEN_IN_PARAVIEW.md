# How to View All Load Cases in ParaView

## Problem with PVD File

ParaView's PVD reader doesn't work well with legacy ASCII VTK files (`.vtk` format). The files created by `ccx2paraview` are in legacy format, which causes the "Could not determine the data type" error.

## ✅ Solution: Open Multiple Files Directly

ParaView has built-in support for time series when opening multiple files. Use this method:

### Method 1: Select All Files (Recommended)

1. **Open ParaView:**
   ```bash
   paraview
   ```

2. **File → Open:**
   - Navigate to: `hands-on-example/` directory
   - **Select ALL 11 VTK files at once:**
     - `barrette_analysis.01.vtk`
     - `barrette_analysis.02.vtk`
     - `barrette_analysis.03.vtk`
     - ... through ...
     - `barrette_analysis.11.vtk`
   
   **How to select multiple:**
   - **Linux/Windows:** Hold `Ctrl` and click each file
   - **Mac:** Hold `Cmd` and click each file
   - Or: Click first file, hold `Shift`, click last file (selects range)

3. **Important:** Check "Group files into series" in the file dialog if available

4. **Click "OK"**

5. **ParaView will:**
   - Load all files as a time series
   - Show time slider at the bottom (steps 1-11)
   - Allow animation with play button
   - Each step corresponds to a different load case

### Method 2: File Pattern (If Available)

Some ParaView versions support file patterns:

1. **File → Open**
2. Navigate to `hands-on-example/` directory
3. Look for "Pattern" or "Filter" option in file dialog
4. Enter: `barrette_analysis.*.vtk`
5. ParaView should detect all matching files as a series

### Using the Time Animation

Once files are loaded:

1. **Time Slider:** Bottom of ParaView window
   - Drag to jump to any load step (1-11)
   - Step 1 = 100 kN
   - Step 11 = 8000 kN

2. **Play Button:** ▶ Click to animate through all steps

3. **Color by MaterialID:**
   - Select dataset in Pipeline Browser
   - In Properties panel, choose "MaterialID" from Coloring dropdown
   - Barrette (ID=1) and soil (ID=2) have different colors

4. **Watch Displacement:**
   - Color by "U_Magnitude" or "U" components
   - See how displacement increases with load

## Load Steps Reference

| Step | Load (kN) | Pressure (kN/m²) |
|------|-----------|------------------|
| 1    | 100       | 22.22           |
| 2    | 200       | 44.44           |
| 3    | 500       | 111.11          |
| 4    | 1000      | 222.22          |
| 5    | 2000      | 444.44          |
| 6    | 3000      | 666.67          |
| 7    | 4000      | 888.89          |
| 8    | 5000      | 1111.11         |
| 9    | 6000      | 1333.33         |
| 10   | 7000      | 1555.56         |
| 11   | 8000      | 1777.78         |

## Alternative: Open Individual Files

If the time series method doesn't work, you can open files individually:

```bash
paraview barrette_analysis.01.vtk  # 100 kN
paraview barrette_analysis.11.vtk  # 8000 kN
```

But you'll need to switch between files manually, which is less convenient than the time series method.

## Why PVD Doesn't Work

The VTK files are in **legacy ASCII format** (`.vtk`), not XML format (`.vtu`). ParaView's PVD reader expects XML files or needs explicit type specification. Converting to XML format would require additional processing that's not currently implemented.

The multi-file selection method is actually **simpler and more reliable** than PVD files for this use case!

