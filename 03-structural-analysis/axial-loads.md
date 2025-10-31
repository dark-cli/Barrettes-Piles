# Axial Load Analysis

## Overview

Structural analysis of barrettes under axial loading involves evaluating the concrete and reinforcement capacity, considering both compressive and tensile loading scenarios.

## Axial Compression Capacity

### Concrete Contribution

The ultimate axial compression capacity is:

$$P_{u,conc} = 0.85f_c'(A_g - A_s) + f_y A_s$$

Where:
- $f_c'$ = concrete compressive strength (MPa)
- $A_g$ = gross cross-sectional area (m²)
- $A_s$ = reinforcement area (m²)
- $f_y$ = reinforcement yield strength (MPa)

### Rectangular Cross-Section

For a rectangular barrette with dimensions $B \times L$:

$$A_g = B \times L$$

### Slenderness Effects

For long barrettes, consider buckling:

$$\frac{L_{eff}}{r} > \text{Critical slenderness ratio}$$

Where:
- $L_{eff}$ = effective length (m)
- $r$ = radius of gyration = $\sqrt{I/A}$ (m)

For rectangular section:
$$r = \frac{B}{\sqrt{12}} \text{ (weak axis)}$$
$$r = \frac{L}{\sqrt{12}} \text{ (strong axis)}$$

### Reduced Capacity Due to Slenderness

$$P_{u,reduced} = \phi \times P_{u,conc}$$

Where $\phi$ is a reduction factor based on slenderness.

## Axial Tension Capacity

### Reinforcement Capacity

$$T_u = f_y \times A_s$$

Where:
- $T_u$ = ultimate tension capacity (kN)
- $f_y$ = reinforcement yield strength (MPa)
- $A_s$ = total reinforcement area (m²)

### Bond Development

Ensure adequate development length for reinforcement:

$$L_d = \frac{f_y \phi}{4f_{bd}}$$

Where:
- $\phi$ = bar diameter (mm)
- $f_{bd}$ = design bond strength (MPa)

## Combined Axial and Bending

### Interaction Diagrams

For combined loading, use interaction diagrams considering:

$$P_u = f(P, M_x, M_y)$$

Where $M_x$ and $M_y$ are moments about the strong and weak axes.

### Rectangular Stress Block

For rectangular barrettes, calculate capacity using rectangular stress block assumption with neutral axis position determined by equilibrium.

## Load Distribution Along Length

### Friction and End Bearing

The axial load varies with depth:

$$P(z) = P_{applied} - Q_{shaft}(z)$$

Where $Q_{shaft}(z)$ is the cumulative shaft resistance from top to depth $z$.

### Structural Design Loads

Design based on:
- Maximum axial force (at head)
- Minimum axial force (at base)
- Intermediate values for reinforcement layout

## Code Requirements

### ACI 318 (if applicable)

- Strength reduction factors: $\phi_c = 0.65$ to $0.75$, $\phi_t = 0.90$
- Minimum reinforcement: Typically 1% of gross area
- Maximum reinforcement: Typically 8% of gross area

### Eurocode 2

- Partial factors: $\gamma_c = 1.5$ (concrete), $\gamma_s = 1.15$ (steel)
- Design strengths: $f_{cd} = f_{ck}/\gamma_c$, $f_{yd} = f_{yk}/\gamma_s$
- Minimum and maximum reinforcement ratios

## References

- ACI Committee 318 (2019). *Building Code Requirements for Structural Concrete (ACI 318-19)*.
- EN 1992-1-1 (2004). *Eurocode 2: Design of concrete structures - Part 1-1: General rules and rules for buildings*.

