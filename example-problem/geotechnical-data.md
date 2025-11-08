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

| Parameter | Value | Notes |
|-----------|-------|-------|
| **General Parameters** |
| Material Model | Mohr-Coulomb (Drained) | - |
| γ_bulk (kN/m³) | 17.5 | - |
| k (m/s) | 1.0 × 10⁻⁵ | - |
| **Strength Parameters** |
| c' (kN/m²) | 5 | - |
| φ' (°) | 28 | - |
| ψ (°) | 0 | - |
| **Stiffness Parameters** |
| E (kN/m²) | 15,000 | - |
| ν | 0.30 | - |
| E₅₀ (kN/m²) | 15,000 | Hardening Soil |
| Eᵤᵣ (kN/m²) | 45,000 | Hardening Soil |
| Eᵒᵈ (kN/m²) | 15,000 | Hardening Soil |
| **Advanced Parameters (Hardening Soil)** |
| m | 0.5 | Power |
| K₀ⁿᶜ | 0.577 | 1 - sin φ' |
| Rf | 0.9 | - |
| **Undrained Parameters** |
| su (kN/m²) | 25 | - |
| Eu (kN/m²) | 750 | Eu ≈ 30 × su |

---

### Layer 2: Soft to Medium Clay (CL)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **General Parameters** |
| Material Model | Soft Soil Model or Modified Cam-Clay | Recommended |
| γ_bulk (kN/m³) | 18.0 | - |
| kᵥ (m/s) | 1.0 × 10⁻⁸ | Vertical |
| kₕ (m/s) | 5.0 × 10⁻⁹ | Horizontal |
| **Strength Parameters** |
| c' (kN/m²) | 10 | - |
| φ' (°) | 22 | - |
| ψ (°) | 0 | - |
| **Stiffness Parameters** |
| E (kN/m²) | 25,000 | - |
| ν | 0.35 | - |
| E₅₀ (kN/m²) | 25,000 | Hardening Soil |
| Eᵤᵣ (kN/m²) | 75,000 | Hardening Soil |
| Eᵒᵈ (kN/m²) | 25,000 | Hardening Soil |
| **Consolidation Parameters (Soft Soil Model)** |
| λ* | 0.15 | λ* = Cc / (2.3 × (1 + e₀)) |
| κ* | 0.02 | κ* = Cr / (2.3 × (1 + e₀)) |
| e₀ | 0.85 | Initial void ratio |
| σ'p (kN/m²) | 50 | Preconsolidation pressure, normally consolidated |
| cv (m²/s) | 2.5 × 10⁻⁷ | - |
| **Undrained Parameters** |
| su (kN/m²) at -3 m | 30 | Varies with depth |
| su (kN/m²) at -12 m | 50 | Linear interpolation |
| Eu (kN/m²) at top | 1,500 | - |
| Eu (kN/m²) at bottom | 2,500 | - |
| **Advanced Parameters** |
| K₀ⁿᶜ | 0.625 | 1 - sin φ' |
| OCR | 1.0 | Normally consolidated |

---

### Layer 3: Dense Sand (SP-SM)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **General Parameters** |
| Material Model | Hardening Soil Model or Mohr-Coulomb | Hardening Soil recommended |
| γ_bulk (kN/m³) | 19.5 | - |
| k (m/s) | 1.0 × 10⁻⁴ | - |
| **Strength Parameters** |
| c' (kN/m²) | 0 | - |
| φ' (°) | 35 | - |
| ψ (°) | 5 | - |
| **Stiffness Parameters** |
| E (kN/m²) | 80,000 | - |
| ν | 0.25 | - |
| E₅₀ (kN/m²) | 80,000 | Hardening Soil |
| Eᵤᵣ (kN/m²) | 240,000 | Hardening Soil |
| Eᵒᵈ (kN/m²) | 80,000 | Hardening Soil |
| **Advanced Parameters (Hardening Soil)** |
| m | 0.5 | Power |
| K₀ⁿᶜ | 0.426 | 1 - sin φ' |
| Rf | 0.9 | - |
| pref (kN/m²) | 100 | Reference pressure |
| **SPT Correlation** |
| SPT N-value (blows/ft) | 35-50 | - |
| Relative Density (%) | 75-85 | - |

---

