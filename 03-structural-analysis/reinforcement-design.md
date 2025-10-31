# Reinforcement Design

## Overview

Reinforcement design for barrettes must account for the rectangular geometry, bidirectional loading, and structural requirements from both geotechnical and structural considerations.

## Reinforcement Requirements

### Minimum Reinforcement

#### Longitudinal Reinforcement

Minimum longitudinal reinforcement ratio:

$$\rho_{min} = \frac{A_{s,min}}{A_g} \geq 0.01 \text{ to } 0.02$$

Where:
- $A_{s,min}$ = minimum reinforcement area (m²)
- $A_g$ = gross cross-sectional area (m²)

For rectangular barrette $B \times L$:
$$A_{s,min} = \rho_{min} \times B \times L$$

#### Transverse Reinforcement

Minimum transverse reinforcement (ties or spirals):
- Minimum diameter: 10 to 12 mm typically
- Maximum spacing: 16 times smallest longitudinal bar diameter or 300 mm

### Maximum Reinforcement

Maximum reinforcement ratio to ensure ductility:

$$\rho_{max} = 0.75\rho_b$$

Where $\rho_b$ is the balanced reinforcement ratio.

## Reinforcement Layout

### Longitudinal Bars

#### Distribution Around Perimeter

For rectangular barrettes, distribute bars:
- Minimum 4 bars (one at each corner)
- Typically 8 to 16 bars for larger sections
- Uniform spacing around perimeter preferred

#### Corner Reinforcement

Additional considerations at corners:
- Corner bars required
- Increased confinement at corners
- Adequate cover maintained

### Transverse Reinforcement

#### Ties

For rectangular sections, use rectangular ties:
- Encircling longitudinal bars
- 135° hooks at ends
- Spacing per code requirements

#### Spacing Requirements

$$s \leq \min\left(16\phi_{long}, 48\phi_{tie}, b_{min}, 300 \text{ mm}\right)$$

Where:
- $\phi_{long}$ = diameter of smallest longitudinal bar
- $\phi_{tie}$ = diameter of tie bar
- $b_{min}$ = smallest barrette dimension

## Design for Axial Loads

### Compression

$$P_{u,design} \leq \phi P_n$$

Where:
$$\phi P_n = \phi[0.85f_c'(A_g - A_s) + f_y A_s]$$

Design reinforcement to satisfy:
$$A_s = \frac{P_{u,design}/\phi - 0.85f_c'A_g}{f_y - 0.85f_c'}$$

### Tension

$$T_{u,design} \leq \phi T_n$$

Where:
$$\phi T_n = \phi f_y A_s$$

Design reinforcement:
$$A_s = \frac{T_{u,design}}{\phi f_y}$$

## Design for Bending

### Uniaxial Bending

For bending about strong axis:

$$M_{u,design} \leq \phi M_n$$

Reinforcement area determined from:
$$M_n = A_s f_y\left(d - \frac{a}{2}\right)$$

With:
$$a = \frac{A_s f_y}{0.85f_c' B}$$

### Biaxial Bending

For combined $M_x$ and $M_y$:
- Use interaction diagrams
- Design reinforcement to satisfy interaction surface
- Consider corner reinforcement contributions

## Design for Shear

### Shear Reinforcement

When $V_u > \phi V_c$:

$$A_v = \frac{(V_u - \phi V_c)s}{\phi f_y d}$$

Where:
- $A_v$ = area of shear reinforcement per spacing (m²)
- $s$ = spacing (m)

### Minimum Shear Reinforcement

$$A_{v,min} = 0.062\sqrt{f_c'}\frac{b_w s}{f_y}$$

## Development and Anchorage

### Development Length

$$L_d = \frac{\phi f_y}{4f_{bd}}$$

Where $f_{bd}$ is the design bond strength.

### Hook Requirements

For bars with hooks:
$$L_{dh} = \frac{0.24\phi f_y}{\sqrt{f_c'}}$$

## Detailing Considerations

### Spacing Requirements

- Minimum spacing: Maximum of (bar diameter, 25 mm, 1.33 times maximum aggregate size)
- Maximum spacing: Per code limitations

### Cover Requirements

- Minimum cover: 75 to 100 mm typically
- Increased for aggressive environments
- Maintained at corners

### Splices

#### Lap Splices

$$L_{lap} = \psi L_d$$

Where $\psi$ depends on:
- Bar location (top or bottom)
- Reinforcement ratio
- Splice configuration

#### Mechanical Splices

For high-load applications or space constraints.

## Quality Control

### Reinforcement Inspection

- Verify bar sizes and grades
- Check spacing and cover
- Ensure proper placement
- Verify development lengths

### Construction Tolerances

- Position tolerance: Typically ±25 mm
- Cover tolerance: Typically +10 mm / -5 mm
- Verticality: Per code requirements

## References

- ACI Committee 318 (2019). *Building Code Requirements for Structural Concrete (ACI 318-19)*.
- EN 1992-1-1 (2004). *Eurocode 2: Design of concrete structures - Part 1-1: General rules and rules for buildings*.
- ACI Committee 315 (2018). *Details and Detailing of Concrete Reinforcement (ACI 315-18)*.

