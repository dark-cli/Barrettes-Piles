# Structural Loads Summary

This document provides detailed load information for the barrette pile foundation design.

## Load Summary Table

| Load Type | Service Load (kN) | Ultimate Load (kN) | Notes |
|-----------|-------------------|-------------------|-------|
| **Corner Column** | 8,000 | 12,000 | Single barrette |
| **Edge Column** | 12,000 | 18,000 | 1-2 barrettes |
| **Interior Column** | 15,000 | 22,500 | 1-2 barrettes |
| **Core Wall (Total)** | 80,000 | 120,000 | 8 barrettes |

## Detailed Column Loads

### Corner Columns (16 columns)

**Service Loads:**
- Axial Load (P): **8,000** kN
- Moment (Mx): **300** kN·m
- Moment (My): **200** kN·m
- Shear (Vx): **150** kN
- Shear (Vy): **100** kN

**Ultimate Loads:**
- Axial Load (P): **12,000** kN
- Moment (Mx): **450** kN·m
- Moment (My): **300** kN·m
- Shear (Vx): **225** kN
- Shear (Vy): **150** kN

**Barrette Assignment:**
- 1 barrette per column
- Barrette dimensions: 3.0 m × 1.5 m
- Location: Building corners

---

### Edge Columns (20 columns)

**Service Loads:**
- Axial Load (P): **12,000** kN
- Moment (Mx): **500** kN·m
- Moment (My): **300** kN·m
- Shear (Vx): **200** kN
- Shear (Vy): **150** kN

**Ultimate Loads:**
- Axial Load (P): **18,000** kN
- Moment (Mx): **750** kN·m
- Moment (My): **450** kN·m
- Shear (Vx): **300** kN
- Shear (Vy): **225** kN

**Barrette Assignment:**
- 1-2 barrettes per column (depending on load)
- Barrette dimensions: 3.0 m × 1.5 m
- Location: Building perimeter (non-corner)

---

### Interior Columns (12 columns)

**Service Loads:**
- Axial Load (P): **15,000** kN
- Moment (Mx): **600** kN·m
- Moment (My): **400** kN·m
- Shear (Vx): **250** kN
- Shear (Vy): **200** kN

**Ultimate Loads:**
- Axial Load (P): **22,500** kN
- Moment (Mx): **900** kN·m
- Moment (My): **600** kN·m
- Shear (Vx): **375** kN
- Shear (Vy): **300** kN

**Barrette Assignment:**
- 1-2 barrettes per column
- Barrette dimensions: 3.0 m × 1.5 m
- Location: Building interior

---

### Core Wall

**Service Loads:**
- Total Axial Load (P): **80,000** kN
- Overturning Moment (Mx): **100,000** kN·m
- Overturning Moment (My): **50,000** kN·m
- Base Shear (Vx): **4,000** kN
- Base Shear (Vy): **3,000** kN

**Ultimate Loads:**
- Total Axial Load (P): **120,000** kN
- Overturning Moment (Mx): **150,000** kN·m
- Overturning Moment (My): **75,000** kN·m
- Base Shear (Vx): **6,000** kN
- Base Shear (Vy): **4,500** kN

**Barrette Assignment:**
- 8 barrettes in 2 rows × 4 columns
- Barrette dimensions: 3.0 m × 1.5 m
- Spacing: 6.0 m center-to-center
- Location: Building center (core)

**Load Distribution per Barrette (Service):**
- Average Axial Load: **10,000** kN per barrette
- Range: **8,000 - 12,000** kN (due to moment distribution)

---

## Load Combinations

### Serviceability Limit State (SLS)

**Combination 1: Permanent + Variable**
- Load Factor (Dead): **1.0**
- Load Factor (Live): **1.0**
- Use for: Settlement analysis, serviceability checks

**Combination 2: Permanent + Variable + Wind**
- Load Factor (Dead): **1.0**
- Load Factor (Live): **1.0**
- Load Factor (Wind): **1.0**
- Use for: Wind loading analysis

**Combination 3: Permanent + Variable + Seismic**
- Load Factor (Dead): **1.0**
- Load Factor (Live): **0.3** (reduced live load for seismic)
- Load Factor (Seismic): **1.0**
- Use for: Seismic loading analysis

---

### Ultimate Limit State (ULS)

