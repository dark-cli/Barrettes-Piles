# Finite Element Analysis for Barrettes

## Overview

Finite element analysis (FEA) provides a numerical method for analyzing barrettes by discretizing the continuous domain into finite elements. This approach allows modeling of complex geometries, soil-structure interaction, and non-linear material behavior.

## Main Natural Phenomena

The finite element method models three fundamental physical phenomena:

1. **Equilibrium**: Forces must balance at every point in the domain
2. **Compatibility**: Displacements must be continuous across the domain
3. **Constitutive Relations**: Stresses relate to strains through material properties

These phenomena are interconnected: applied loads create stresses, stresses cause strains through constitutive relationships, and strains produce displacements that must satisfy equilibrium and compatibility.

## Governing Differential Equations

### Strong Form: Equilibrium Equations

The fundamental governing equation is the equilibrium condition, expressed as a differential equation:

$$\frac{\partial \sigma_{ij}}{\partial x_j} + b_i = 0$$

Where:
- $\sigma_{ij}$ = stress tensor
- $b_i$ = body force vector (e.g., gravity)
- $x_j$ = spatial coordinates

In expanded form for 3D:

$$\frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \tau_{xy}}{\partial y} + \frac{\partial \tau_{xz}}{\partial z} + b_x = 0$$

$$\frac{\partial \tau_{yx}}{\partial x} + \frac{\partial \sigma_{yy}}{\partial y} + \frac{\partial \tau_{yz}}{\partial z} + b_y = 0$$

$$\frac{\partial \tau_{zx}}{\partial x} + \frac{\partial \tau_{zy}}{\partial y} + \frac{\partial \sigma_{zz}}{\partial z} + b_z = 0$$

### Weak Form: Principle of Virtual Work

The finite element method solves the weak form of equilibrium, which states that the internal virtual work equals the external virtual work:

$$\int_V \delta \epsilon^T \sigma \, dV = \int_V \delta u^T b \, dV + \int_S \delta u^T t \, dS$$

Where:
- $\delta u$ = virtual displacement
- $\delta \epsilon$ = virtual strain
- $\sigma$ = stress vector
- $b$ = body force vector
- $t$ = surface traction vector
- $V$ = volume domain
- $S$ = surface domain

## Strain-Displacement Relationship

Strains are related to displacements through the kinematic equations:

$$\epsilon_{ij} = \frac{1}{2}\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right)$$

In vector form for 3D:

$$\{\epsilon\} = \begin{bmatrix}
\epsilon_{xx} \\
\epsilon_{yy} \\
\epsilon_{zz} \\
\gamma_{xy} \\
\gamma_{yz} \\
\gamma_{zx}
\end{bmatrix} = \begin{bmatrix}
\frac{\partial u}{\partial x} \\
\frac{\partial v}{\partial y} \\
\frac{\partial w}{\partial z} \\
\frac{\partial u}{\partial y} + \frac{\partial v}{\partial x} \\
\frac{\partial v}{\partial z} + \frac{\partial w}{\partial y} \\
\frac{\partial w}{\partial x} + \frac{\partial u}{\partial z}
\end{bmatrix}$$

## Constitutive Relationships

### General Elastic Constitutive Matrix

For isotropic elastic materials (both pile and soil), the stress-strain relationship is:

$$\{\sigma\} = [D] \{\epsilon\}$$

The general constitutive matrix $[D]$ for isotropic elastic material:

$$[D] = \frac{E}{(1+\nu)(1-2\nu)} \begin{bmatrix}
1-\nu & \nu & \nu & 0 & 0 & 0 \\
\nu & 1-\nu & \nu & 0 & 0 & 0 \\
\nu & \nu & 1-\nu & 0 & 0 & 0 \\
0 & 0 & 0 & \frac{1-2\nu}{2} & 0 & 0 \\
0 & 0 & 0 & 0 & \frac{1-2\nu}{2} & 0 \\
0 & 0 & 0 & 0 & 0 & \frac{1-2\nu}{2}
\end{bmatrix}$$

### Pile Material

For the concrete barrette (linear elastic):

$$[D_c] = [D] \text{ with } E = E_c, \nu = \nu_c$$

Where:
- $E_c$ = Young's modulus of concrete (typically 20-40 GPa)
- $\nu_c$ = Poisson's ratio of concrete (typically 0.15-0.2)

### Soil Material

For soil, the elastic part uses:

$$[D_s] = [D] \text{ with } E = E_s, \nu = \nu_s$$

Where:
- $E_s$ = Young's modulus of soil
- $\nu_s$ = Poisson's ratio of soil (typically 0.2-0.3)

**Important:** The Mohr-Coulomb parameters $c'$ and $\phi'$ are **not** in the elastic $[D_s]$ matrix. The elastic matrix $[D_s]$ only contains $E_s$ and $\nu_s$ and governs elastic behavior.

### Mohr-Coulomb Plasticity for Soil

For non-linear soil behavior, the Mohr-Coulomb failure criterion applies:

$$\tau = c' + \sigma_n' \tan\phi'$$

Where:
- $c'$ = effective cohesion
- $\phi'$ = effective friction angle
- $\tau$ = shear stress
- $\sigma_n'$ = effective normal stress

