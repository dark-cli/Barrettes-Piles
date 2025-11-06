# Geotechnical Data Summary

This document provides a tabulated summary of all geotechnical parameters for direct input into Plaxis 3D.

## Soil Layer Summary

| Layer | Depth (m) | Thickness (m) | Description | Classification |
|-------|-----------|---------------|-------------|----------------|
| 1 | 0.0 to -3.0 | 3.0 | Fill Material | SM |
| 2 | -3.0 to -12.0 | 9.0 | Soft to Medium Clay | CL |
| 3 | -12.0 to -25.0 | 13.0 | Dense Sand | SP-SM |
| 4 | -25.0 to -40.0 | 15.0 | Stiff to Very Stiff Clay | CH |
| 5 | -40.0+ | - | Very Dense Sand/Bedrock | SP/Rock |

## Material Parameters for Plaxis 3D

### Layer 1: Fill Material (SM)

**General Parameters:**
- Material Model: **Mohr-Coulomb** (Drained)
- Unit Weight (γ): **17.5** kN/m³
- Unit Weight (γ') below water table: **7.5** kN/m³
- Permeability (k): **1.0 × 10⁻⁵** m/s

**Strength Parameters:**
- Cohesion (c'): **5** kN/m²
- Friction Angle (φ'): **28** °
- Dilation Angle (ψ): **0** °

**Stiffness Parameters:**
- Young's Modulus (E): **15,000** kN/m²
- Poisson's Ratio (ν): **0.30**
- E₅₀ (for Hardening Soil): **15,000** kN/m²
- Eᵤᵣ (for Hardening Soil): **45,000** kN/m²
- Eᵒᵈ (for Hardening Soil): **15,000** kN/m²

**Advanced Parameters (if using Hardening Soil Model):**
- m (power): **0.5**
- K₀ⁿᶜ: **0.577** (1 - sin φ')
- Rf: **0.9**

**Undrained Parameters:**
- Undrained Shear Strength (su): **25** kN/m²
- Undrained Young's Modulus (Eu): **750** kN/m² (Eu ≈ 30 × su)

---

### Layer 2: Soft to Medium Clay (CL)

**General Parameters:**
- Material Model: **Soft Soil Model** or **Modified Cam-Clay** (recommended)
- Unit Weight (γ): **18.0** kN/m³
- Unit Weight (γ') below water table: **8.0** kN/m³
- Permeability (k): **1.0 × 10⁻⁸** m/s (vertical), **5.0 × 10⁻⁹** m/s (horizontal)

**Strength Parameters:**
- Cohesion (c'): **10** kN/m²
- Friction Angle (φ'): **22** °
- Dilation Angle (ψ): **0** °

**Stiffness Parameters:**
- Young's Modulus (E): **25,000** kN/m²
- Poisson's Ratio (ν): **0.35**
- E₅₀ (for Hardening Soil): **25,000** kN/m²
- Eᵤᵣ (for Hardening Soil): **75,000** kN/m²
- Eᵒᵈ (for Hardening Soil): **25,000** kN/m²

**Consolidation Parameters (for Soft Soil Model):**
- Compression Index (λ*): **0.15** (λ* = Cc / (2.3 × (1 + e₀)))
- Swelling Index (κ*): **0.02** (κ* = Cr / (2.3 × (1 + e₀)))
- Initial Void Ratio (e₀): **0.85**
- Preconsolidation Pressure (σ'p): **50** kN/m² (normally consolidated)
- Coefficient of Consolidation (cv): **2.5 × 10⁻⁷** m²/s

**Undrained Parameters:**
- Undrained Shear Strength (su): **30-50** kN/m² (varies with depth)
  - At -3 m: **30** kN/m²
  - At -12 m: **50** kN/m²
  - Linear interpolation between
- Undrained Young's Modulus (Eu): **1,500** kN/m² (at top) to **2,500** kN/m² (at bottom)

**Advanced Parameters:**
- K₀ⁿᶜ: **0.625** (1 - sin φ')
- OCR: **1.0** (normally consolidated)

---

### Layer 3: Dense Sand (SP-SM)

**General Parameters:**
- Material Model: **Hardening Soil Model** (recommended) or **Mohr-Coulomb**
- Unit Weight (γ): **19.5** kN/m³
- Unit Weight (γ') below water table: **9.5** kN/m³
- Permeability (k): **1.0 × 10⁻⁴** m/s

**Strength Parameters:**
- Cohesion (c'): **0** kN/m²
- Friction Angle (φ'): **35** °
- Dilation Angle (ψ): **5** °

**Stiffness Parameters:**
- Young's Modulus (E): **80,000** kN/m²
- Poisson's Ratio (ν): **0.25**
- E₅₀ (for Hardening Soil): **80,000** kN/m²
- Eᵤᵣ (for Hardening Soil): **240,000** kN/m²
- Eᵒᵈ (for Hardening Soil): **80,000** kN/m²

**Advanced Parameters (for Hardening Soil Model):**
- m (power): **0.5**
- K₀ⁿᶜ: **0.426** (1 - sin φ')
- Rf: **0.9**
- Reference Pressure (pref): **100** kN/m²

**SPT Correlation:**
- SPT N-value: **35-50** blows/ft
- Relative Density: **75-85%**

---

### Layer 4: Stiff to Very Stiff Clay (CH)

**General Parameters:**
- Material Model: **Hardening Soil Model** or **Modified Cam-Clay**
- Unit Weight (γ): **19.0** kN/m³
- Unit Weight (γ') below water table: **9.0** kN/m³
- Permeability (k): **1.0 × 10⁻⁹** m/s (vertical), **5.0 × 10⁻¹⁰** m/s (horizontal)

**Strength Parameters:**
- Cohesion (c'): **25** kN/m²
- Friction Angle (φ'): **25** °
- Dilation Angle (ψ): **0** °

**Stiffness Parameters:**
- Young's Modulus (E): **100,000** kN/m²
- Poisson's Ratio (ν): **0.30**
- E₅₀ (for Hardening Soil): **100,000** kN/m²
- Eᵤᵣ (for Hardening Soil): **300,000** kN/m²
- Eᵒᵈ (for Hardening Soil): **100,000** kN/m²

**Consolidation Parameters (if using Soft Soil Model):**
- Compression Index (λ*): **0.10**
- Swelling Index (κ*): **0.015**
- Initial Void Ratio (e₀): **0.60**
- Preconsolidation Pressure (σ'p): **200** kN/m²
- Coefficient of Consolidation (cv): **1.0 × 10⁻⁸** m²/s

**Undrained Parameters:**
- Undrained Shear Strength (su): **150-200** kN/m² (varies with depth)
  - At -25 m: **150** kN/m²
  - At -40 m: **200** kN/m²
  - Linear interpolation between
- Undrained Young's Modulus (Eu): **7,500** kN/m² (at top) to **10,000** kN/m² (at bottom)

**Advanced Parameters:**
- K₀ⁿᶜ: **0.577** (1 - sin φ')
- OCR: **2.5-3.0** (overconsolidated)

---

### Layer 5: Very Dense Sand/Bedrock (SP/Rock)

**General Parameters:**
- Material Model: **Hardening Soil Model** or **Mohr-Coulomb**
- Unit Weight (γ): **20.0** kN/m³
- Unit Weight (γ') below water table: **10.0** kN/m³
- Permeability (k): **1.0 × 10⁻³** m/s

**Strength Parameters:**
- Cohesion (c'): **0** kN/m²
- Friction Angle (φ'): **38** °
- Dilation Angle (ψ): **8** °

**Stiffness Parameters:**
- Young's Modulus (E): **150,000** kN/m²
- Poisson's Ratio (ν): **0.20**
- E₅₀ (for Hardening Soil): **150,000** kN/m²
- Eᵤᵣ (for Hardening Soil): **450,000** kN/m²
- Eᵒᵈ (for Hardening Soil): **150,000** kN/m²

**Advanced Parameters (for Hardening Soil Model):**
- m (power): **0.5**
- K₀ⁿᶜ: **0.384** (1 - sin φ')
- Rf: **0.9**
- Reference Pressure (pref): **100** kN/m²

**SPT Correlation:**
- SPT N-value: **>50** blows/ft (refusal)

---

## Groundwater Conditions

- **Groundwater Table**: **-2.0 m** below ground level
- **Unit Weight of Water**: **9.81** kN/m³
- **Hydrostatic Pressure Distribution**: Linear from water table

---

## Initial Stress State

### At-Rest Earth Pressure Coefficient (K₀)

- **Layer 1 (Fill)**: K₀ = **0.577** (1 - sin φ' = 1 - sin 28°)
- **Layer 2 (Soft Clay, NC)**: K₀ = **0.625** (1 - sin φ' = 1 - sin 22°)
- **Layer 3 (Dense Sand)**: K₀ = **0.426** (1 - sin φ' = 1 - sin 35°)
- **Layer 4 (Stiff Clay, OC)**: K₀ = **0.866-1.039** (K₀ⁿᶜ × √OCR = 0.577 × √2.5 to √3.0)
  - Use **0.95** as average
- **Layer 5 (Very Dense Sand)**: K₀ = **0.384** (1 - sin φ' = 1 - sin 38°)

---

## Barrette Material Properties

### Concrete (C40/50)

- **Material Model**: **Linear Elastic** (or Concrete model if available)
- **Unit Weight (γ)**: **24.0** kN/m³
- **Young's Modulus (E)**: **35,000,000** kN/m² (35 GPa)
- **Poisson's Ratio (ν)**: **0.20**
- **Compressive Strength (fck)**: **40,000** kN/m² (40 MPa)
- **Tensile Strength (fctk)**: **2,500** kN/m² (2.5 MPa)
- **Thermal Expansion Coefficient**: **10 × 10⁻⁶** /°C

### Reinforcement (High-Yield Steel)

- **Yield Strength (fy)**: **500,000** kN/m² (500 MPa)
- **Design Yield Strength (fyd)**: **435,000** kN/m² (435 MPa)
- **Young's Modulus (Es)**: **200,000,000** kN/m² (200 GPa)
- **Unit Weight**: **78.5** kN/m³

---

## Interface Properties (Pile-Soil)

### Interface Reduction Factors (Rinter)

- **Layer 1 (Fill)**: **0.70** (typical for fill)
- **Layer 2 (Soft Clay)**: **0.60** (typical for soft clay)
- **Layer 3 (Dense Sand)**: **0.80** (typical for dense sand)
- **Layer 4 (Stiff Clay)**: **0.70** (typical for stiff clay)
- **Layer 5 (Very Dense Sand)**: **0.85** (typical for very dense sand/rock)

**Note**: Rinter = 1.0 means full friction, Rinter < 1.0 reduces interface strength

---

## Plaxis 3D Input Checklist

- [ ] Create soil layers with correct depths
- [ ] Assign material models to each layer
- [ ] Input all strength parameters (c', φ', ψ)
- [ ] Input all stiffness parameters (E, ν, or E₅₀, Eᵤᵣ, Eᵒᵈ)
- [ ] Set permeability values
- [ ] Define groundwater table at -2.0 m
- [ ] Set initial stress state (K₀ values)
- [ ] Create barrette geometry (3.0 m × 1.5 m)
- [ ] Assign concrete material properties
- [ ] Set interface properties (Rinter values)
- [ ] Define boundary conditions
- [ ] Set up analysis phases

---

## Notes

- All parameters are in SI units (kN, m, s)
- Use drained parameters for long-term analysis
- Use undrained parameters for short-term analysis
- Consider using Hardening Soil Model for better accuracy
- Soft Soil Model recommended for Layer 2 (soft clay)
- Interface properties may need calibration based on construction method