**Combination 1: Permanent + Variable**
- Load Factor (Dead): **1.4**
- Load Factor (Live): **1.6**
- Use for: Bearing capacity, structural design

**Combination 2: Permanent + Variable + Wind**
- Load Factor (Dead): **1.2**
- Load Factor (Live): **1.2**
- Load Factor (Wind): **1.2**
- Use for: Combined loading with wind

**Combination 3: Permanent + Variable + Seismic**
- Load Factor (Dead): **1.2**
- Load Factor (Live): **1.0**
- Load Factor (Seismic): **1.0**
- Use for: Seismic design

---

## Load Application in Plaxis 3D

### Point Loads (Columns)

For each column location:
1. Create point load at barrette top
2. Apply axial load (P) in vertical direction (negative Z)
3. Apply moments (Mx, My) as concentrated moments
4. Apply shear forces (Vx, Vy) as horizontal point loads

**Typical Corner Column (Service):**
```
Point Load at (x, y, z = 0):
  Fz = -8,000 kN
  Mx = 300 kN·m
  My = 200 kN·m
  Fx = 150 kN
  Fy = 100 kN
```

### Distributed Loads (Core Wall)

For core wall:
1. Create distributed load over barrette group area
2. Apply total axial load distributed over 8 barrettes
3. Apply overturning moment as linearly varying pressure
4. Apply base shear as horizontal distributed load

**Core Wall (Service):**
```
Distributed Load Area: 12 m × 6 m (2 rows × 4 columns)
  Average Pressure: 80,000 / (12 × 6) = 1,111 kN/m²
  Moment creates pressure variation: ±500 kN/m²
  Horizontal Load: 4,000 kN (in X direction)
```

---

## Load Phases for Analysis

### Phase 1: Initial Stress
- No applied loads
- Establish initial geostatic stress

### Phase 2: Barrette Construction
- No applied loads
- Consider installation effects (if modeling)

### Phase 3: Dead Loads
- Apply 100% of dead loads
- All columns and core wall

### Phase 4: Live Loads
- Apply 100% of live loads
- All columns and core wall

### Phase 5: Long-term Consolidation
- Maintain all loads
- Allow consolidation of clay layers
- Duration: 10-50 years (depending on analysis)

### Phase 6: Wind Loading
- Maintain dead + live loads
- Add wind loads
- Consider dynamic effects if applicable

### Phase 7: Seismic Loading
- Maintain dead + reduced live loads
- Add seismic loads
- Consider time-history or response spectrum

---

## Load-Settlement Analysis

For each barrette, analyze:
1. **Load-Settlement Curve**: Apply increasing loads and record settlement
2. **Ultimate Capacity**: Load at which settlement becomes excessive
3. **Working Load Settlement**: Settlement at service load
4. **Group Effects**: Settlement of barrette group vs. single barrette

**Typical Load Steps:**
- 0 kN (initial)
- 2,000 kN
- 4,000 kN
- 6,000 kN
- 8,000 kN (service)
- 10,000 kN
- 12,000 kN (ultimate)
- 15,000 kN
- 18,000 kN
- 20,000 kN (failure)

---

## Lateral Load Analysis

### Wind Loads

**Design Wind Speed**: 50 m/s (3-second gust)

**Wind Pressure Distribution:**
- Base: 1.0 kN/m²
- Top: 1.5 kN/m²
- Linear variation with height

**Total Wind Force**: 8,000 kN
**Overturning Moment at Foundation**: 250,000 kN·m

### Seismic Loads

**Design Parameters:**
- Peak Ground Acceleration (PGA): **0.15g**
- Response Spectrum: Type II (medium soil)
- Importance Factor: **1.0**
- Behavior Factor: **3.0**

**Base Shear**: 8% of total building weight
- Total Building Weight: ~100,000 kN
- Base Shear: **8,000** kN

**Overturning Moment**: Base shear × 0.67 × building height
- Building Height: 120 m
- Overturning Moment: **640,000** kN·m

---

## Notes

- All loads are in kN (kilonewtons)
- Moments are in kN·m
- Coordinate system: X = East, Y = North, Z = Up (positive upward)
- Loads are applied at ground level (z = 0 m)
- Consider load eccentricity for moment application
- Group effects may reduce individual barrette loads
- Dynamic amplification factors may apply for seismic loads

