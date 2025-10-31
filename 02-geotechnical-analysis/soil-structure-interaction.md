# Soil-Structure Interaction

## Overview

Soil-structure interaction (SSI) analysis considers the mutual influence between the barrette and surrounding soil, accounting for stiffness, damping, and non-linear behavior.

## Interaction Mechanisms

### Load Transfer

- **Base resistance**: Load transfer at barrette base
- **Shaft resistance**: Load transfer along barrette perimeter
- **Load distribution**: How loads are distributed with depth

### Displacement Compatibility

- **Settlement**: Vertical displacement compatibility
- **Lateral displacement**: Horizontal movement compatibility
- **Rotation**: Angular compatibility at connections

### Stress Interaction

- **Contact stresses**: Normal and shear stresses at interface
- **Stress redistribution**: Changes in soil stress state
- **Failure mechanisms**: Progressive failure development

## Interface Behavior

### Friction and Adhesion

For cohesive soils:
$$\tau_{max} = \alpha \times c_u$$

For granular soils:
$$\tau_{max} = \sigma_n' \times \tan\delta$$

Where:
- $\alpha$ = adhesion factor (0.3 to 0.6)
- $\delta$ = interface friction angle (typically 2/3 to 3/4 of $\phi'$)
- $c_u$ = undrained shear strength
- $\sigma_n'$ = effective normal stress

### Slip and Separation

- **Slip**: Relative movement between barrette and soil
- **Separation**: Gap formation under uplift or lateral loading
- **Re-contact**: Re-establishment of contact after separation

## Stiffness Considerations

### Barrette Stiffness

$$K_b = \frac{EA}{L}$$

Where:
- $E$ = modulus of elasticity (kN/m²)
- $A$ = cross-sectional area (m²)
- $L$ = length (m)

### Soil Stiffness

#### Modulus of Subgrade Reaction

$$k = \frac{E_s}{B(1-\nu^2)}$$

Where $E_s$ is the soil modulus.

#### Equivalent Spring Constants

For different degrees of freedom:
- **Vertical**: $K_v = k_v A$
- **Horizontal**: $K_h = k_h A$
- **Rotational**: $K_r = k_r I$

## Numerical Modeling Approaches

### Spring-Dashpot Models

Simple models using:
- Springs for stiffness
- Dashpots for damping
- Non-linear spring behavior

### Continuum Models

Full 3D continuum modeling:
- Soil as continuum medium
- Barrette as structural element
- Interface elements for interaction

### Hybrid Models

Combination of:
- Analytical solutions for far-field
- Numerical methods for near-field
- Simplified models for interfaces

## Dynamic Considerations

### Natural Frequency

$$f_n = \frac{1}{2\pi}\sqrt{\frac{K_{eq}}{M_{eq}}}$$

Where $K_{eq}$ and $M_{eq}$ are equivalent stiffness and mass.

### Damping

- **Material damping**: Soil and concrete internal damping
- **Radiation damping**: Energy loss through wave propagation
- **Interface damping**: Friction and adhesion effects

## Group Interaction

### Load Distribution

Groups of barrettes redistribute loads:
- Stiffer barrettes take more load
- Settlement compatibility affects load sharing
- Rotational effects in groups

### Efficiency Factors

Group efficiency for various response parameters:
- **Settlement**: $\eta_s = s_{group}/s_{single}$
- **Capacity**: $\eta_c = Q_{group}/(n \times Q_{single})$
- **Stiffness**: $\eta_k = K_{group}/(n \times K_{single})$

## References

- Poulos, H. G., & Davis, E. H. (1980). *Pile Foundation Analysis and Design*. John Wiley & Sons.
- Gazetas, G. (1991). Foundation vibrations. *Foundation Engineering Handbook*, 553-593.
- Wolf, J. P. (1985). *Dynamic Soil-Structure Interaction*. Prentice-Hall.