**How $c'$ and $\phi'$ are used:**

1. **Yield criterion**: Check if yielding occurs at each Gauss point using the Mohr-Coulomb criterion: $f(\sigma, c', \phi') = 0$
2. **Tangent stiffness matrix**: When yielding occurs, the tangent constitutive matrix $[D_t]$ replaces $[D_s]$. The matrix $[D_t]$ is computed from plasticity theory and incorporates the effects of $c'$ and $\phi'$ through:
   - The yield function $f(\sigma, c', \phi')$ 
   - The plastic flow rule
   - The current stress state

The exact form of $[D_t]$ is determined by the plasticity algorithm, but it always incorporates $c'$ and $\phi'$ through these relationships. For elastic Gauss points (below yield), $[D_s]$ is used. For yielded Gauss points, $[D_t]$ is used in the element stiffness calculation.

## Element Construction

### Discretization

The continuous domain is divided into finite elements. For 3D analysis:
- **Pile elements**: Solid elements (e.g., 8-node hexahedral) representing the concrete barrette
- **Soil elements**: Solid elements (e.g., 8-node hexahedral or 6-node wedge) representing the soil

### Strain-Displacement Relationship

The strain-displacement matrix $[B]^e$ relates element strains to element nodal displacements:

$$\{\epsilon\}^e = [B]^e \{u\}^e$$

The $[B]^e$ matrix is computed automatically by FEA software based on element geometry and shape functions.

### Pile Element Stiffness Matrix

For concrete pile elements, the element stiffness matrix is:

$$[k]^e_{pile} = \int_{V^e} [B]^T [D_c] [B] \, dV$$

Where $[D_c]$ is the constitutive matrix for concrete (uses $E_c$ and $\nu_c$).

### Soil Element Stiffness Matrix

For soil elements, the element stiffness matrix is:

$$[k]^e_{soil} = \int_{V^e} [B]^T [D] [B] \, dV$$

Where $[D]$ depends on the behavior:
- **Elastic behavior**: $[D] = [D_s]$ (uses $E_s$ and $\nu_s$)
- **Plastic behavior** (non-linear analysis): $[D] = [D_t]$ at yielded Gauss points (incorporates $c'$ and $\phi'$ through plasticity)

The integration is performed numerically using Gauss quadrature at integration points within each element.

## Global System Assembly

### Global Stiffness Matrix

Element stiffness matrices are assembled into the global stiffness matrix:

$$[K] = \sum_{e=1}^{n_{elem}} [C]^e [k]^e ([C]^e)^T$$

Where $[C]^e$ is the connectivity matrix mapping element degrees of freedom to global degrees of freedom.

### Global Equilibrium Equation

The assembled system of equations is:

$$[K]\{u\} = \{F\}$$

Where:
- $[K]$ = global stiffness matrix
- $\{u\}$ = global displacement vector (unknown)
- $\{F\}$ = global force vector (applied loads)

### Solution Process

1. **Compute element stiffness matrices**: For each element, calculate $[k]^e$ using appropriate $[D]$ matrix (pile or soil)
2. **Assemble global matrix**: Combine element contributions into $[K]$
3. **Apply boundary conditions**: Modify $[K]$ and $\{F\}$ to enforce displacement constraints
4. **Solve**: Compute $\{u\} = [K]^{-1}\{F\}$
5. **Post-process**: Extract element strains and stresses:
   - $\{\epsilon\}^e = [B]^e \{u\}^e$
   - $\{\sigma\}^e = [D] \{\epsilon\}^e$

## Non-Linear Analysis

For non-linear soil behavior (Mohr-Coulomb plasticity), the solution requires iteration:

1. Check yielding at each Gauss point using the Mohr-Coulomb criterion: $\tau \geq c' + \sigma_n' \tan\phi'$
2. For yielded Gauss points, replace $[D_s]$ with tangent stiffness $[D_t]$ (which incorporates $c'$ and $\phi'$ through plasticity)
3. Compute element stiffness matrices using $[D_t]$ for yielded points and $[D_s]$ for elastic points
4. Assemble global tangent stiffness matrix $[K_t]^{(i)}$
5. Solve equilibrium: $[K_t]^{(i)} \{\Delta u\}^{(i)} = \{F\} - \{R\}^{(i)}$
6. Update displacements: $\{u\}^{(i+1)} = \{u\}^{(i)} + \{\Delta u\}^{(i)}$
7. Iterate until convergence

Where:
- $[K_t]^{(i)}$ = global tangent stiffness matrix at iteration $i$ (assembled from element matrices using $[D_t]$ for yielded Gauss points)
- $\{R\}^{(i)}$ = residual force vector (unbalanced forces)
- $\{\Delta u\}^{(i)}$ = displacement increment at iteration $i$

## References

- Poulos, H. G., & Davis, E. H. (1980). *Pile Foundation Analysis and Design*. John Wiley & Sons.
- Potts, D. M., & Zdravkovic, L. (2001). *Finite Element Analysis in Geotechnical Engineering: Theory*. Thomas Telford.
- FHWA (2010). *Geotechnical Engineering Circular No. 10: Drilled Shafts: Construction Procedures and LRFD Design Methods*.
