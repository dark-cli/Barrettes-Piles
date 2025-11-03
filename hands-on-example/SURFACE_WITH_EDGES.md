# How to View Surface with Edges in ParaView

## Problem

When opening `.vtk` files in ParaView, the "Surface with Edges" representation option is not available in the **Representation** dropdown for UNSTRUCTURED_GRID datasets with volumetric elements (hexahedrons).

## Why This Happens

The VTK files exported from CalculiX contain:
- **Dataset type**: UNSTRUCTURED_GRID
- **Cell type**: Hexahedrons (8-node brick elements)
- **These are volumetric elements**, not surface elements

ParaView only shows "Surface with Edges" for:
- Surface datasets (POLYDATA)
- 2D elements (triangles, quads)
- After extracting the surface from volumetric meshes

## ✅ Solution: Extract Surface First

To enable "Surface with Edges", you need to extract the surface geometry first:

### Step-by-Step:

1. **Open your VTK file** in ParaView
   - Select the dataset in Pipeline Browser

2. **Apply Extract Surface filter:**
   - Go to: **Filters → Alphabetical → Extract Surface**
   - Or search for "Extract Surface" in the filter search bar
   - Click **Apply**

3. **Now you'll see:**
   - A new `ExtractSurface1` object in Pipeline Browser
   - The representation options now include **"Surface with Edges"**

4. **Select "Surface with Edges":**
   - With `ExtractSurface1` selected
   - In **Properties** panel → **Representation** dropdown
   - Select **"Surface with Edges"**
   - Click **Apply**

5. **Adjust edge appearance (optional):**
   - In **Properties** panel → **Styling** section
   - **Edge Color**: Change to black or any color
   - **Line Width**: Adjust thickness (try 1-2)

## Alternative: Extract Edges Separately

If you want more control over edges:

1. **Apply Extract Edges filter:**
   - **Filters → Alphabetical → Extract Edges**
   - Click **Apply**

2. **Visualize edges separately:**
   - In Pipeline Browser, you'll see the original dataset and `ExtractEdges1`
   - Select `ExtractEdges1`
   - Set representation to **"Surface"** or **"Wireframe"**
   - Adjust color and line width in **Styling**

3. **Show both together:**
   - Keep both datasets visible
   - Use different colors to distinguish surfaces from edges

## Pro Tips

### For Better Edge Visibility:

1. **Adjust edge color:**
   - In **Properties → Styling** when using "Surface with Edges"
   - Set **Edge Color** to **Black** or **Dark Gray** for contrast

2. **For volumetric visualization:**
   - Keep the original dataset with **Surface** representation
   - Apply **Extract Edges** filter on top
   - This shows the volume with highlighted edges

3. **Hide interior edges (only show surface edges):**
   - Use **Extract Surface** first
   - Then **Extract Edges** on the surface
   - This gives only the external edges, not internal mesh lines

### Combining with Warp by Vector:

1. Apply **Extract Surface**
2. Then apply **Warp by Vector** on the extracted surface
3. Select **"Surface with Edges"** on the warped result
4. This shows deformed shape with visible edges

## Example Workflow

```
Original Dataset (barrette_analysis.vtk)
  ↓ [Extract Surface]
ExtractSurface1
  ↓ [Warp by Vector] (optional)
WarpByVector1
  ↓ [Representation: Surface with Edges]
Final visualization with visible edges
```

## Why Extract Surface First?

- **Extract Surface** converts volumetric hexahedrons to surface polygons
- This creates a POLYDATA-like structure
- ParaView then recognizes it as a surface and enables "Surface with Edges" option
- The extracted surface maintains the same geometry but only shows the external faces

## Note on Performance

- Extracting surface creates additional data
- For large meshes, this may take a moment
- The extracted surface has fewer elements (only faces, not volumes)
- This can actually improve rendering performance for visualization

