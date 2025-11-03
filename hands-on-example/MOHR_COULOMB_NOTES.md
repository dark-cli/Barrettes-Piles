# Mohr-Coulomb Material Model Notes

## Current Status

**Mohr-Coulomb is currently DISABLED** in the analysis.

The soil material is currently using **linear elastic** behavior only.

## Why Mohr-Coulomb Was Disabled

During testing, CalculiX was crashing (segmentation fault) when Mohr-Coulomb plasticity was enabled. The crash occurred during the Newton-Raphson iterative procedure for non-linear analysis.

### Symptoms Observed:
- CalculiX detected loads correctly (88 distributed facial loads)
- Analysis started successfully
- Crash occurred during non-linear solution phase
- No results written (FRD file remained at 153 bytes - header only)

### Possible Causes:
1. **Numerical instability**: Mohr-Coulomb parameters may cause convergence issues
2. **Step size**: Non-linear increments may be too large
3. **Material parameter interaction**: Cohesion and friction angle combination
4. **CalculiX implementation**: Potential bug or limitation in Mohr-Coulomb implementation

## Enabling Mohr-Coulomb

To re-enable Mohr-Coulomb plasticity:

### Step 1: Edit `create_barrette_inp.py`

Uncomment lines 205-207:
```python
f.write("*MOHR COULOMB\n")
# Format: cohesion (kN/m²), friction angle (degrees), dilation angle (degrees)
f.write(f"{COHESION},{FRICTION_ANGLE},{DILATATION_ANGLE}\n")
```

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

