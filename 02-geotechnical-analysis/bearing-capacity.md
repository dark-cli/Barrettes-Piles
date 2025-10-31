# Bearing Capacity Analysis

## Overview

Bearing capacity analysis determines the maximum load that a barrette can safely support without experiencing geotechnical failure. Barrettes can have various cross-sectional shapes including rectangular, L-shaped, T-shaped, or wall-like configurations. For accurate analysis of these complex geometries, finite element analysis is the recommended approach.

## General Bearing Capacity Equation

### Theoretical Background

The general bearing capacity equation for foundations is:

$$q_u = c'N_c + q'N_q + \frac{1}{2}\gamma B' N_\gamma$$

Where:
- $c'$ = effective cohesion of soil (kN/m²)
- $q'$ = effective overburden pressure at foundation level (kN/m²)
- $\gamma$ = unit weight of soil (kN/m³)
- $B'$ = effective width (m)
- $N_c$, $N_q$, $N_\gamma$ = bearing capacity factors (functions of friction angle $\phi'$)

### Limitations of Analytical Methods for Barrettes

While this equation forms the theoretical basis for bearing capacity analysis, analytical methods have significant limitations when applied to barrettes:

1. **Complex Geometries**: Barrettes can have rectangular, L-shaped, T-shaped, or wall-like cross-sections. Analytical methods require extensive approximations and shape factor modifications that are not well-established for non-rectangular shapes.

2. **Corner and Stress Concentration Effects**: Rectangular and complex geometries introduce stress concentrations at corners and re-entrant angles that analytical methods cannot accurately capture.

3. **Three-Dimensional Behavior**: Barrettes exhibit complex three-dimensional load transfer mechanisms involving non-uniform stress distribution around the perimeter that extend beyond simplified analytical assumptions.

4. **Soil-Structure Interaction**: The interaction between complex barrette geometries and surrounding soil involves progressive failure and non-uniform contact stresses that cannot be modeled adequately by analytical approaches.

5. **Code Limitations**: Most design codes (FHWA, ICE, Eurocode) provide guidance primarily for circular piles. Adaptations for barrettes require significant engineering judgment and approximations, particularly for L, T, or wall geometries.

6. **Group Effects**: When barrettes are used in groups with complex geometries, analytical methods become increasingly unreliable.

For these reasons, **finite element analysis is the recommended method for accurate bearing capacity evaluation of barrettes**, especially for:
- Complex geometries (L, T, walls)
- Important or high-load projects
- Projects requiring detailed understanding of failure mechanisms
- Validation and verification purposes

## Finite Element Analysis for Bearing Capacity

### Overview

Finite element analysis provides a powerful numerical tool for analyzing barrettes, allowing for complex soil-structure interaction, non-linear behavior, and three-dimensional effects that cannot be captured by analytical methods. FEA can accurately model all barrette geometries including rectangular, L-shaped, T-shaped, and wall-like configurations.

For comprehensive details on finite element analysis methodology, soil constitutive models, mesh generation, and analysis procedures, refer to the [Finite Element Analysis Guide](./finite-element-analysis.md).

### Key Points for Bearing Capacity Analysis

For bearing capacity evaluation using FEA:

- **Recommended soil model**: Mohr-Coulomb model
- **Load application**: Load-controlled method (load increment)
- **Failure criterion**: Settlement-based (25 mm for normal structures, 50 mm for rafts)
- **Analysis type**: Non-linear analysis with incremental loading
- **Result extraction**: Load-displacement curve, plastic zone development, stress distribution

See [Finite Element Analysis Guide](./finite-element-analysis.md) for detailed step-by-step procedures, soil constitutive models, mesh generation, boundary conditions, and best practices.

### Step-by-Step Calculation Procedure for Bearing Capacity

#### Step 1: Model Setup

**1.1 Geometry Definition**
- Create barrette geometry (rectangular, L, T, or wall shape)
- Define dimensions: length $L$, width $B$, embedment depth $D$
- Model soil domain extending:
  - 3 to 5 times barrette width laterally
  - 2 to 3 times embedment depth below base

**1.2 Material Properties**

*Barrette properties:*
- Elastic modulus: $E_c$ = 20-40 GPa (concrete)
- Poisson's ratio: $\nu_c$ = 0.15-0.2
- Unit weight: $\gamma_c$ = 24 kN/m³

*Soil properties:*
- Select constitutive model (Mohr-Coulomb recommended for bearing capacity)
- Define: cohesion $c'$, friction angle $\phi'$, unit weight $\gamma$, Young's modulus $E_s$
- Estimate $E_s$ from correlations (e.g., $E_s = \alpha \times N_{SPT}$ or from CPT)

#### Step 2: Mesh Generation

**2.1 Element Sizing**
- **Barrette elements**: Fine mesh (element size = $B/10$ to $B/20$)
- **Corners and junctions**: Extra fine mesh for stress concentrations (L, T shapes)
- **Near-field soil**: Medium mesh ($B/5$ to $B/10$)
- **Far-field soil**: Coarse mesh ($B$ to $2B$)

**2.2 Element Types**
- 8-node hexahedral elements for soil
- Interface elements between barrette and soil
- Ensure proper connectivity at junctions for complex shapes

#### Step 3: Boundary Conditions

- **Lateral boundaries**: Roller supports (zero horizontal displacement: $u_x = 0$ or $u_y = 0$)
- **Bottom boundary**: Fixed (zero displacement in all directions: $u_x = u_y = u_z = 0$)
- **Top surface**: Free (no constraints)

#### Step 4: Initial Stress State

Establish geostatic equilibrium:

$$\sigma_v' = \gamma' z$$

$$\sigma_h' = K_0 \sigma_v'$$

Where $K_0 = 1 - \sin\phi'$ (Jaky's formula) or use site-specific value.

