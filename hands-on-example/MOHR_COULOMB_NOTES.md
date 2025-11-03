# Mohr-Coulomb Material Model Notes

## Current Status

**Mohr-Coulomb is ENABLED** in the code, but **CalculiX crashes** during execution.

The syntax is correct, but CalculiX 2.22 experiences segmentation faults when solving the non-linear system with Mohr-Coulomb plasticity.

## Why Mohr-Coulomb Is Not Working

CalculiX 2.22 crashes (segmentation fault) when Mohr-Coulomb plasticity is enabled, even with correct syntax and conservative parameters. The crash occurs during the Newton-Raphson iterative procedure for non-linear analysis.

### Symptoms Observed:
- CalculiX detected loads correctly (88 distributed facial loads)
- Analysis starts successfully
- "Nonlinear material laws are taken into account" message appears
- "Newton-Raphson iterative procedure is active" message appears
- Then crashes (core dump) before first iteration completes
- No results written (FRD file remains at 153 bytes - header only)

### What Was Tried:
✅ Correct parameter order: `phi, psi, c` (friction, dilation, cohesion)  
✅ Smaller load increments: 50, 100, 200... (instead of 100, 200, 500...)  
✅ Non-associative flow: Dilation angle = 0°  
✅ Proper step increments: 0.1,1.0,1e-6,1.0  
✅ All syntax verified against CalculiX source code

### Parameter Order in CalculiX:
CalculiX expects: `friction_angle, dilation_angle, cohesion` (phi, psi, c)
```python
f.write(f"{FRICTION_ANGLE},{DILATATION_ANGLE},{COHESION}\n")
# Example: 25.0,0.0,15.0 (25° friction, 0° dilation, 15 kN/m² cohesion)
```

### Possible Causes:
1. **Numerical instability**: Mohr-Coulomb parameters may cause convergence issues
2. **Step size**: Non-linear increments may be too large
3. **Material parameter interaction**: Cohesion and friction angle combination
4. **CalculiX implementation**: Potential bug or limitation in Mohr-Coulomb implementation

## Mohr-Coulomb Is Currently Enabled

The code already has Mohr-Coulomb enabled in `create_barrette_inp.py` (lines 203-208):

```python
f.write("*MOHR COULOMB\n")
# Format: friction angle (degrees), dilation angle (degrees), cohesion (kN/m²)
# Note: CalculiX expects: phi, psi, c (NOT c, phi, psi!)
f.write(f"{FRICTION_ANGLE},{DILATATION_ANGLE},{COHESION}\n")
```

**However, the analysis crashes** before results can be written. To temporarily disable Mohr-Coulomb, comment out these lines.

### Step 2: Adjust Step Increments

In `create_barrette_inp.py`, modify the step increment settings (around line 282):
```python
# For non-linear analysis with Mohr-Coulomb:
f.write("0.1,1.0,1e-6,1.0\n")  # Smaller initial increment for convergence
```

### Step 3: Check Parameters in `config.py`

Current parameters (disabled):
```python
COHESION = 15.0            # kN/m² - effective cohesion c'
FRICTION_ANGLE = 25.0      # degrees - effective friction angle φ'
DILATATION_ANGLE = 0.0     # degrees - dilation angle (0 = non-associative flow)
```

**Recommendations if enabling:**
- Start with smaller friction angle (e.g., 20°)
- Ensure cohesion is reasonable for the stress levels
- Consider reducing load increments initially
- Monitor convergence carefully

### Step 4: Test Gradually

1. Start with single load step (e.g., 100 kN)
2. If successful, add more steps gradually
3. Monitor CalculiX output for convergence warnings
4. Check `.sta` and `.cvg` files for convergence data

## Alternative Approaches

### Option 1: Simplified Non-Linear
- Use Drucker-Prager instead of Mohr-Coulomb (if CalculiX supports it)
- Try different yield criteria

### Option 2: Elasto-Plastic with Hardening
- Add hardening parameters to stabilize behavior
- Use smaller load increments

### Option 3: Staged Analysis
- Run initial linear elastic analysis
- Use results as initial conditions for non-linear
- Apply loads in smaller increments

## Current Working Configuration

✅ **Linear Elastic Soil** - Working perfectly
- All 11 load steps complete successfully
- Results exported to VTK format
- Visualization works in ParaView

## Next Steps

1. **Verify linear elastic results are correct** (check S-zz at top)
2. **Once validated**, attempt to add Mohr-Coulomb back
3. **Start with conservative parameters** and gradually increase complexity
4. **Monitor for convergence issues** and adjust step sizes accordingly

## References

- CalculiX documentation on Mohr-Coulomb: Check CalculiX manual
- Mohr-Coulomb parameters: See geotechnical analysis documentation
- Non-linear FEA best practices: Use small increments for plasticity

