# Settlement Analysis

## Overview

Settlement analysis predicts the vertical deformation of barrettes under applied loads. Barrettes can have various cross-sectional shapes including rectangular, L-shaped, T-shaped, or wall-like configurations. For accurate prediction of settlement in these complex geometries, finite element analysis is the recommended approach.

## Limitations of Analytical Methods for Barrettes

### General Settlement Equations

Traditional analytical methods for settlement prediction include:

- Elastic theory with influence factors
- Layer summation method  
- One-dimensional consolidation theory

However, these methods have significant limitations for barrettes:

1. **Complex Geometries**: Rectangular, L-shaped, T-shaped, and wall-like barrettes require complex influence factors that are not well-established or require extensive simplifications.

2. **Three-Dimensional Effects**: Analytical methods typically assume simplified stress distributions that may not accurately represent the actual three-dimensional behavior of deep barrettes with complex cross-sections.

3. **Progressive Settlement**: The interaction between base resistance, shaft resistance, and progressive mobilization of soil resistance cannot be adequately captured by simplified analytical methods.

4. **Complex Soil Profiles**: Layered or heterogeneous soil profiles require significant simplifications in analytical approaches that may not accurately represent actual behavior.

5. **Time-Dependent Behavior**: Consolidation and creep behavior in complex soil profiles and around complex geometries are better captured by numerical methods.

6. **Non-Rectangular Shapes**: For L-shaped, T-shaped, or wall-like barrettes, analytical methods become impractical or require extensive approximations.

Therefore, **finite element analysis is the recommended method for accurate settlement prediction of barrettes**, particularly for complex geometries and important projects.

## Finite Element Analysis for Settlement

### Overview

Finite element analysis provides a comprehensive numerical tool for predicting barrette settlement, allowing for complex geometries, realistic three-dimensional stress distribution, non-linear soil behavior, progressive settlement, and time-dependent consolidation behavior.

For comprehensive details on finite element analysis methodology, soil constitutive models, mesh generation, analysis procedures, and interpretation of results, refer to the [Finite Element Analysis Guide](./finite-element-analysis.md).

### Key Points for Settlement Analysis

For settlement prediction using FEA:

- **Recommended soil models**: 
  - Hardening Soil model for granular soils and overconsolidated clays
  - Modified Cam Clay model for consolidation in cohesive soils
- **Load application**: Apply service loads incrementally
- **Analysis type**: 
  - Non-linear analysis for immediate settlement
  - Consolidation analysis for time-dependent settlement
- **Result extraction**: Settlement-time curves, settlement distribution, differential settlement

### Settlement Analysis Considerations

#### Consolidation Analysis

For time-dependent settlement in cohesive soils:
1. **Initial settlement**: Immediate/elastic settlement
2. **Primary consolidation**: Pore pressure dissipation with time
3. **Secondary compression**: Long-term creep

#### Consolidation Parameters

- **Coefficient of consolidation**: $c_v$ (vertical), $c_h$ (horizontal)
- **Permeability**: $k_v$, $k_h$ (may vary with direction)
- **Compressibility**: $\lambda$, $\kappa$ (Modified Cam Clay)

#### Settlement Monitoring Points

For complex shapes, monitor settlement at:
- Center of barrette
- Corners (for rectangular shapes)
- Junction points (for L and T shapes)
- Various points along length (for wall-like shapes)

See [Finite Element Analysis Guide](./finite-element-analysis.md) for detailed procedures on consolidation analysis, time stepping, and result interpretation.

## References

- Poulos, H. G., & Davis, E. H. (1980). *Pile Foundation Analysis and Design*. John Wiley & Sons.
- FHWA (2010). *Geotechnical Engineering Circular No. 10: Drilled Shafts: Construction Procedures and LRFD Design Methods*.
- EN 1997-1 (2004). *Eurocode 7: Geotechnical design - Part 1: General rules*.
