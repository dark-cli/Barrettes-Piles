# ParaView Visualization Guide

## Issue: Barrette Looks Square / Can't See Soil

### Quick Fix

1. **Open the VTK file in ParaView:**
   ```bash
   paraview barrette_analysis.vtk
   ```

2. **Color by MaterialID:**
   - In the **Properties** panel (when `barrette_analysis.vtk` is selected)
   - Find **Coloring** dropdown
   - Select **MaterialID** from the list
   - The barrette (MaterialID=1) and soil (MaterialID=2) will now have different colors!

3. **To see the rectangular shape:**
   - The barrette is **3.0m × 1.5m** (2:1 aspect ratio)
   - Use **Reset Camera** (View menu) or press `R` to fit view
   - Rotate the view to see the rectangular cross-section
   - The barrette spans only ~4×2 elements, so it may appear small relative to the 15m×15m domain

### Understanding the Model

- **Barrette**: 80 elements (3.0m × 1.5m × 15m deep)
- **Soil**: 11,920 elements (surrounding domain)
- **Total**: 12,000 elements
- **Domain**: 15m × 15m × 45m deep

### ParaView Tips

1. **Adjust Transparency:**
   - Select the dataset
   - In **Properties > Styling**, adjust **Opacity** (try 0.7 for soil)

2. **Use Clip/Slice Filters:**
   - `Filters > Alphabetical > Slice` to see cross-sections
   - `Filters > Alphabetical > Clip` to hide parts

3. **Warp by Displacement:**
   - `Filters > Alphabetical > Warp by Vector`
   - Select displacement field to see deformed shape

4. **Color by Different Fields:**
   - Try coloring by stress (S11, S22, S33)
   - Or by displacement magnitude

5. **Surface with Edges:**
   - The "Surface with Edges" option is not directly available for volumetric meshes
   - **Solution**: Apply `Filters > Alphabetical > Extract Surface` first
   - Then select "Surface with Edges" representation
   - See `SURFACE_WITH_EDGES.md` for detailed instructions

### Why the Barrette Looks Small

The barrette occupies only:
- **20%** of domain width (3.0m / 15m)
- **10%** of domain length (1.5m / 15m)

With a mesh density of 20×20×30, the barrette spans approximately:
- **4 elements** in X direction
- **2 elements** in Y direction
- **20 elements** in Z direction (depth)

This is why it may look small and why the rectangular shape isn't immediately obvious - you need to zoom in and look carefully, or use the MaterialID coloring to distinguish it from soil.

### Increase Mesh Density (Optional)

If you want a more detailed barrette visualization, edit `config.py`:

```python
MESH_DENSITY_X = 40  # Increase from 20
MESH_DENSITY_Y = 40  # Increase from 20
MESH_DENSITY_Z = 60  # Increase from 30
```

This will give you more elements in the barrette, but the analysis will take longer to run.

