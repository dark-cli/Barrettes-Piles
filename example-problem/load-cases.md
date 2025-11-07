# Individual Pile Load Cases

This document provides load cases for individual pile analysis in Plaxis 3D.

For column loads and load combinations, see [structural-loads.md](./structural-loads.md).

---

## Load Cases for Single Pile Analysis

### Case 1: Corner Column Pile (Most Common - Single Pile)
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

**Note**: 1 pile per column, so column load = pile load

---

### Case 2: Edge Column Pile (Single Pile Option)
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

**Note**: If 1 pile per column, use above. If 2 piles per column, divide by 2 (see Case 3).

---

### Case 3: Edge/Interior Column Pile (Two Piles per Column)
**Service Loads (per pile):**
- Axial Load (P): **6,000** kN (12,000 ÷ 2) or **7,500** kN (15,000 ÷ 2)
- Moment (Mx): **250** kN·m (500 ÷ 2) or **300** kN·m (600 ÷ 2)
- Moment (My): **150** kN·m (300 ÷ 2) or **200** kN·m (400 ÷ 2)
- Shear (Vx): **100** kN (200 ÷ 2) or **125** kN (250 ÷ 2)
- Shear (Vy): **75** kN (150 ÷ 2) or **100** kN (200 ÷ 2)

**Ultimate Loads (per pile):**
- Axial Load (P): **9,000** kN (18,000 ÷ 2) or **11,250** kN (22,500 ÷ 2)
- Moment (Mx): **375** kN·m (750 ÷ 2) or **450** kN·m (900 ÷ 2)
- Moment (My): **225** kN·m (450 ÷ 2) or **300** kN·m (600 ÷ 2)
- Shear (Vx): **150** kN (300 ÷ 2) or **187.5** kN (375 ÷ 2)
- Shear (Vy): **112.5** kN (225 ÷ 2) or **150** kN (300 ÷ 2)

**Note**: Loads divided equally between two piles (assumes symmetric loading)

---

### Case 4: Core Wall Pile (8-Pile Group)
**Service Loads (average per pile):**
- Axial Load (P): **10,000** kN (80,000 ÷ 8)
- Moment (Mx): **12,500** kN·m (100,000 ÷ 8)
- Moment (My): **6,250** kN·m (50,000 ÷ 8)
- Shear (Vx): **500** kN (4,000 ÷ 8)
- Shear (Vy): **375** kN (3,000 ÷ 8)

**Ultimate Loads (average per pile):**
- Axial Load (P): **15,000** kN (120,000 ÷ 8)
- Moment (Mx): **18,750** kN·m (150,000 ÷ 8)
- Moment (My): **9,375** kN·m (75,000 ÷ 8)
- Shear (Vx): **750** kN (6,000 ÷ 8)
- Shear (Vy): **562.5** kN (4,500 ÷ 8)

**Note**: 
- Average values shown above
- Actual loads vary due to moment distribution (range: 8,000 - 12,000 kN service)
- For group analysis, model all 8 piles with moment distribution

---

## Recommended Load Case for Single Pile Analysis

**Use Case 1 (Corner Column Pile)** for initial analysis:
- **Service Load**: 8,000 kN axial + moments + shear
- **Ultimate Load**: 12,000 kN axial + moments + shear

This represents a typical single pile case and is conservative for design.

---

## Load Application in Plaxis 3D

### Single Pile Analysis (Recommended)

For **individual pile analysis**, apply loads directly at the pile head:

**Example: Corner Column Pile (Service Loads)**
```
Point Load at pile head (z = 0):
  Fz = -8,000 kN        (axial, downward)
  Mx = 300 kN·m         (moment about X-axis)
  My = 200 kN·m         (moment about Y-axis)
  Fx = 150 kN           (shear in X-direction)
  Fy = 100 kN           (shear in Y-direction)
```

**Example: Corner Column Pile (Ultimate Loads)**
```
Point Load at pile head (z = 0):
  Fz = -12,000 kN       (axial, downward)
  Mx = 450 kN·m         (moment about X-axis)
  My = 300 kN·m         (moment about Y-axis)
  Fx = 225 kN           (shear in X-direction)
  Fy = 150 kN           (shear in Y-direction)
```

### Group Analysis (Multiple Piles)

For **pile group analysis** (e.g., 2 piles per column or 8 piles under core wall):
1. Model all piles in the group
2. Apply column loads at pile cap or distribute to pile heads
3. Consider moment distribution for groups with overturning moments

**Example: Two Piles per Column**
```
Pile 1 and Pile 2 (each):
  Fz = -6,000 kN        (12,000 ÷ 2)
  Mx = 250 kN·m         (500 ÷ 2)
  My = 150 kN·m         (300 ÷ 2)
  Fx = 100 kN           (200 ÷ 2)
  Fy = 75 kN            (150 ÷ 2)
```

**Example: Core Wall (8 Piles)**
```
Average per pile:
  Fz = -10,000 kN       (80,000 ÷ 8, average)
  Mx = 12,500 kN·m      (distributed based on position)
  My = 6,250 kN·m       (distributed based on position)
  Fx = 500 kN           (4,000 ÷ 8)
  Fy = 375 kN           (3,000 ÷ 8)
  
Note: Actual loads vary - piles on moment side carry more load
```

---

## Coordinate System

- **X-axis**: East direction
- **Y-axis**: North direction
- **Z-axis**: Up (positive upward)
- **Loads applied at**: Ground level (z = 0 m)

---

## Notes

- All loads are in kN (kilonewtons)
- Moments are in kN·m
- For load combinations (SLS/ULS), see [structural-loads.md](./structural-loads.md)
- Consider load eccentricity for moment application
- Group effects may reduce individual barrette loads