**Initial step procedure:**
1. Apply gravitational acceleration
2. Solve for equilibrium (linear elastic analysis)
3. Verify stress distribution is reasonable

#### Step 5: Construction Sequence

**5.1 Sequence of Steps**

1. **Step 1 - Geostatic**: Establish initial soil stresses (equilibrium under self-weight)
2. **Step 2 - Excavation**: "Kill" or remove soil elements where barrette will be placed
3. **Step 3 - Installation**: "Activate" barrette elements (with self-weight)
4. **Step 4 - Contact**: Establish contact between barrette and surrounding soil
5. **Step 5 - Equilibrium**: Allow system to reach equilibrium after installation

#### Step 6: Load Application for Bearing Capacity

**Load-Controlled Method (Load Increment)**

Apply vertical load at barrette head incrementally:

- Increment 1: $Q_1 = 0.1 \times Q_{estimated}$
- Increment 2: $Q_2 = 0.2 \times Q_{estimated}$
- Increment 3: $Q_3 = 0.3 \times Q_{estimated}$
- Continue increasing load in increments (typically 10-20% of estimated capacity per increment)

**Procedure:**
1. Apply load increment
2. Solve for equilibrium
3. Extract settlement at barrette head
4. Check if failure criterion is reached
5. If not, proceed to next increment
6. Continue until failure criterion is met

#### Step 7: Non-Linear Analysis

For each load/displacement increment:

1. **Apply increment**: Apply load or displacement
2. **Newton-Raphson iteration**: Solve equilibrium equations iteratively
3. **Check convergence**:
   - Force residual < 0.5% to 1% of applied load
   - Displacement change < tolerance
   - Energy change < tolerance
4. **If converged**: Proceed to next increment
5. **If not converged**: Reduce increment size and retry

#### Step 8: Extract Results

**8.1 Load-Displacement Curve**

Plot vertical displacement ($\delta$) versus applied load or reaction force ($Q$):

| Load Q (kN) | Displacement δ (mm) |
|-------------|---------------------|
| 1000        | 2.5                 |
| 2000        | 5.1                 |
| 3000        | 8.2                 |
| 4000        | 12.5                |
| 5000        | 18.3                |
| 6000        | 28.7 ← Failure     |

**8.2 Plastic Zone Development**

Monitor plastic points (yielded elements) at each increment:
- Identify when extensive plastic zones form
- Check if plastic zone connects barrette base to surface or extends laterally
- Visualize failure mechanism

**8.3 Stress Distribution**

Extract at each increment:
- Base normal stress: $\sigma_{base}$
- Shaft shear stress: $\tau_{shaft}$ along perimeter
- Contact pressures around barrette
- Soil stress contours

#### Step 9: Determine Ultimate Bearing Capacity

**Settlement Criterion Method**

The ultimate bearing capacity is defined as the load at which a specified settlement is reached:

**For normal structures:**
$$Q_u = Q(\delta = 25 \text{ mm}) = Q(\delta = 1 \text{ inch})$$

**For rafts:**
$$Q_u = Q(\delta = 50 \text{ mm}) = Q(\delta = 2 \text{ inches})$$

**Procedure:**
1. Extract settlement at each load increment
2. Plot load-displacement curve
3. Identify load corresponding to the specified settlement (25 mm for normal structures, 50 mm for rafts)
4. This load is the ultimate bearing capacity $Q_u$

**Alternative: Non-Convergence Method**

If solution fails to converge at a load increment before reaching the specified settlement, the ultimate capacity can be taken as the last successfully converged load increment.

