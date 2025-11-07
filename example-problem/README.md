# Barrette Pile Foundation Design - Example Problem

## Overview

This example problem is based on a **real published case study** from the Mekong Delta, Vietnam (Exim Bank Building, Ho Chi Minh City). The problem provides complete geotechnical and structural data for analysis using Plaxis 3D.

**Reference**: Nguyen, H.M., Fellenius, B.H., Puppala, A.J., Aravind, P., & Tran, Q.T. (2016). "Bidirectional Tests on Two Shaft-Grouted Barrette Piles in the Mekong Delta, Vietnam." *Geotechnical Engineering Journal of the SEAGS & AGSSEA*, 47(1), 15-25.

For details about what's real vs. simplified, see [case-study-source.md](./case-study-source.md).

---

## Quick Start

1. **Problem Statement**: See [Project Description](#project-description) below
2. **Geotechnical Data**: See [geotechnical-data.md](./geotechnical-data.md) for all soil parameters
3. **Load Cases**: See [load-cases.md](./load-cases.md) for individual pile loads (Plaxis 3D ready)
4. **Structural Loads**: See [structural-loads.md](./structural-loads.md) for column loads and combinations
5. **Case Study Source**: See [case-study-source.md](./case-study-source.md) for original paper reference

---

## Project Description

### Building Information
- **Project**: Downtown Commercial Tower (based on Exim Bank Building, Ho Chi Minh City)
- **Location**: Mekong Delta, Vietnam
- **Building Type**: 35-story commercial office tower
- **Foundation Type**: Barrette pile foundation system

### Site Conditions
- **Ground Level**: +0.0 m (reference elevation)
- **Groundwater Table**: -2.0 m below ground level
- **Site Area**: 50 m × 50 m
- **Construction Method**: Slurry wall technique

### Soil Profile Summary
1. **Fill Material** (0.0 to -3.0 m): Silty sand, SM
2. **Soft to Medium Clay** (-3.0 to -12.0 m): Normally consolidated, CL
3. **Dense Sand** (-12.0 to -25.0 m): SP-SM
4. **Stiff to Very Stiff Clay** (-25.0 to -40.0 m): Overconsolidated, CH
5. **Very Dense Sand/Bedrock** (-40.0 m+): SP/Rock

**Complete soil parameters**: See [geotechnical-data.md](./geotechnical-data.md)

### Barrette Pile Design
- **Dimensions**: 3.0 m × 1.5 m (length × width)
- **Embedment Depth**: To be determined (target: 30-35 m)
- **Total Number**: 48 barrettes
- **Spacing**: 6.0 m center-to-center
- **Concrete Grade**: C40/50

### Structural Loads Summary
- **Corner Columns**: 8,000 kN (service), 12,000 kN (ultimate)
- **Edge Columns**: 12,000 kN (service), 18,000 kN (ultimate)
- **Interior Columns**: 15,000 kN (service), 22,500 kN (ultimate)
- **Core Wall**: 80,000 kN (service), 120,000 kN (ultimate)

**Individual pile loads**: See [load-cases.md](./load-cases.md)  
**Column loads and combinations**: See [structural-loads.md](./structural-loads.md)

### Design Criteria
- **Bearing Capacity**: FOS = 2.5 (service loads)
- **Maximum Settlement**: 50 mm total, 25 mm differential
- **Lateral Deflection**: < 25 mm at ground level

---

## Analysis Objectives

Using Plaxis 3D, analyze and verify:
1. **Bearing Capacity**: Ultimate capacity and factor of safety
2. **Settlement**: Immediate and long-term (consolidation)
3. **Lateral Resistance**: Deflection and moment capacity
4. **Structural Adequacy**: Reinforcement requirements

---

## Files in This Folder

- **README.md** (this file): Problem overview and quick start
- **geotechnical-data.md**: Complete soil parameters for Plaxis 3D input
- **load-cases.md**: Individual pile load cases ready for Plaxis 3D
- **structural-loads.md**: Column loads and load combinations
- **case-study-source.md**: Original paper reference and adaptation notes

---

## Notes

- All parameters are provided for direct input into Plaxis 3D
- Soil parameters are representative of Mekong Delta conditions
- For exact values from the original study, refer to the published paper
- The problem can be simplified or extended based on learning objectives

