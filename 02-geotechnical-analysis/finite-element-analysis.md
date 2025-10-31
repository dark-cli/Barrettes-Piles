# Finite Element Analysis for Barrettes

## Overview

Finite element analysis (FEA) provides a powerful numerical tool for analyzing barrettes, allowing for complex soil-structure interaction, non-linear behavior, and three-dimensional effects that cannot be captured by analytical methods. FEA can accurately model all barrette geometries including rectangular, L-shaped, T-shaped, and wall-like configurations.

FEA is the recommended method for barrette analysis because:
- It handles complex geometries without approximations
- It captures three-dimensional behavior accurately
- It models progressive failure mechanisms
- It accounts for non-linear soil behavior
- It evaluates group effects reliably
- It provides detailed insights into stress distribution and failure mechanisms

## Modeling Complex Barrette Shapes

FEA allows accurate modeling of various barrette configurations without requiring shape factor approximations:

- **Rectangular barrettes**: Standard rectangular cross-section with corner effects
- **L-shaped barrettes**: Two rectangular sections at right angles with re-entrant corner effects
- **T-shaped barrettes**: Cross-sections with additional flanges and complex junction behavior
- **Wall-like barrettes**: Elongated sections with high aspect ratios

The FEA approach handles all these geometries without requiring simplified assumptions or extensive approximations.

## Soil Constitutive Model: Mohr-Coulomb

### Overview

The Mohr-Coulomb model is the recommended constitutive model for finite element analysis of barrettes. It is widely available in FEA software, relatively simple to calibrate, and provides reliable results for bearing capacity and settlement analysis.

### Model Parameters

The Mohr-Coulomb model requires the following parameters:

- **Cohesion** $c'$ (kN/m²): Effective cohesion of soil
- **Friction angle** $\phi'$ (degrees): Effective angle of internal friction
- **Dilation angle** $\psi$ (degrees): Typically 0° for clays, $\phi' - 30°$ to $\phi'$ for sands (often set to 0° for simplicity)
- **Young's modulus** $E_s$ (kN/m²): Elastic modulus of soil
- **Poisson's ratio** $\nu$: Typically 0.2-0.3 for soils

### Advantages

- Captures failure envelope accurately
- Widely available in all major FEA software
- Relatively simple to calibrate
- Well-established in geotechnical practice
- Appropriate for both cohesive and granular soils

### Limitations

- Linear elastic-perfectly plastic behavior
- May overestimate stiffness before failure
- Does not account for stress-dependent stiffness
- Does not model consolidation or time-dependent behavior

### Parameter Determination

**Cohesion and Friction Angle:**
- From laboratory tests (triaxial, direct shear)
- From field tests (CPT, SPT correlations)
- From literature values for similar soils

**Young's Modulus:**
- From correlations with SPT: $E_s = \alpha \times N_{SPT}$ (where $\alpha$ typically ranges from 500-2000 kN/m²)
- From CPT correlations
- From laboratory tests (triaxial, oedometer)

**Poisson's Ratio:**
- Typically 0.2-0.3 for most soils
- 0.4-0.5 for saturated clays under undrained conditions

### Alternative and Advanced Models

For specialized applications, alternative models may be considered:

- **Linear Elastic Model**: For preliminary analysis and model verification only
- **Modified Cam Clay Model**: For consolidation settlement analysis in clays (time-dependent behavior)
- **Hardening Soil Model**: For more realistic stress-strain behavior and stress-dependent stiffness
- **Hypoplastic Model**: For advanced analysis of granular soils with state-dependent behavior

These advanced models require additional parameters and expertise in calibration. Refer to software documentation and geotechnical literature for detailed guidance on these models.

## Model Setup

### Step 1: Geometry Definition

**1.1 Barrette Geometry**
- Create barrette geometry (rectangular, L, T, or wall shape)
- Define dimensions: length $L$, width $B$, embedment depth $D$
- For complex shapes, define all cross-sectional dimensions

**1.2 Soil Domain**
- Model soil domain extending:
  - At least 3 to 5 times barrette characteristic dimension laterally
  - At least 2 to 3 times longest barrette dimension in the strong direction
  - At least 2 to 3 times embedment depth ($D$) below base

### Step 2: Material Properties

**2.1 Barrette Properties**

- **Elastic modulus**: $E_c$ = 20-40 GPa (concrete)
- **Poisson's ratio**: $\nu_c$ = 0.15-0.2
- **Unit weight**: $\gamma_c$ = 24 kN/m³
- **Strength**: Typically elastic for structural elements, or model as elastic-perfectly plastic if structural failure is considered

**2.2 Soil Properties**

- **Constitutive model**: Use Mohr-Coulomb model
- Define parameters:
  - Cohesion $c'$, friction angle $\phi'$
  - Unit weight $\gamma$
  - Young's modulus $E_s$
  - Poisson's ratio $\nu$
- Estimate $E_s$ from correlations:
  - $E_s = \alpha \times N_{SPT}$ (from SPT, where $\alpha$ typically ranges from 500-2000 kN/m²)
  - From CPT correlations
  - From laboratory tests

## Mesh Generation and Boundary Conditions

### Domain Size

The analysis domain should extend:
- At least 3 to 5 times the barrette characteristic dimension laterally
- At least 2 to 3 times the longest barrette dimension in the strong direction
- At least 2 to 3 times the embedment depth ($D$) below the base

### Mesh Refinement

The mesh should be refined based on barrette geometry:

- **Barrette elements**: Fine mesh (element size = characteristic dimension/10 to characteristic dimension/20)
- **Corners and junctions**: Extra fine mesh for L, T, or complex shapes to capture stress concentrations
- **Near-field soil**: Medium mesh (element size = characteristic dimension/5 to characteristic dimension/10)
- **Far-field soil**: Coarse mesh (element size = characteristic dimension to 2×characteristic dimension)

#### Geometry-Specific Mesh Guidelines