#### Step 10: Validation and Verification

**10.1 Mesh Sensitivity Check**

- Refine mesh and repeat analysis
- Compare results with coarser mesh
- Ensure mesh-independent results

**10.2 Boundary Effects Check**

- Increase domain size and compare results
- Verify boundaries don't affect results

**10.3 Comparison with Analytical Methods**

- Compare $Q_u$ with simplified analytical estimates (for validation)
- Check order of magnitude consistency

**10.4 Field Validation**

- Compare with load test data if available
- Adjust model if significant discrepancies exist

#### Step 11: Report Results

Typical results to report:

1. **Ultimate bearing capacity**: $Q_u$ (kN)
2. **Load-displacement curve**: Graphical plot
3. **Base resistance contribution**: $Q_{base}$ from base stress integration
4. **Shaft resistance contribution**: $Q_{shaft}$ from shaft stress integration
5. **Failure mechanism**: Plastic zone plots and stress distribution
6. **Settlement at working load**: Settlement at $Q_{working} = Q_u / FOS$

### Analysis Procedures Summary

#### Load Application

1. **Initial geostatic step**: Establish initial stress state
2. **Construction sequence**: Activate barrette elements gradually (important for complex shapes)
3. **Load application**: Apply service or ultimate loads incrementally

#### Non-linear Analysis

- **Load control**: Apply loads in increments (recommended method)
- **Newton-Raphson iteration**: Solve equilibrium equations iteratively at each increment
- **Increment size**: Typically 10-20% of estimated capacity per increment

#### Convergence Criteria

- **Force equilibrium**: Residual forces < tolerance (typically 0.5% to 1% of applied load)
- **Displacement**: Change in displacement < tolerance
- **Energy**: Change in energy < tolerance

### Interpretation of FEA Results

#### Bearing Capacity

The ultimate bearing capacity from FEA can be determined by:

1. **Load-displacement curve**: Identify point of large displacement increase
2. **Plastic zone development**: Observe propagation of failure surface
3. **Convergence difficulties**: Non-convergence may indicate failure

$$Q_{ultimate} = \text{Load at failure from FEA}$$

#### Load Distribution

- **Base resistance**: Extract normal stresses at barrette base
- **Shaft resistance**: Extract shear stresses along barrette shaft (important for complex shapes with varying perimeter)
- **Load transfer**: Analyze load distribution with depth
- **Shape effects**: For L and T shapes, identify load distribution at junctions

#### Displacements

- **Settlement**: Vertical displacement at barrette head
- **Lateral displacement**: Horizontal movement under lateral loads
- **Rotation**: Angular rotation at barrette head
- **Differential displacement**: For complex shapes, check for differential settlement across cross-section

#### Stress Distribution

- **Soil stresses**: Identify stress concentrations around barrette
- **Contact stresses**: Base and shaft contact pressures (may vary significantly for complex shapes)
- **Failure zones**: Plastic zones indicating failure mechanism
- **Corner effects**: Examine stress concentrations at corners and re-entrant angles

### Advantages of FEA for Barrettes

- Captures complex geometry (rectangular, L, T, walls) without approximations
- Accounts for non-linear soil behavior
- Includes three-dimensional effects
- Models construction sequence
- Handles complex loading conditions
- Evaluates group effects
- Captures stress concentrations at corners and junctions
- Models progressive failure mechanisms

### Limitations of FEA

- Requires significant computational resources
- Model calibration needed for soil parameters
- Results sensitive to input parameters
- Requires expertise in numerical modeling
- May not capture all physical phenomena
- Mesh quality significantly affects results

### Best Practices for FEA

1. **Start simple**: Begin with linear elastic model to verify geometry and boundary conditions
2. **Incremental complexity**: Add non-linearity gradually
3. **Parameter sensitivity**: Conduct sensitivity analysis for soil parameters
4. **Model validation**: Compare with field data or simplified analytical solutions where possible
5. **Mesh refinement**: Check mesh sensitivity, especially at corners and junctions
6. **Boundary effects**: Verify domain size is adequate (larger may be needed for wall-like barrettes)
7. **Convergence**: Ensure proper convergence at each load increment
8. **Documentation**: Document all assumptions, parameters, and model geometry

## References

- Terzaghi, K. (1943). *Theoretical Soil Mechanics*. John Wiley & Sons.
- Poulos, H. G., & Davis, E. H. (1980). *Pile Foundation Analysis and Design*. John Wiley & Sons.
- FHWA (2010). *Geotechnical Engineering Circular No. 10: Drilled Shafts: Construction Procedures and LRFD Design Methods*.
