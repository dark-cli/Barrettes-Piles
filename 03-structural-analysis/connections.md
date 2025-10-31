# Connections

## Overview

Barrettes connect to superstructure elements (columns, walls, pile caps) and must transfer axial loads, moments, and shear forces. Connection design is critical for overall structural performance.

## Connection Types

### Pile Cap Connections

#### Embedment

Barrettes are typically embedded into pile caps:
- Minimum embedment: Typically 150 to 300 mm
- Transfer of loads through bearing and bond
- Additional reinforcement for moment transfer

#### Dowel Bars

Dowel bars connect barrette to pile cap:
- Typically 20 to 32 mm diameter
- Embedded in both barrette and cap
- Designed for tension and shear

### Direct Column Connections

#### Column-to-Barrette

Direct connection where column aligns with barrette:
- Alignment of reinforcement
- Continuity of load path
- Moment transfer considerations

### Wall Connections

#### Embedded Wall-to-Barrette

For barrettes supporting walls:
- Continuity of reinforcement
- Load distribution
- Crack control

## Load Transfer Mechanisms

### Axial Load Transfer

$$P_{transfer} = P_{bearing} + P_{dowels}$$

Where:
- $P_{bearing}$ = bearing capacity at interface
- $P_{dowels}$ = dowel bar capacity

### Bearing Capacity

$$P_{bearing} = \phi \times 0.85f_c' \times A_{bearing}$$

Where $A_{bearing}$ is the bearing area.

### Moment Transfer

Moments transfer through:
- Direct moment connection
- Eccentric loading
- Reinforcement continuity

### Shear Transfer

Shear transfer mechanisms:
- Interface shear friction
- Dowel action
- Shear keys or roughness

## Design Requirements

### Axial Load

Connection must resist:
$$P_{u,connection} \geq P_{u,barrette}$$

### Bending Moment

$$M_{u,connection} \geq M_{u,barrette}$$

### Shear Force

$$V_{u,connection} \geq V_{u,barrette}$$

## Reinforcement Details

### Dowel Bars

#### Tension Capacity

$$T_{dowel} = A_s f_y$$

#### Development Length

$$L_d = \frac{\phi f_y}{4f_{bd}}$$

#### Embedment Length

In pile cap:
$$L_{embed} \geq L_d$$

In barrette:
$$L_{embed} \geq L_d$$

### Additional Reinforcement

For moment transfer, additional reinforcement may be required:
- Extended longitudinal bars
- Additional dowels
- Shear reinforcement

## Interface Design

### Shear Friction

$$V_n = \mu A_{vf} f_y$$

Where:
- $\mu$ = friction coefficient (typically 1.0 to 1.4)
- $A_{vf}$ = area of reinforcement crossing interface (m²)

### Combined Actions

For combined shear and tension:
$$\left(\frac{V_u}{\phi V_n}\right)^2 + \left(\frac{T_u}{\phi T_n}\right)^2 \leq 1$$

## Constructibility

### Tolerances

- Position tolerance: ±25 to ±50 mm
- Verticality: Per code requirements
- Alignment: Critical for direct connections

### Construction Sequence

1. Construct barrettes
2. Prepare connection interface
3. Install connection reinforcement
4. Cast connecting element (cap, column, wall)

## Special Considerations

### Corrosion Protection

- Adequate cover at connections
- Protection of exposed reinforcement
- Durable concrete at interface

### Durability

- Proper joint detailing
- Waterproofing if required
- Protection against aggressive environments

## References

- ACI Committee 318 (2019). *Building Code Requirements for Structural Concrete (ACI 318-19)*.
- ACI Committee 315 (2018). *Details and Detailing of Concrete Reinforcement (ACI 315-18)*.
- EN 1992-1-1 (2004). *Eurocode 2: Design of concrete structures - Part 1-1: General rules and rules for buildings*.