**Rectangular Barrettes**
- Fine mesh at corners (stress concentration zones)
- Element size: $B/10$ to $B/20$ at barrette
- Medium mesh in near-field soil
- Account for aspect ratio effects

**L-Shaped Barrettes**
- Extra fine mesh at re-entrant corners (highest stress concentrations)
- Fine mesh at external corners
- Account for stress concentrations at junctions
- Ensure proper mesh connectivity at L-junction

**T-Shaped Barrettes**
- Extra fine mesh at T-junction (complex stress distribution)
- Fine mesh at all corners (external and internal)
- Appropriate mesh at flange-web junction
- Account for asymmetric load transfer

**Wall-Like Barrettes**
- Fine mesh along length (account for bending)
- Mesh refinement based on thickness
- Account for high aspect ratio effects
- Consider plane strain conditions where appropriate

### Element Types

- **Barrette**: Solid elements or beam elements with soil-structure interface
- **Soil**: Solid continuum elements (8-node hexahedral or 6-node wedge)
- **Interface**: Zero-thickness interface elements or contact surfaces
- **Special considerations**: For L and T shapes, ensure proper element connectivity at junctions

### Boundary Conditions

- **Lateral boundaries**: Roller supports (zero horizontal displacement: $u_x = 0$ or $u_y = 0$)
- **Bottom boundary**: Fixed (zero displacement in all directions: $u_x = u_y = u_z = 0$)
- **Top surface**: Free (no constraints) or with surcharge loading if applicable

### Initial Conditions

**Initial Stress State**

Establish geostatic equilibrium:

$$\sigma_v' = \gamma' z$$

$$\sigma_h' = K_0 \sigma_v'$$

Where $K_0 = 1 - \sin\phi'$ (Jaky's formula) or use site-specific value.

**Initial Step Procedure:**
1. Apply gravitational acceleration
2. Solve for equilibrium (linear elastic analysis)
3. Verify stress distribution is reasonable

**Additional Initial Conditions:**
- **Groundwater**: Pore pressure distribution if present
- **Initial void ratio**: For advanced models (Modified Cam Clay, Hypoplastic)

## Mathematical Formulation of Finite Element Method

### Notation Convention

**Important:** In the following mathematical formulations:

- **Global quantities** (for entire model): No superscript
  - $[K]$ = global stiffness matrix
  - $\{u\}$ = global displacement vector
  - $\{F\}$ = global force vector

- **Element-level quantities** (for individual elements): Superscript $^e$
  - $[k]^e$ = element stiffness matrix for element $e$
  - $\{u\}^e$ = element displacement vector for element $e$
  - $\{f\}^e$ = element force vector for element $e$
  - $\{\epsilon\}^e$ = element strain vector for element $e$
  - $\{\sigma\}^e$ = element stress vector for element $e$
  - $[B]^e$ = element strain-displacement matrix for element $e$

**Key Point:** Strains and stresses are computed at the **element level** from element nodal displacements. There is no single global strain or stress vector - each element has its own strain and stress values computed at Gauss points within that element.

### Fundamental Matrix Equation

The finite element method solves the equilibrium equations in matrix form:

$$[K]\{u\} = \{F\}$$

Where:
- $[K]$ = global stiffness matrix
- $\{u\}$ = displacement vector (nodal displacements)
- $\{F\}$ = force vector (nodal forces)

This equation represents the equilibrium condition where the internal forces (stiffness × displacements) equal the external applied forces.

#### Expanded Form

For a system with $n$ nodes, the expanded forms are:

**Global Stiffness Matrix** $[K]$ (size: $3n \times 3n$):

