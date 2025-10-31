# Bending and Shear Analysis

## Overview

Barrettes must resist bending moments and shear forces from lateral loads, eccentric axial loads, and structural connections. The rectangular cross-section provides directional stiffness advantages.

## Bending Moment Capacity

### Rectangular Cross-Section

For a barrette with dimensions $B \times L$ (width $\times$ length):

#### Strong Axis Bending

Moment of inertia about strong axis:
$$I_{strong} = \frac{BL^3}{12}$$

Section modulus:
$$S_{strong} = \frac{BL^2}{6}$$

#### Weak Axis Bending

Moment of inertia about weak axis:
$$I_{weak} = \frac{LB^3}{12}$$

Section modulus:
$$S_{weak} = \frac{LB^2}{6}$$

### Ultimate Moment Capacity

For rectangular section with reinforcement:

$$M_u = A_s f_y\left(d - \frac{a}{2}\right)$$

Where:
- $A_s$ = tension reinforcement area (m²)
- $f_y$ = reinforcement yield strength (MPa)
- $d$ = effective depth (m)
- $a$ = depth of equivalent stress block = $\frac{A_s f_y}{0.85f_c' B}$

### Balanced Condition

The balanced reinforcement ratio:

$$\rho_b = \frac{0.85\beta_1 f_c'}{f_y} \times \frac{\epsilon_{cu}}{\epsilon_{cu} + \epsilon_y}$$

Where:
- $\beta_1$ = stress block factor (typically 0.65 to 0.85)
- $\epsilon_{cu}$ = ultimate concrete strain (typically 0.003)
- $\epsilon_y$ = yield strain = $f_y/E_s$

### Minimum and Maximum Reinforcement

- **Minimum**: $\rho_{min} = 0.002$ to $0.004$ (typically)
- **Maximum**: $\rho_{max} = 0.75\rho_b$ (typically)

## Biaxial Bending

### Interaction Surface

For biaxial bending:

$$\left(\frac{M_x}{M_{ux}}\right)^\alpha + \left(\frac{M_y}{M_{uy}}\right)^\alpha \leq 1$$

Where $\alpha$ typically ranges from 1.0 to 2.0 depending on reinforcement layout.

### Bresler's Formula

Common approximation:

$$\frac{1}{M_u} = \frac{1}{M_{ux}} + \frac{1}{M_{uy}} - \frac{1}{M_{u,axial}}$$

## Shear Capacity

### Concrete Contribution

$$V_c = 0.17\sqrt{f_c'} b_w d$$

For rectangular barrette:
- $b_w = B$ (for loading parallel to $L$)
- $b_w = L$ (for loading parallel to $B$)

### Reinforcement Contribution

$$V_s = \frac{A_v f_y d}{s}$$

Where:
- $A_v$ = area of shear reinforcement (m²)
- $s$ = spacing of shear reinforcement (m)

### Total Shear Capacity

$$V_u = V_c + V_s \leq 0.25\sqrt{f_c'} b_w d$$

### Maximum Spacing

$$s_{max} = \min\left(\frac{d}{2}, 600 \text{ mm}\right)$$

## Moment-Curvature Relationship

### Section Analysis

For detailed analysis, develop moment-curvature ($M-\phi$) relationship:

1. Assume strain distribution
2. Calculate stress in concrete and steel
3. Integrate to find forces
4. Calculate moment capacity
5. Determine curvature

### Curvature

$$\phi = \frac{\epsilon_c}{c}$$

Where:
- $\epsilon_c$ = extreme fiber strain
- $c$ = neutral axis depth

## Design Considerations

### Corner Reinforcement

Rectangular barrettes require careful reinforcement at corners:
- Increased confinement
- Corner bars for crack control
- Detailing for stress concentrations

### Reinforcement Layout

- **Longitudinal bars**: Distributed around perimeter
- **Transverse reinforcement**: Ties or spirals
- **Corner bars**: Additional reinforcement at corners

### Cover Requirements

- Minimum cover: Typically 75 to 100 mm
- Increased cover for aggressive environments
- Protection for long-term durability

## References

- ACI Committee 318 (2019). *Building Code Requirements for Structural Concrete (ACI 318-19)*.
- EN 1992-1-1 (2004). *Eurocode 2: Design of concrete structures - Part 1-1: General rules and rules for buildings*.
- MacGregor, J. G., & Wight, J. K. (2005). *Reinforced Concrete: Mechanics and Design*. Pearson.

