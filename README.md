# Geotechnical and Structural Analyses of Barrettes

## Overview

This resource provides a comprehensive guide to the geotechnical and structural analyses of barrettes (rectangular deep foundation elements). The guide covers theoretical foundations, practical design methods, and code-based approaches.

**Target Audience**: Geotechnical and structural engineers, engineering students.

## Structure

### [01 - Introduction](./01-introduction/introduction.md)
- Definition of barrettes
- Applications
- Advantages and limitations
- Overview of analysis approaches

### [02 - Geotechnical Analysis](./02-geotechnical-analysis/)
- [Bearing Capacity](./02-geotechnical-analysis/bearing-capacity.md)
  - Terzaghi's bearing capacity (modified for rectangular shape)
  - Methods from codes (FHWA, ICE, Eurocode)
  - Finite element analysis (FEA) with soil models
- [Settlement Analysis](./02-geotechnical-analysis/settlement.md)
- [Lateral Resistance](./02-geotechnical-analysis/lateral-resistance.md)
- [Soil-Structure Interaction](./02-geotechnical-analysis/soil-structure-interaction.md)

### [03 - Structural Analysis](./03-structural-analysis/)
- [Axial Loads](./03-structural-analysis/axial-loads.md)
- [Bending and Shear](./03-structural-analysis/bending-shear.md)
- [Reinforcement Design](./03-structural-analysis/reinforcement-design.md)
- [Connections](./03-structural-analysis/connections.md)

### [04 - Case Studies](./04-case-studies/case-studies.md)
- Real-world projects
- Design approaches
- Lessons learned

### [05 - Conclusion](./05-conclusion/conclusion.md)
- Summary
- Best practices
- Design workflow
- References

### [Example Problem](./example-problem/)
- **Real case study**: Based on Exim Bank Building, Ho Chi Minh City, Vietnam
- **Complete data**: Geotechnical investigation, soil parameters, structural loads
- **Analysis ready**: All parameters formatted for Plaxis 3D input
- **Documentation**:
  - [Problem description](./example-problem/README.md) - Full project overview
  - [Geotechnical data](./example-problem/geotechnical-data.md) - Soil parameters and properties
  - [Load cases](./example-problem/load-cases.md) - Individual pile loads for Plaxis 3D
  - [Structural loads](./example-problem/structural-loads.md) - Column loads and combinations
  - [Case study source](./example-problem/case-study-source.md) - Original paper reference

## Resources

Additional resources are available in the `resources/` folder:
- `resources/papers/` - Research papers
- `resources/textbooks/` - Textbook references
- `resources/codes_manuals/` - Design codes and manuals
- `resources/figures/` - Figures and diagrams

## Conventions

- **Equations**: LaTeX format with inline ($...$) or display ($$...$$) notation
- **Units**: SI units (metric) primary
- **Citations**: Author-year format with full references
- **Terminology**: Consistent throughout

## Quick Reference

### Key Analysis Methods

1. **Terzaghi's Bearing Capacity** (modified for rectangular shape)
   - Shape factors for rectangular cross-section
   - Depth factors for deep foundations
   - Application to barrettes

2. **Code-Based Methods**
   - FHWA GEC-10 (Drilled Shafts)
   - FHWA GEC-11 (Driven Piles)
   - ICE Specification
   - Eurocode 7

3. **Finite Element Analysis**
   - Soil constitutive models
   - Mesh generation
   - Interpretation of results

## Notes

This guide is a working document and may be updated as additional information becomes available or as design methods evolve.