$$[K] = \begin{bmatrix}
K_{11} & K_{12} & K_{13} & \cdots & K_{1,3n} \\
K_{21} & K_{22} & K_{23} & \cdots & K_{2,3n} \\
K_{31} & K_{32} & K_{33} & \cdots & K_{3,3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
K_{3n,1} & K_{3n,2} & K_{3n,3} & \cdots & K_{3n,3n}
\end{bmatrix}$$

Where each $K_{ij}$ represents the stiffness contribution relating DOF $i$ to DOF $j$.

**Displacement Vector** $\{u\}$ (size: $3n \times 1$):

$$\{u\} = \begin{bmatrix}
u_{1x} \\
u_{1y} \\
u_{1z} \\
u_{2x} \\
u_{2y} \\
u_{2z} \\
\vdots \\
u_{nx} \\
u_{ny} \\
u_{nz}
\end{bmatrix}$$

Where $u_{ix}$, $u_{iy}$, $u_{iz}$ are the displacements of node $i$ in $x$, $y$, and $z$ directions.

**Force Vector** $\{F\}$ (size: $3n \times 1$):

$$\{F\} = \begin{bmatrix}
F_{1x} \\
F_{1y} \\
F_{1z} \\
F_{2x} \\
F_{2y} \\
F_{2z} \\
\vdots \\
F_{nx} \\
F_{ny} \\
F_{nz}
\end{bmatrix}$$

Where $F_{ix}$, $F_{iy}$, $F_{iz}$ are the forces applied to node $i$ in $x$, $y$, and $z$ directions.

### Element Stiffness Matrix

For each element, the element stiffness matrix $[k]^e$ relates element nodal displacements $\{u\}^e$ to element nodal forces $\{f\}^e$:

$$[k]^e\{u\}^e = \{f\}^e$$

For a 3D solid element (e.g., 8-node hexahedral), the element stiffness matrix is:

$$[k]^e = \int_{V^e} [B]^T [D] [B] \, dV$$

Where:
- $[B]$ = strain-displacement matrix
- $[D]$ = constitutive matrix (material property matrix)
- $V^e$ = volume of element $e$

#### Expanded Form

For an 8-node hexahedral element, the element stiffness matrix $[k]^e$ has size $24 \times 24$ (8 nodes × 3 DOF per node):

$$[k]^e = \begin{bmatrix}
k_{11} & k_{12} & k_{13} & \cdots & k_{1,24} \\
k_{21} & k_{22} & k_{23} & \cdots & k_{2,24} \\
k_{31} & k_{32} & k_{33} & \cdots & k_{3,24} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
k_{24,1} & k_{24,2} & k_{24,3} & \cdots & k_{24,24}
\end{bmatrix}$$

**Element Displacement Vector** $\{u\}^e$ (size: $24 \times 1$ for 8-node element):

$$\{u\}^e = \begin{bmatrix}
u_{1x} \\
u_{1y} \\
u_{1z} \\
u_{2x} \\
u_{2y} \\
u_{2z} \\
\vdots \\
u_{8x} \\
u_{8y} \\
u_{8z}
\end{bmatrix}$$

**Element Force Vector** $\{f\}^e$ (size: $24 \times 1$ for 8-node element):

$$\{f\}^e = \begin{bmatrix}
f_{1x} \\
f_{1y} \\
f_{1z} \\
f_{2x} \\
f_{2y} \\
f_{2z} \\
\vdots \\
f_{8x} \\
f_{8y} \\
f_{8z}
\end{bmatrix}$$

### Strain-Displacement Matrix

The strain-displacement matrix $[B]^e$ relates element strains $\{\epsilon\}^e$ to element nodal displacements:

$$\{\epsilon\}^e = [B]^e \{u\}^e$$

**Important:** Strains are computed **at the element level**. Each element has its own strain vector computed from its element nodal displacements.

For 3D analysis, element strains are:

$$\{\epsilon\}^e = \begin{bmatrix}
\epsilon_{xx} \\
\epsilon_{yy} \\
\epsilon_{zz} \\
\gamma_{xy} \\
\gamma_{yz} \\
\gamma_{zx}
\end{bmatrix}^e = \begin{bmatrix}
\frac{\partial u}{\partial x} \\
\frac{\partial v}{\partial y} \\
\frac{\partial w}{\partial z} \\
\frac{\partial u}{\partial y} + \frac{\partial v}{\partial x} \\
\frac{\partial v}{\partial z} + \frac{\partial w}{\partial y} \\
\frac{\partial w}{\partial x} + \frac{\partial u}{\partial z}
\end{bmatrix}$$

#### Expanded Form of [B]^e Matrix

For an 8-node hexahedral element, the strain-displacement matrix $[B]^e$ has size $6 \times 24$ (6 strains, 24 DOF):

$$[B]^e = \begin{bmatrix}
\frac{\partial N_1}{\partial x} & 0 & 0 & \frac{\partial N_2}{\partial x} & 0 & 0 & \cdots & \frac{\partial N_8}{\partial x} & 0 & 0 \\
0 & \frac{\partial N_1}{\partial y} & 0 & 0 & \frac{\partial N_2}{\partial y} & 0 & \cdots & 0 & \frac{\partial N_8}{\partial y} & 0 \\
0 & 0 & \frac{\partial N_1}{\partial z} & 0 & 0 & \frac{\partial N_2}{\partial z} & \cdots & 0 & 0 & \frac{\partial N_8}{\partial z} \\
\frac{\partial N_1}{\partial y} & \frac{\partial N_1}{\partial x} & 0 & \frac{\partial N_2}{\partial y} & \frac{\partial N_2}{\partial x} & 0 & \cdots & \frac{\partial N_8}{\partial y} & \frac{\partial N_8}{\partial x} & 0 \\
0 & \frac{\partial N_1}{\partial z} & \frac{\partial N_1}{\partial y} & 0 & \frac{\partial N_2}{\partial z} & \frac{\partial N_2}{\partial y} & \cdots & 0 & \frac{\partial N_8}{\partial z} & \frac{\partial N_8}{\partial y} \\
\frac{\partial N_1}{\partial z} & 0 & \frac{\partial N_1}{\partial x} & \frac{\partial N_2}{\partial z} & 0 & \frac{\partial N_2}{\partial x} & \cdots & \frac{\partial N_8}{\partial z} & 0 & \frac{\partial N_8}{\partial x}
\end{bmatrix}$$

**Note:** The $[B]^e$ matrix is computed automatically by FEA software based on element geometry and interpolation functions. The matrix elements contain derivatives that relate nodal displacements to strains. $[B]^e$ is specific to each element and varies with element geometry.

### Constitutive Matrix for Mohr-Coulomb (Elastic Part)

For linear elastic behavior, the constitutive matrix $[D]$ relates element stresses to element strains:

$$\{\sigma\}^e = [D] \{\epsilon\}^e$$

**Note:** $[D]$ is the material property matrix and is the same for all elements with the same material properties. However, stresses $\{\sigma\}^e$ are computed at the element level.

For isotropic elastic material, $[D]$ is:

$$[D] = \frac{E}{(1+\nu)(1-2\nu)} \begin{bmatrix}
1-\nu & \nu & \nu & 0 & 0 & 0 \\
\nu & 1-\nu & \nu & 0 & 0 & 0 \\
\nu & \nu & 1-\nu & 0 & 0 & 0 \\
0 & 0 & 0 & \frac{1-2\nu}{2} & 0 & 0 \\
0 & 0 & 0 & 0 & \frac{1-2\nu}{2} & 0 \\
0 & 0 & 0 & 0 & 0 & \frac{1-2\nu}{2}
\end{bmatrix}$$

Where:
- $E$ = Young's modulus
- $\nu$ = Poisson's ratio

### Note on Shape Functions

The strain-displacement matrix $[B]^e$ is computed automatically by FEA software using interpolation functions (called "shape functions"). These functions allow the software to:

- Interpolate displacements at any point within an element from nodal displacement values
- Compute strain derivatives needed for the $[B]^e$ matrix
- Transform between local element coordinates and global coordinates

**For practical use:** You don't need to know the mathematical form of shape functions. The FEA software handles all shape function calculations automatically when you select an element type (e.g., 8-node hexahedral). The software computes $[B]^e$ based on your element geometry and the selected element type.

### Numerical Integration

The element stiffness matrix is computed using numerical integration (Gauss quadrature):

$$[k]^e = \int_{V^e} ([B]^e)^T [D] [B]^e \, dV = \sum_{p=1}^{n_{GP}} w_p ([B]^e_p)^T [D] [B]^e_p |J_p|$$

Where:
- $n_{GP}$ = number of Gauss points (typically 2×2×2 = 8 for 8-node elements)
- $w_p$ = weight at Gauss point $p$
- $[B]^e_p$ = strain-displacement matrix for element $e$ evaluated at Gauss point $p$
- $|J_p|$ = determinant of Jacobian matrix at Gauss point $p$

The Jacobian matrix $[J]$ relates local to global coordinates:

$$[J] = \begin{bmatrix}
\frac{\partial x}{\partial \xi} & \frac{\partial y}{\partial \xi} & \frac{\partial z}{\partial \xi} \\
\frac{\partial x}{\partial \eta} & \frac{\partial y}{\partial \eta} & \frac{\partial z}{\partial \eta} \\
\frac{\partial x}{\partial \zeta} & \frac{\partial y}{\partial \zeta} & \frac{\partial z}{\partial \zeta}
\end{bmatrix}$$

**Expanded Form:** The Jacobian matrix (size: $3 \times 3$) contains the partial derivatives that transform from local coordinates $(\xi, \eta, \zeta)$ to global coordinates $(x, y, z)$. Each element $J_{ij}$ represents how the $j$-th global coordinate changes with respect to the $i$-th local coordinate.

### Example Calculation of Element Stiffness Matrix

This example shows how $[k]^e$ is computed step-by-step using Gauss quadrature.

#### Step 1: Setup

For an 8-node hexahedral element, we use 2×2×2 = 8 Gauss points. For 2-point Gauss quadrature in 1D, the Gauss points and weights are:

- Local coordinate: $\xi_1 = -\frac{1}{\sqrt{3}} \approx -0.577$, $\xi_2 = +\frac{1}{\sqrt{3}} \approx +0.577$
- Weight: $w = 1.0$ (for both points)

The 8 Gauss points in 3D are at all combinations:
- $(\xi_i, \eta_j, \zeta_k)$ where $i, j, k \in \{1, 2\}$
- Each with weight $w_p = 1.0 \times 1.0 \times 1.0 = 1.0$

#### Step 2: At Each Gauss Point $p$

For each of the 8 Gauss points, compute:

1. **$[B]^e_p$**: Evaluate the strain-displacement matrix at Gauss point $p$
   - Size: $6 \times 24$ (6 strains, 24 DOF)

2. **$|J_p|$**: Compute Jacobian determinant at Gauss point $p$
   - Scalar value (measures element volume at this point)

3. **$([B]^e_p)^T [D] [B]^e_p$**: Matrix multiplication
   - $([B]^e_p)^T$: $24 \times 6$
   - $[D]$: $6 \times 6$
   - $[B]^e_p$: $6 \times 24$
   - Result: $24 \times 24$ matrix

4. **$w_p \times \text{result} \times |J_p|$**: Scale by weight and Jacobian
   - Result: $24 \times 24$ matrix contribution from Gauss point $p$

#### Step 3: Sum All Contributions

$$[k]^e = \sum_{p=1}^{8} w_p ([B]^e_p)^T [D] [B]^e_p |J_p|$$

This means adding the 8 matrices (each $24 \times 24$) together element-by-element.

#### Numerical Example

**Assumptions for simplified example:**
- Regular cubic element with side length $a = 2$ m
- Material: $E = 10,000$ kN/m², $\nu = 0.3$
- For a regular element: $|J_p| = \frac{a^3}{8} = 1.0$ m³ (approximately constant for regular shape)

**At Gauss point 1** ($\xi = -0.577, \eta = -0.577, \zeta = -0.577$):

1. Software computes $[B]^e_1$ (depends on element geometry - simplified representation):
   $$[B]^e_1 = \begin{bmatrix}
   b_{11} & 0 & 0 & b_{12} & 0 & 0 & \cdots & b_{1,24} \\
   0 & b_{21} & 0 & 0 & b_{22} & 0 & \cdots & b_{2,24} \\
   \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots
   \end{bmatrix}_{6 \times 24}$$

2. With $E = 10,000$ kN/m² and $\nu = 0.3$:
   $$[D] = \frac{10000}{(1.3)(0.4)} \begin{bmatrix}
   0.7 & 0.3 & 0.3 & 0 & 0 & 0 \\
   0.3 & 0.7 & 0.3 & 0 & 0 & 0 \\
   0.3 & 0.3 & 0.7 & 0 & 0 & 0 \\
   0 & 0 & 0 & 0.2 & 0 & 0 \\
   0 & 0 & 0 & 0 & 0.2 & 0 \\
   0 & 0 & 0 & 0 & 0 & 0.2
   \end{bmatrix}$$

3. Compute contribution from Gauss point 1:
   $$[k]^e_{GP1} = w_1 \times ([B]^e_1)^T [D] [B]^e_1 \times |J_1|$$
   $$[k]^e_{GP1} = 1.0 \times ([B]^e_1)^T [D] [B]^e_1 \times 1.0 = ([B]^e_1)^T [D] [B]^e_1$$

   This gives a $24 \times 24$ matrix with numerical values.

4. **Repeat for all 8 Gauss points**, each producing a $24 \times 24$ matrix contribution.

5. **Sum all contributions**:
   $$[k]^e = [k]^e_{GP1} + [k]^e_{GP2} + [k]^e_{GP3} + [k]^e_{GP4} + [k]^e_{GP5} + [k]^e_{GP6} + [k]^e_{GP7} + [k]^e_{GP8}$$

#### Final Shape of $[k]^e$

The final element stiffness matrix $[k]^e$ is a **$24 \times 24$ symmetric matrix**:

$$[k]^e = \begin{bmatrix}
k_{11} & k_{12} & k_{13} & k_{14} & \cdots & k_{1,24} \\
k_{21} & k_{22} & k_{23} & k_{24} & \cdots & k_{2,24} \\
k_{31} & k_{32} & k_{33} & k_{34} & \cdots & k_{3,24} \\
k_{41} & k_{42} & k_{43} & k_{44} & \cdots & k_{4,24} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
k_{24,1} & k_{24,2} & k_{24,3} & k_{24,4} & \cdots & k_{24,24}
\end{bmatrix}$$

**Properties:**
- **Symmetric**: $k_{ij} = k_{ji}$ (due to energy considerations)
- **Size**: $24 \times 24$ = 576 individual terms
- **Structure**: Coupling between all 8 nodes (each node has 3 DOF: $u_x$, $u_y$, $u_z$)
- **Physical meaning**: $k_{ij}$ = force at DOF $i$ due to unit displacement at DOF $j$

**Typical Structure Pattern:**

The matrix has a block structure where each $3 \times 3$ block represents coupling between two nodes:

$$[k]^e = \begin{bmatrix}
[k]_{11} & [k]_{12} & [k]_{13} & \cdots & [k]_{18} \\
[k]_{21} & [k]_{22} & [k]_{23} & \cdots & [k]_{28} \\
[k]_{31} & [k]_{32} & [k]_{33} & \cdots & [k]_{38} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
[k]_{81} & [k]_{82} & [k]_{83} & \cdots & [k]_{88}
\end{bmatrix}$$

Where each $[k]_{ij}$ is a $3 \times 3$ submatrix representing the stiffness coupling between node $i$ and node $j$:

$$[k]_{ij} = \begin{bmatrix}
k_{ix,jx} & k_{ix,jy} & k_{ix,jz} \\
k_{iy,jx} & k_{iy,jy} & k_{iy,jz} \\
k_{iz,jx} & k_{iz,jy} & k_{iz,jz}
\end{bmatrix}$$

**Important Notes:**
- All numerical values ($k_{ij}$) are computed by the software automatically
- The exact values depend on: element geometry (nodal coordinates), material properties ($E$, $\nu$), and integration scheme
- For regular (cubic) elements, the matrix will have certain symmetries
- For irregular/distorted elements, all terms are generally non-zero and geometry-dependent

## Step-by-Step Matrix Assembly Procedure

### Step 1: Element Numbering and Node Connectivity

1. **Number all elements**: Assign unique element numbers (1, 2, 3, ..., $n_{elem}$)
2. **Number all nodes**: Assign unique global node numbers (1, 2, 3, ..., $n_{node}$)
3. **Create connectivity table**: For each element, list the global node numbers of its nodes

**Example connectivity for element $e$:**

| Element | Node 1 | Node 2 | Node 3 | Node 4 | Node 5 | Node 6 | Node 7 | Node 8 |
|---------|--------|--------|--------|--------|--------|--------|--------|--------|
| $e$     | 15     | 23     | 24     | 16     | 35     | 43     | 44     | 36     |

### Step 2: Initialize Global Matrices

1. **Initialize global stiffness matrix**: $[K] = [0]$ (size: $n_{DOF} \times n_{DOF}$)
   - $n_{DOF} = 3 \times n_{node}$ (3 DOF per node: $u_x$, $u_y$, $u_z$)
2. **Initialize global force vector**: $\{F\} = \{0\}$ (size: $n_{DOF} \times 1$)
3. **Initialize global displacement vector**: $\{u\} = \{0\}$ (size: $n_{DOF} \times 1$)

**Example:** For a system with 100 nodes:
- $n_{DOF} = 3 \times 100 = 300$
- $[K]$ is $300 \times 300$ matrix (initially all zeros)
- $\{F\}$ and $\{u\}$ are $300 \times 1$ vectors (initially all zeros)

### Step 3: Compute Element Stiffness Matrices

For each element $e = 1$ to $n_{elem}$:

1. **Get element nodes**: From connectivity table, identify global node numbers
2. **Get nodal coordinates**: Extract coordinates for element nodes
3. **Compute element stiffness matrix**:

   $$[k]^e = \int_{V^e} ([B]^e)^T [D] [B]^e \, dV$$

   Using Gauss quadrature:
   
   $$[k]^e = \sum_{p=1}^{n_{GP}} w_p ([B]^e_p)^T [D] [B]^e_p |J_p|$$

4. **Store element matrix**: $[k]^e$ has size $n_e \times n_e$ where $n_e$ = number of DOF in element (24 for 8-node element: 8 nodes × 3 DOF)

### Step 4: Assembly of Global Stiffness Matrix

For each element $e$:

1. **Get element DOF mapping**: Map element DOF to global DOF

   For node $i$ in element $e$:
   - Global DOF indices: $3(i-1)+1$, $3(i-1)+2$, $3(i-1)+3$ (for $u_x$, $u_y$, $u_z$)

2. **Add element contributions to global matrix**:

   $$[K][I, J] = [K][I, J] + [k]^e[i, j]$$

   Where:
   - $I, J$ = global DOF indices
   - $i, j$ = element DOF indices
   - Mapping: $I = f(\text{global node}, \text{DOF})$, $i = f(\text{element node}, \text{DOF})$

**Assembly equation:**

$$[K] = \sum_{e=1}^{n_{elem}} [C]^e [k]^e ([C]^e)^T$$

Where $[C]^e$ is the connectivity/assembly matrix for element $e$.

**Example of Assembly Process:**

Consider two 8-node elements sharing a common face. Element 1 has nodes [1, 2, 3, 4, 5, 6, 7, 8] and Element 2 has nodes [5, 6, 7, 8, 9, 10, 11, 12] (sharing nodes 5-8).

The element stiffness matrix $[k]^1$ (24×24) contributes to global $[K]$ at positions corresponding to global nodes 1-8. The element stiffness matrix $[k]^2$ (24×24) contributes to global $[K]$ at positions corresponding to global nodes 5-12. 

The overlapping region (nodes 5-8) shows how element contributions are **added together** in the global matrix:

$$[K]_{global} = \begin{bmatrix}
[k]^1_{1-4,1-4} & [k]^1_{1-4,5-8} & 0 \\
[k]^1_{5-8,1-4} & [k]^1_{5-8,5-8} + [k]^2_{5-8,5-8} & [k]^2_{5-8,9-12} \\
0 & [k]^2_{9-12,5-8} & [k]^2_{9-12,9-12}
\end{bmatrix}$$

Note: Submatrices shown are blocks, not individual elements. The actual assembly adds corresponding components element-by-element.

**Pseudo-code for assembly:**

```
For each element e:
    For each node i in element e:
        global_node_i = connectivity[e][i]
        For each DOF dof_i (1, 2, 3):
            global_DOF_i = 3*(global_node_i - 1) + dof_i
            element_DOF_i = 3*(i - 1) + dof_i
            
            For each node j in element e:
                global_node_j = connectivity[e][j]
                For each DOF dof_j (1, 2, 3):
                    global_DOF_j = 3*(global_node_j - 1) + dof_j
                    element_DOF_j = 3*(j - 1) + dof_j
                    
                    K[global_DOF_i, global_DOF_j] += k^e[element_DOF_i, element_DOF_j]
```

### Step 5: Apply Boundary Conditions

1. **Fixed boundary conditions**: For nodes with fixed displacement ($u = 0$):
   - Modify stiffness matrix: Set row and column to identity, set diagonal = 1, off-diagonals = 0
   - Set corresponding force to zero

   $$[K][i, :] = [0], \quad [K][:, i] = [0], \quad [K][i, i] = 1, \quad \{F\}[i] = 0$$

2. **Prescribed displacements**: For nodes with known displacement ($u = u_0$):
   - Apply same procedure, but set $\{F\}[i] = u_0$ (or handle via constraint elimination)

### Step 6: Apply Loads

Add nodal forces to force vector $\{F\}$:

- **Point loads**: $\{F\}[i] = F_i$ (where $i$ is the DOF index)
- **Distributed loads**: Convert to equivalent nodal forces automatically by the software:

$$\{f\}^e = \int_{S^e} [N]^e \{t\} \, dS$$

Where:
- $[N]^e$ = interpolation matrix (automatically computed by software from element shape functions)
- $\{t\}$ = traction vector (applied at element surface)
- $S^e$ = surface of element $e$

**Note:** The software automatically converts distributed loads to equivalent nodal forces. You only need to specify the distributed load magnitude and location.

### Step 7: Solve System of Equations

Solve the linear system:

$$[K]\{u\} = \{F\}$$

Using methods such as:
- **Direct methods**: Gaussian elimination, Cholesky decomposition (for symmetric positive definite matrices)
- **Iterative methods**: Conjugate gradient, preconditioned conjugate gradient

### Step 8: Extract Results

1. **Displacements**: From solution vector $\{u\}$

2. **Strains**: Compute at element level for each element $e$:

   $$\{\epsilon\}^e = [B]^e \{u\}^e$$

   Expanded element strain vector:
   $$\{\epsilon\}^e = \begin{bmatrix}
   \epsilon_{xx} \\
   \epsilon_{yy} \\
   \epsilon_{zz} \\
   \gamma_{xy} \\
   \gamma_{yz} \\
   \gamma_{zx}
   \end{bmatrix}^e = \begin{bmatrix}
   \text{normal strain in } x \\
   \text{normal strain in } y \\
   \text{normal strain in } z \\
   \text{shear strain in } xy \\
   \text{shear strain in } yz \\
   \text{shear strain in } zx
   \end{bmatrix}$$

   **Note:** Strains are computed at Gauss points within each element. Each element has its own strain vector.

3. **Stresses**: Compute at element level for each element $e$:

   $$\{\sigma\}^e = [D] \{\epsilon\}^e$$

   Expanded element stress vector:
   $$\{\sigma\}^e = \begin{bmatrix}
   \sigma_{xx} \\
   \sigma_{yy} \\
   \sigma_{zz} \\
   \tau_{xy} \\
   \tau_{yz} \\
   \tau_{zx}
   \end{bmatrix}^e = \begin{bmatrix}
   \text{normal stress in } x \\
   \text{normal stress in } y \\
   \text{normal stress in } z \\
   \text{shear stress in } xy \\
   \text{shear stress in } yz \\
   \text{shear stress in } zx
   \end{bmatrix}$$

   **Note:** Stresses are computed at Gauss points within each element. Each element has its own stress vector.

### Non-Linear Analysis (Mohr-Coulomb Plasticity)

For non-linear analysis with Mohr-Coulomb plasticity:

1. **Initial elastic solution**: Solve $[K]_{elastic}\{u\} = \{F\}$

2. **Check yielding**: For each Gauss point, check if stress state exceeds Mohr-Coulomb criterion:

$$\tau = c' + \sigma_n' \tan\phi'$$

3. **Plastic correction**: If yielded, compute plastic strains and update stresses

4. **Update stiffness**: Modify stiffness matrix based on plastic state

5. **Newton-Raphson iteration**: Iterate until convergence:

$$[K_t]^{(i)} \{\Delta u\}^{(i)} = \{F\} - \{R\}^{(i)}$$

$$\{u\}^{(i+1)} = \{u\}^{(i)} + \{\Delta u\}^{(i)}$$

Where:
- $[K_t]^{(i)}$ = tangent stiffness matrix at iteration $i$ (updated based on current plastic state)
- $\{R\}^{(i)}$ = residual force vector (unbalanced forces)
- $\{\Delta u\}^{(i)}$ = displacement increment

#### Expanded Form for Non-Linear Analysis

**Tangent Stiffness Matrix** $[K_t]^{(i)}$ (size: $3n \times 3n$):
$$[K_t]^{(i)} = \begin{bmatrix}
K_{t,11} & K_{t,12} & \cdots & K_{t,1,3n} \\
K_{t,21} & K_{t,22} & \cdots & K_{t,2,3n} \\
\vdots & \vdots & \ddots & \vdots \\
K_{t,3n,1} & K_{t,3n,2} & \cdots & K_{t,3n,3n}
\end{bmatrix}$$

**Residual Force Vector** $\{R\}^{(i)}$ (size: $3n \times 1$):
$$\{R\}^{(i)} = \{F\} - \{F_{int}\}^{(i)} = \begin{bmatrix}
F_{1x} - F_{int,1x} \\
F_{1y} - F_{int,1y} \\
F_{1z} - F_{int,1z} \\
\vdots \\
F_{nx} - F_{int,nx} \\
F_{ny} - F_{int,ny} \\
F_{nz} - F_{int,nz}
\end{bmatrix}$$

Where $\{F_{int}\}^{(i)}$ are the internal forces computed from current stress state.

**Displacement Increment Vector** $\{\Delta u\}^{(i)}$ (size: $3n \times 1$):
$$\{\Delta u\}^{(i)} = \begin{bmatrix}
\Delta u_{1x} \\
\Delta u_{1y} \\
\Delta u_{1z} \\
\vdots \\
\Delta u_{nx} \\
\Delta u_{ny} \\
\Delta u_{nz}
\end{bmatrix}$$

Convergence when: $\|\{R\}^{(i)}\| < \epsilon$ (residual force magnitude is small)

## Summary of Matrix Assembly Process

The complete process can be summarized as:

1. **Discretize domain**: Divide into finite elements
2. **Select element type**: Choose element type (e.g., 8-node hexahedral) - software automatically handles interpolation functions
3. **Compute element matrices**: For each element $e$, software computes $[k]^e$ using $[B]^e$ and $[D]$
4. **Assemble global matrix**: Sum element contributions → $[K] = \sum_{e} [k]^e$ (via assembly)
5. **Apply boundary conditions**: Modify $[K]$ and $\{F\}$
6. **Apply loads**: Add to $\{F\}$
7. **Solve**: $\{u\} = [K]^{-1}\{F\}$ → get global displacements
8. **Post-process**: 
   - Extract element displacements $\{u\}^e$ from global $\{u\}$
   - Compute element strains: $\{\epsilon\}^e = [B]^e \{u\}^e$
   - Compute element stresses: $\{\sigma\}^e = [D] \{\epsilon\}^e$

For non-linear analysis, steps 3-7 are repeated iteratively with updated material properties based on current stress state. At each iteration, element strains and stresses are computed using the $^e$ notation to maintain clarity that these are element-level quantities.

## Analysis Procedures

### Construction Sequence

**Sequence of Steps:**

1. **Step 1 - Geostatic**: Establish initial soil stresses (equilibrium under self-weight)
2. **Step 2 - Excavation**: "Kill" or remove soil elements where barrette will be placed
3. **Step 3 - Installation**: "Activate" barrette elements (with self-weight)
4. **Step 4 - Contact**: Establish contact between barrette and surrounding soil
5. **Step 5 - Equilibrium**: Allow system to reach equilibrium after installation

### Load Application Method

#### Load-Controlled Method (Load Increment)

Apply vertical load at barrette head incrementally:

- Increment 1: $Q_1 = 0.1 \times Q_{estimated}$
- Increment 2: $Q_2 = 0.2 \times Q_{estimated}$
- Increment 3: $Q_3 = 0.3 \times Q_{estimated}$
- Continue increasing load in increments

**Load increment size:**
- Use consistent increments (e.g., 10-20% of estimated capacity per increment)
- May reduce increment size near expected failure for better resolution

**Procedure:**
1. Apply load increment
2. Solve for equilibrium
3. Extract settlement at barrette head
4. Check if failure criterion is reached
5. If not, proceed to next increment
6. Continue until failure criterion is met

#### Service Load Application (For Settlement)

Apply service loads incrementally:
- Apply design loads gradually
- Monitor settlement at each increment
- Record settlement at working load

### Non-Linear Analysis

For each load/displacement increment:

1. **Apply increment**: Apply load or displacement
2. **Newton-Raphson iteration**: Solve equilibrium equations iteratively
3. **Check convergence**:
   - Force residual < 0.5% to 1% of applied load
   - Displacement change < tolerance
   - Energy change < tolerance
4. **If converged**: Proceed to next increment
5. **If not converged**: Reduce increment size and retry

**Advanced Methods:**
- **Arc-length method**: For snap-through or snap-back behavior
- **Modified Newton-Raphson**: For improved convergence
- **Line search**: To improve convergence rate

### Convergence Criteria

- **Force equilibrium**: Residual forces < tolerance (typically 0.5% to 1% of applied load)
- **Displacement**: Change in displacement < tolerance (typically 0.1% of maximum displacement)
- **Energy**: Change in energy < tolerance (typically 0.1% of total energy)

## Interpretation of FEA Results

### For Bearing Capacity Analysis

#### Load-Displacement Curve

Plot vertical displacement ($\delta$) versus applied load or reaction force ($Q$):

| Load Q (kN) | Displacement δ (mm) |
|-------------|---------------------|
| 1000        | 2.5                 |
| 2000        | 5.1                 |
| 3000        | 8.2                 |
| 4000        | 12.5                |
| 5000        | 18.3                |
| 6000        | 28.7 ← Failure     |

#### Determining Ultimate Bearing Capacity

**Settlement Criterion Method**

The ultimate bearing capacity is defined as the load at which a specified settlement is reached:

**For normal structures:**
$$Q_u = Q(\delta = 25 \text{ mm}) = Q(\delta = 1 \text{ inch})$$

**For rafts:**
$$Q_u = Q(\delta = 50 \text{ mm}) = Q(\delta = 2 \text{ inches})$$

**Procedure:**
1. Extract settlement at each load increment
2. Plot load-displacement curve
3. Identify load corresponding to the specified settlement (25 mm or 50 mm)
4. This load is the ultimate bearing capacity $Q_u$

**Alternative: Non-Convergence Method**

If solution fails to converge at a load increment before reaching the specified settlement, the ultimate capacity can be taken as the last successfully converged load increment.

#### Plastic Zone Development

Monitor plastic points (yielded elements) at each increment:
- Identify when extensive plastic zones form
- Check if plastic zone connects barrette base to surface or extends laterally
- Visualize failure mechanism

#### Stress Distribution

Extract at each increment:
- Base normal stress: $\sigma_{base}$
- Shaft shear stress: $\tau_{shaft}$ along perimeter
- Contact pressures around barrette
- Soil stress contours

### For Settlement Analysis

#### Settlement Components

- **Immediate settlement**: Elastic deformation occurring during or immediately after load application
- **Consolidation settlement**: Time-dependent settlement in cohesive soils due to pore pressure dissipation
- **Total settlement**: Sum of all settlement components

#### Settlement Distribution

- **Uniform settlement**: Under uniform loading on symmetric geometries
- **Differential settlement**: Under eccentric or non-uniform loading
- **Tilt**: Rotation of barrette due to non-uniform settlement
- **Shape effects**: For L and T shapes, differential settlement may occur across cross-section

#### Settlement-Time Curves

For consolidation analysis, develop settlement-time relationships:
- **Initial rapid settlement**: Immediate elastic and initial consolidation
- **Primary consolidation phase**: Exponential decay of excess pore pressure
- **Secondary compression phase**: Long-term creep

#### Settlement Analysis Points

For complex shapes, monitor settlement at:
- Center of barrette
- Corners (for rectangular shapes)
- Junction points (for L and T shapes)
- Various points along length (for wall-like shapes)

### Load Distribution

- **Base resistance**: Extract normal stresses at barrette base
- **Shaft resistance**: Extract shear stresses along barrette shaft (important for complex shapes with varying perimeter)
- **Load transfer**: Analyze load distribution with depth
- **Shape effects**: For L and T shapes, identify load distribution at junctions

### Displacements

- **Settlement**: Vertical displacement at barrette head
- **Lateral displacement**: Horizontal movement under lateral loads
- **Rotation**: Angular rotation at barrette head
- **Differential displacement**: For complex shapes, check for differential settlement across cross-section

## Validation and Verification

### Mesh Sensitivity Check

- Refine mesh and repeat analysis
- Compare results with coarser mesh
- Ensure mesh-independent results
- Typical approach: Start with coarse mesh, refine progressively

### Boundary Effects Check

- Increase domain size and compare results
- Verify boundaries don't affect results
- Typical check: Double domain size and compare

### Comparison with Analytical Methods

- Compare $Q_u$ with simplified analytical estimates (for validation)
- Check order of magnitude consistency
- Use as sanity check, not primary design method

### Field Validation

- Compare with load test data if available
- Adjust model if significant discrepancies exist
- Calibrate soil parameters based on field data

### Parameter Sensitivity Analysis

- Vary key soil parameters (e.g., $c'$, $\phi'$, $E_s$)
- Assess sensitivity of results
- Identify critical parameters requiring accurate determination

## Best Practices for FEA

1. **Start simple**: Begin with linear elastic model to verify geometry and boundary conditions
2. **Incremental complexity**: Add non-linearity gradually
3. **Parameter sensitivity**: Conduct sensitivity analysis for soil parameters
4. **Model validation**: Compare with field data or simplified analytical solutions where possible
5. **Mesh refinement**: Check mesh sensitivity, especially at corners and junctions
6. **Boundary effects**: Verify domain size is adequate (larger may be needed for wall-like barrettes)
7. **Convergence**: Ensure proper convergence at each load increment
8. **Documentation**: Document all assumptions, parameters, and model geometry
9. **Quality control**: Review results for physical reasonableness
10. **Expert review**: Have experienced FEA practitioners review critical models

## Advantages of FEA for Barrettes

- Captures complex geometry (rectangular, L, T, walls) without approximations
- Accounts for non-linear soil behavior
- Includes three-dimensional effects
- Models construction sequence
- Handles complex loading conditions
- Evaluates group effects accurately
- Captures stress concentrations at corners and junctions
- Models progressive failure mechanisms
- Provides detailed insights into soil-structure interaction
- Can model time-dependent behavior (consolidation)

## Limitations of FEA

- Requires significant computational resources
- Model calibration needed for soil parameters
- Results sensitive to input parameters
- Requires expertise in numerical modeling
- May not capture all physical phenomena
- Mesh quality significantly affects results
- Can be time-consuming for complex models
- Requires validation and verification

## Typical FEA Software

Common FEA software packages used for barrette analysis:

- **PLAXIS**: Geotechnical-specific FEA software
- **ABAQUS**: General-purpose FEA with geotechnical capabilities
- **FLAC/FLAC3D**: Finite difference method (alternative to FEA)
- **DIANA**: Multi-purpose FEA with geotechnical features
- **MIDAS GTS**: Geotechnical analysis software
- **ANSYS**: General-purpose FEA

## References

- Poulos, H. G., & Davis, E. H. (1980). *Pile Foundation Analysis and Design*. John Wiley & Sons.
- FHWA (2010). *Geotechnical Engineering Circular No. 10: Drilled Shafts: Construction Procedures and LRFD Design Methods*.
- Potts, D. M., & Zdravkovic, L. (2001). *Finite Element Analysis in Geotechnical Engineering: Theory*. Thomas Telford.
- Brinkgreve, R. B. J., et al. (2020). *PLAXIS 2D - Reference Manual*. Bentley Systems.