### Layer 4: Stiff to Very Stiff Clay (CH)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **General Parameters** |
| Material Model | Hardening Soil Model or Modified Cam-Clay | - |
| γ_bulk (kN/m³) | 19.0 | - |
| kᵥ (m/s) | 1.0 × 10⁻⁹ | Vertical |
| kₕ (m/s) | 5.0 × 10⁻¹⁰ | Horizontal |
| **Strength Parameters** |
| c' (kN/m²) | 25 | - |
| φ' (°) | 25 | - |
| ψ (°) | 0 | - |
| **Stiffness Parameters** |
| E (kN/m²) | 100,000 | - |
| ν | 0.30 | - |
| E₅₀ (kN/m²) | 100,000 | Hardening Soil |
| Eᵤᵣ (kN/m²) | 300,000 | Hardening Soil |
| Eᵒᵈ (kN/m²) | 100,000 | Hardening Soil |
| **Consolidation Parameters (Soft Soil Model)** |
| λ* | 0.10 | - |
| κ* | 0.015 | - |
| e₀ | 0.60 | Initial void ratio |
| σ'p (kN/m²) | 200 | Preconsolidation pressure |
| cv (m²/s) | 1.0 × 10⁻⁸ | - |
| **Undrained Parameters** |
| su (kN/m²) at -25 m | 150 | Varies with depth |
| su (kN/m²) at -40 m | 200 | Linear interpolation |
| Eu (kN/m²) at top | 7,500 | - |
| Eu (kN/m²) at bottom | 10,000 | - |
| **Advanced Parameters** |
| K₀ⁿᶜ | 0.577 | 1 - sin φ' |
| OCR | 2.5-3.0 | Overconsolidated (use average 2.75) |

---

### Layer 5: Very Dense Sand/Bedrock (SP/Rock)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **General Parameters** |
| Material Model | Hardening Soil Model or Mohr-Coulomb | - |
| γ_bulk (kN/m³) | 20.0 | - |
| k (m/s) | 1.0 × 10⁻³ | - |
| **Strength Parameters** |
| c' (kN/m²) | 0 | - |
| φ' (°) | 38 | - |
| ψ (°) | 8 | - |
| **Stiffness Parameters** |
| E (kN/m²) | 150,000 | - |
| ν | 0.20 | - |
| E₅₀ (kN/m²) | 150,000 | Hardening Soil |
| Eᵤᵣ (kN/m²) | 450,000 | Hardening Soil |
| Eᵒᵈ (kN/m²) | 150,000 | Hardening Soil |
| **Advanced Parameters (Hardening Soil)** |
| m | 0.5 | Power |
| K₀ⁿᶜ | 0.384 | 1 - sin φ' |
| Rf | 0.9 | - |
| pref (kN/m²) | 100 | Reference pressure |
| **SPT Correlation** |
| SPT N-value (blows/ft) | >50 | Refusal |

---

## Groundwater Conditions

| Parameter | Value | Notes |
|-----------|-------|-------|
| Groundwater Table (m) | -2.0 | Below ground level |
| γw (kN/m³) | 9.81 | Unit weight of water |
| Hydrostatic Pressure | Linear | From water table |

---

## Initial Stress State

### At-Rest Earth Pressure Coefficient (K₀)

| Layer | Description | K₀ | Calculation | Notes |
|-------|-------------|-----|-------------|-------|
| 1 | Fill | 0.577 | 1 - sin φ' = 1 - sin 28° | - |
| 2 | Soft Clay (NC) | 0.625 | 1 - sin φ' = 1 - sin 22° | Normally consolidated |
| 3 | Dense Sand | 0.426 | 1 - sin φ' = 1 - sin 35° | - |
| 4 | Stiff Clay (OC) | 0.95 | K₀ⁿᶜ × √OCR = 0.577 × √2.5 to √3.0 | Average (range: 0.866-1.039) |
| 5 | Very Dense Sand | 0.384 | 1 - sin φ' = 1 - sin 38° | - |

---

## Barrette Material Properties

### Concrete (C40/50)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Material Model | Linear Elastic | Or Concrete model if available |
| γ_bulk (kN/m³) | 24.0 | - |
| E (kN/m²) | 35,000,000 | 35 GPa |
| ν | 0.20 | - |
| fck (kN/m²) | 40,000 | 40 MPa |
| fctk (kN/m²) | 2,500 | 2.5 MPa |
| α (/°C) | 10 × 10⁻⁶ | Thermal expansion coefficient |

### Reinforcement (High-Yield Steel)

| Parameter | Value | Notes |
|-----------|-------|-------|
| fy (kN/m²) | 500,000 | 500 MPa |
| fyd (kN/m²) | 435,000 | 435 MPa |
| Es (kN/m²) | 200,000,000 | 200 GPa |
| γ_bulk (kN/m³) | 78.5 | - |

---

## Interface Properties (Pile-Soil)

### Interface Reduction Factors (Rinter)

| Layer | Description | Rinter | Notes |
|-------|-------------|--------|-------|
| 1 | Fill | 0.70 | Typical for fill |
| 2 | Soft Clay | 0.60 | Typical for soft clay |
| 3 | Dense Sand | 0.80 | Typical for dense sand |
| 4 | Stiff Clay | 0.70 | Typical for stiff clay |
| 5 | Very Dense Sand | 0.85 | Typical for very dense sand/rock |

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
