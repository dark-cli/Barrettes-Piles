# Lateral Resistance and Deflection

## Overview

Barrettes are particularly effective for resisting lateral loads due to their rectangular cross-section, which provides higher moment of inertia in the strong axis direction.

## P-y Curve Method (Winkler Foundation)

### Principle

The soil is modeled as a series of independent springs (Winkler foundation) with non-linear load-displacement relationships (p-y curves).

### Governing Differential Equation

For a barrette under lateral loading: 

$$EI\frac{d^4y}{dz^4} + Q\frac{d^2y}{dz^2} - py = 0$$

Where:
- $E$ = modulus of elasticity of barrette (kN/m²)
- $I$ = moment of inertia (m⁴)
- $y$ = lateral deflection (m)
- $z$ = depth (m)
- $Q$ = axial load (kN)
- $p$ = soil reaction per unit length (kN/m)

### P-y Curves for Different Soils

#### Soft Clay

$$p = 0.5p_u\left(\frac{y}{y_{50}}\right)^{1/3} \text{ for } y \leq 8y_{50}$$

$$p = p_u \text{ for } y > 8y_{50}$$

Where:
$$p_u = \left(3 + \frac{\gamma'z}{c_u} + \frac{Jz}{B}\right)c_uB$$

$$y_{50} = 2.5\epsilon_{50}B$$

#### Stiff Clay

Similar form with different parameters based on soil strength.

#### Sand

$$p = Ap_u\tanh\left(\frac{kz}{Ap_u}y\right)$$

Where:
$$p_u = \min\left[(C_1z + C_2D)\gamma'z, C_3D\gamma'z\right]$$

And $A$, $C_1$, $C_2$, $C_3$ are empirical constants.

### Modification for Rectangular Cross-Section

For rectangular barrettes, use effective width:

$$B_{eff} = B \text{ for loading perpendicular to width}$$
$$B_{eff} = L \text{ for loading perpendicular to length}$$

## Lateral Load Capacity

### Ultimate Lateral Resistance

The ultimate lateral capacity depends on:
- Soil strength parameters
- Barrette dimensions
- Embedment depth
- Boundary conditions at head

### Free-Head Conditions

For free-head barrettes:

$$H_u = \frac{M_u}{e + f}$$

Where:
- $H_u$ = ultimate lateral load (kN)
- $M_u$ = ultimate moment capacity (kN·m)
- $e$ = eccentricity (m)
- $f$ = depth to maximum moment (m)

### Fixed-Head Conditions

Fixed-head barrettes can resist higher lateral loads due to moment restraint at the head.

## Moment of Inertia Considerations

### Strong and Weak Axes

Rectangular barrettes have different moments of inertia:

$$I_{strong} = \frac{BL^3}{12}$$

$$I_{weak} = \frac{LB^3}{12}$$

Where $L > B$ is the typical orientation.

### Design Implications

- Orient barrette with strong axis perpendicular to primary lateral load
- Consider bidirectional loading cases
- Account for rotation of loading direction

## Numerical Analysis

### Beam-Column Analysis

Barrettes can be analyzed as beam-columns with:
- $P-\Delta$ effects
- Non-linear material behavior
- Distributed soil springs (p-y curves)

### Finite Element Analysis

3D FEA allows for:
- Complete soil-structure interaction
- Group effects
- Complex geometry and loading
- Non-linear soil and structural behavior

## Group Effects

### P-Multiplier Method

For groups of barrettes, use p-multipliers:

$$p_{group} = p_{m} \times p_{single}$$

Where $p_m$ depends on:
- Barrette spacing
- Row position (leading, trailing, interior)
- Load direction

### Typical P-Multipliers

| Row Position | Spacing | P-Multiplier |
|--------------|---------|--------------|
| Leading | 3B | 0.8-1.0 |
| Trailing | 3B | 0.3-0.5 |
| Interior | 3B | 0.4-0.7 |

## References

- FHWA (2010). *Geotechnical Engineering Circular No. 10: Drilled Shafts: Construction Procedures and LRFD Design Methods*.
- Reese, L. C., & Van Impe, W. F. (2011). *Single Piles and Pile Groups Under Lateral Loading*. CRC Press.
- Poulos, H. G. (1971). Behavior of laterally loaded piles: I—Single piles. *Journal of the Soil Mechanics and Foundations Division*, 97(5), 711-731.

