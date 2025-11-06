# Barrette Pile Foundation Design - Example Problem

## Quick Navigation

- **[Problem Description](#project-description)** - Building and site information
- **[Geotechnical Data](./geotechnical-data.md)** - Complete soil parameters for Plaxis 3D
- **[Structural Loads](./structural-loads.md)** - Load combinations and values
- **[Case Study Source](./case-study-source.md)** - Original paper reference

---

## Project Overview

This example is **based on a real published case study** from the Mekong Delta, Vietnam (Exim Bank Building, Ho Chi Minh City). The problem includes complete geotechnical investigation data, structural loads, and design requirements adapted from the real project.

**Real Case Study Source**: See [case-study-source.md](./case-study-source.md) for full reference and details about what's real vs. simplified.

**Original Reference**:  
Nguyen, H.M., Fellenius, B.H., Puppala, A.J., Aravind, P., & Tran, Q.T. (2016). "Bidirectional Tests on Two Shaft-Grouted Barrette Piles in the Mekong Delta, Vietnam." *Geotechnical Engineering Journal of the SEAGS & AGSSEA*, 47(1), 15-25.

**Objective**: Design and analyze barrette pile foundations using Plaxis 3D to verify:
- Bearing capacity
- Settlement behavior
- Lateral resistance
- Structural adequacy

---

## Project Description

### Building Information
- **Project Name**: Downtown Commercial Tower (based on Exim Bank Building, Ho Chi Minh City)
- **Location**: Mekong Delta, Vietnam (adapted from real case study)
- **Building Type**: 35-story commercial office tower (original was 40-story)
- **Structure**: Reinforced concrete frame with central core
- **Foundation Type**: Barrette pile foundation system

### Site Conditions
- **Site Area**: 50 m × 50 m
- **Ground Level**: +0.0 m (reference elevation)
- **Groundwater Table**: -2.0 m below ground level
- **Site Access**: Constrained urban site with adjacent buildings
- **Construction Method**: Slurry wall technique for barrette installation

---

## Geotechnical Investigation

### Site Investigation Summary
- **Investigation Date**: 2023
- **Number of Boreholes**: 5 (one at each corner + center)
- **Maximum Depth**: 45 m below ground level
- **Standard Penetration Tests (SPT)**: Conducted at 1.5 m intervals
- **Laboratory Tests**: 
  - Triaxial compression tests (CU and CD)
  - Consolidation tests
  - Direct shear tests
  - Atterberg limits

### Soil Profile

The site consists of the following soil layers:

#### Layer 1: Fill Material (0.0 m to -3.0 m)
- **Thickness**: 3.0 m
- **Description**: Loose to medium dense silty sand with construction debris
- **Classification**: SM (Silty Sand)
- **Unit Weight (γ)**: 17.5 kN/m³
- **Effective Unit Weight (γ')**: 7.5 kN/m³ (below water table)
- **Cohesion (c')**: 5 kN/m²
- **Friction Angle (φ')**: 28°
- **Dilation Angle (ψ)**: 0°
- **Young's Modulus (E)**: 15,000 kN/m²
- **Poisson's Ratio (ν)**: 0.30
- **Undrained Shear Strength (su)**: 25 kN/m²
- **SPT N-value**: 8-12 blows/ft

#### Layer 2: Soft to Medium Clay (-3.0 m to -12.0 m)
- **Thickness**: 9.0 m
- **Description**: Soft to medium stiff silty clay, normally consolidated
- **Classification**: CL (Low Plasticity Clay)
- **Unit Weight (γ)**: 18.0 kN/m³
- **Effective Unit Weight (γ')**: 8.0 kN/m³
- **Cohesion (c')**: 10 kN/m²
- **Friction Angle (φ')**: 22°
- **Dilation Angle (ψ)**: 0°
- **Young's Modulus (E)**: 25,000 kN/m²
- **Poisson's Ratio (ν)**: 0.35
- **Undrained Shear Strength (su)**: 30-50 kN/m² (increasing with depth)
- **SPT N-value**: 4-8 blows/ft
- **Coefficient of Consolidation (cv)**: 2.5 × 10⁻⁷ m²/s
- **Compression Index (Cc)**: 0.35
- **Recompression Index (Cr)**: 0.05

#### Layer 3: Dense Sand (-12.0 m to -25.0 m)
- **Thickness**: 13.0 m
- **Description**: Dense to very dense fine to medium sand
- **Classification**: SP-SM (Poorly Graded Sand with Silt)
- **Unit Weight (γ)**: 19.5 kN/m³
- **Effective Unit Weight (γ')**: 9.5 kN/m³
- **Cohesion (c')**: 0 kN/m²
- **Friction Angle (φ')**: 35°
- **Dilation Angle (ψ)**: 5°
- **Young's Modulus (E)**: 80,000 kN/m²
- **Poisson's Ratio (ν)**: 0.25
- **SPT N-value**: 35-50 blows/ft
- **Relative Density (Dr)**: 75-85%

#### Layer 4: Stiff to Very Stiff Clay (-25.0 m to -40.0 m)
- **Thickness**: 15.0 m
- **Description**: Stiff to very stiff overconsolidated clay
- **Classification**: CH (High Plasticity Clay)
- **Unit Weight (γ)**: 19.0 kN/m³
- **Effective Unit Weight (γ')**: 9.0 kN/m³
- **Cohesion (c')**: 25 kN/m²
- **Friction Angle (φ')**: 25°
- **Dilation Angle (ψ)**: 0°
- **Young's Modulus (E)**: 100,000 kN/m²
- **Poisson's Ratio (ν)**: 0.30
- **Undrained Shear Strength (su)**: 150-200 kN/m²
- **SPT N-value**: 25-40 blows/ft
- **Overconsolidation Ratio (OCR)**: 2.5-3.0

#### Layer 5: Very Dense Sand/Bedrock (-40.0 m and below)
- **Thickness**: Extends to great depth
- **Description**: Very dense sand transitioning to weathered rock
- **Classification**: SP (Poorly Graded Sand) / Weathered Rock
- **Unit Weight (γ)**: 20.0 kN/m³
- **Effective Unit Weight (γ')**: 10.0 kN/m³
- **Cohesion (c')**: 0 kN/m²
- **Friction Angle (φ')**: 38°
- **Dilation Angle (ψ)**: 8°
- **Young's Modulus (E)**: 150,000 kN/m²
- **Poisson's Ratio (ν)**: 0.20
- **SPT N-value**: >50 blows/ft (refusal)

---

## Structural Loads

### Superstructure Loads

#### Dead Loads
- **Structural Frame**: 8.0 kN/m² per floor
- **Floor Finishes**: 1.5 kN/m² per floor
- **Partitions**: 1.0 kN/m² per floor
- **Mechanical/Electrical**: 0.5 kN/m² per floor
- **Total Dead Load per Floor**: 11.0 kN/m²

#### Live Loads
- **Office Areas**: 3.0 kN/m² per floor
- **Corridors**: 4.0 kN/m² per floor
- **Roof**: 1.5 kN/m² (snow/rain not applicable)

#### Wind Loads
- **Design Wind Speed**: 50 m/s (3-second gust)
- **Wind Pressure**: 1.2 kN/m² (typical for 35-story building)
- **Overturning Moment**: 250,000 kN·m at foundation level

#### Seismic Loads
- **Design Seismic Zone**: Zone 3 (moderate seismicity)
- **Peak Ground Acceleration (PGA)**: 0.15g
- **Response Spectrum**: Type II (medium soil)
- **Base Shear**: 8% of total building weight

### Foundation Load Summary

#### Column Loads (Typical)
- **Corner Columns**: 
  - Axial Load: 8,000 kN (service)
  - Axial Load: 12,000 kN (ultimate)
  - Moment: 500 kN·m
  - Shear: 200 kN

- **Edge Columns**:
  - Axial Load: 12,000 kN (service)
  - Axial Load: 18,000 kN (ultimate)
  - Moment: 800 kN·m
  - Shear: 300 kN

- **Interior Columns**:
  - Axial Load: 15,000 kN (service)
  - Axial Load: 22,500 kN (ultimate)
  - Moment: 1,000 kN·m
  - Shear: 400 kN

- **Core Wall**:
  - Total Axial Load: 80,000 kN (service)
  - Total Axial Load: 120,000 kN (ultimate)
  - Overturning Moment: 150,000 kN·m
  - Base Shear: 5,000 kN

#### Load Combinations (Serviceability Limit State)
- **Combination 1**: Dead + Live
- **Combination 2**: Dead + Live + Wind
- **Combination 3**: Dead + Live + Seismic

#### Load Combinations (Ultimate Limit State)
- **Combination 1**: 1.4 × Dead + 1.6 × Live
- **Combination 2**: 1.2 × Dead + 1.2 × Live + 1.2 × Wind
- **Combination 3**: 1.2 × Dead + 1.0 × Live + 1.0 × Seismic

---

## Barrette Pile Design Requirements

### Preliminary Design Parameters

#### Barrette Dimensions
- **Length (strong direction)**: 3.0 m
- **Width**: 1.5 m
- **Aspect Ratio**: 2:1 (typical for barrettes)
- **Embedment Depth**: To be determined (target: 30-35 m)

#### Barrette Material Properties
- **Concrete Grade**: C40/50 (fck = 40 MPa, fcd = 26.7 MPa)
- **Reinforcement**: High-yield steel (fy = 500 MPa, fyd = 435 MPa)
- **Concrete Unit Weight**: 24 kN/m³
- **Young's Modulus (Ec)**: 35,000 MPa
- **Poisson's Ratio (νc)**: 0.20

#### Barrette Layout
- **Total Number of Barrettes**: 48
- **Arrangement**: 
  - 4 rows × 12 columns
  - Spacing: 6.0 m center-to-center (both directions)
  - Grid pattern: 24 m × 66 m
- **Under Core Wall**: 8 barrettes in 2 rows × 4 columns
- **Under Columns**: 1-2 barrettes per column

### Design Criteria

#### Bearing Capacity
- **Factor of Safety (FOS)**: 2.5 (service loads)
- **Ultimate Capacity**: Must exceed 1.5 × ultimate load
- **End Bearing**: Must be in Layer 4 (stiff clay) or Layer 5 (dense sand)
- **Shaft Resistance**: Consider all layers along embedment

#### Settlement
- **Maximum Total Settlement**: 50 mm
- **Differential Settlement**: 25 mm (between adjacent barrettes)
- **Long-term Settlement**: Consider consolidation of clay layers
- **Immediate Settlement**: < 20 mm

#### Lateral Resistance
- **Lateral Load Capacity**: Must resist wind and seismic loads
- **Lateral Deflection**: < 25 mm at ground level
- **Moment Capacity**: Sufficient for combined axial + bending

#### Structural Design
- **Reinforcement**: Designed for:
  - Axial compression
  - Bending moments (from lateral loads)
  - Shear forces
  - Torsion (if applicable)
- **Crack Control**: Maximum crack width 0.3 mm
- **Durability**: 50-year design life, exposure class XC2

---

## Analysis Requirements

### Plaxis 3D Analysis Tasks

1. **Model Setup**
   - Create 3D model with all soil layers
   - Model barrette piles as embedded beams or volume elements
   - Apply appropriate boundary conditions
   - Set up groundwater conditions

2. **Material Models**
   - **Fill Material**: Mohr-Coulomb (drained)
   - **Soft Clay**: Soft Soil Model or Modified Cam-Clay
   - **Dense Sand**: Hardening Soil Model or Mohr-Coulomb
   - **Stiff Clay**: Hardening Soil Model or Modified Cam-Clay
   - **Very Dense Sand**: Hardening Soil Model
   - **Concrete**: Linear Elastic (or Concrete model if available)

3. **Analysis Phases**
   - **Phase 1**: Initial stress state (K₀ = 0.5-0.6 for normally consolidated, 1.0-1.5 for overconsolidated)
   - **Phase 2**: Construction of barrettes (consider installation effects)
   - **Phase 3**: Application of dead loads
   - **Phase 4**: Application of live loads
   - **Phase 5**: Long-term consolidation (if applicable)
   - **Phase 6**: Wind/seismic loading (if applicable)

4. **Results to Extract**
   - Axial load distribution along barrette length
   - Shaft resistance mobilization
   - End bearing pressure
   - Settlement of each barrette
   - Differential settlement between barrettes
   - Lateral deflection and bending moments
   - Stress distribution in soil
   - Pile-soil interaction forces

5. **Verification Checks**
   - Compare with analytical methods (Terzaghi, FHWA methods)
   - Check against design criteria
   - Verify structural adequacy
   - Assess group effects

---

## Design Codes and Standards

- **Geotechnical Design**: Eurocode 7 (EN 1997-1)
- **Structural Design**: Eurocode 2 (EN 1992-1-1)
- **Seismic Design**: Eurocode 8 (EN 1998-1)
- **Construction**: ICE Specification for Piling and Embedded Retaining Walls
- **Reference**: FHWA GEC-10 (Drilled Shafts)

---

## Deliverables

1. **Plaxis 3D Model File** (.p3d)
2. **Analysis Results Report** including:
   - Load-settlement curves
   - Axial load distribution
   - Settlement contours
   - Stress distributions
   - Deflection profiles
3. **Design Verification**:
   - Bearing capacity calculations
   - Settlement predictions
   - Comparison with code methods
4. **Recommendations**:
   - Final barrette dimensions
   - Required embedment depth
   - Reinforcement requirements
   - Construction considerations

---

## Notes

- This problem is based on a real case study from Ho Chi Minh City, Vietnam
- Soil parameters are representative of Mekong Delta geological conditions
- Loads are typical for a 35-story commercial building (original was 40-story)
- The problem can be simplified or extended based on learning objectives
- All parameters are provided for direct input into Plaxis 3D
- For exact values from the original study, refer to the published paper (link in References)

---

## References

### Primary Case Study
- Nguyen, H.M., Fellenius, B.H., Puppala, A.J., Aravind, P., & Tran, Q.T. (2016). "Bidirectional Tests on Two Shaft-Grouted Barrette Piles in the Mekong Delta, Vietnam." *Geotechnical Engineering Journal of the SEAGS & AGSSEA*, 47(1), 15-25.  
  Available at: https://www.fellenius.net/papers/360%20Bidirectional%20Tests%20on%20Two%20Shaft%20Grouted%20Barrette%20Piles.pdf

### Design Codes and Standards
- Eurocode 7: Geotechnical Design
- FHWA GEC-10: Drilled Shafts
- ICE Specification for Piling
- Pile Foundation Analysis and Design (H. G. Poulos)
- Plaxis 3D Reference Manual

