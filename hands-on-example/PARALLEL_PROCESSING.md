# Parallel Processing in CalculiX

## Overview

CalculiX supports multi-core parallel processing through OpenMP. This can significantly speed up analysis, especially for:
- Large models (many elements)
- Non-linear analyses (deformation plasticity, Mohr-Coulomb)
- Multiple load steps

## Automatic Configuration

The `run_analysis.sh` script automatically detects and uses available CPU cores:

- **Detects CPU cores**: Uses `nproc` to find available cores
- **Uses N-1 cores**: Leaves 1 core free for system tasks
- **Sets environment variables**: Configures OpenMP for parallel execution

### Environment Variables

CalculiX uses these environment variables for parallelization:

1. **OMP_NUM_THREADS**: General OpenMP thread count
   ```bash
   export OMP_NUM_THREADS=11
   ```

2. **CCX_NPROC_STIFFNESS**: Threads for stiffness matrix computation
   ```bash
   export CCX_NPROC_STIFFNESS=11
   ```

3. **CCX_NPROC_RESULTS**: Threads for results computation
   ```bash
   export CCX_NPROC_RESULTS=11
   ```

The script automatically sets all three variables.

## Manual Configuration

If you want to manually control the number of cores:

### Option 1: Set Before Running
```bash
export OMP_NUM_THREADS=8
export CCX_NPROC_STIFFNESS=8
export CCX_NPROC_RESULTS=8
./run_analysis.sh
```

### Option 2: Modify Script
Edit `run_analysis.sh` and change:
```bash
USE_CORES=8  # Set to desired number of cores
```

### Option 3: One-Time Run
```bash
OMP_NUM_THREADS=8 CCX_NPROC_STIFFNESS=8 CCX_NPROC_RESULTS=8 ./run_analysis.sh
```

## Performance Expectations

- **Linear elastic analysis**: 2-4x speedup with 4-8 cores
- **Non-linear analysis**: 3-6x speedup with 4-8 cores
- **Diminishing returns**: Beyond 8-12 cores, speedup may be limited

## GPU Acceleration

CalculiX does **not** natively support GPU acceleration.

**Alternative: PaStiX Integration**
- Requires complex setup and recompilation
- Needs CUDA libraries for NVIDIA GPUs
- May not provide benefits for smaller models
- Best for very large models (millions of elements)

For most barrette pile analyses, CPU parallelization (OpenMP) is sufficient.

## Verification

Check if parallel processing is active:

1. **Monitor CPU usage**:
   ```bash
   top -H -p $(pgrep ccx_2.22)
   ```
   You should see multiple threads running.

2. **Check CalculiX output**: Look for messages about using multiple CPUs

3. **Compare runtime**: Run with 1 core vs multiple cores to see speedup

## Troubleshooting

**Problem**: No speedup observed
- **Solution**: Check that CalculiX was compiled with OpenMP (`-fopenmp` flag)
- **Solution**: Verify environment variables are set correctly

**Problem**: System becomes unresponsive
- **Solution**: Reduce number of cores (leave more free)
- **Solution**: Check available memory (parallel processing uses more RAM)

**Problem**: Analysis crashes with parallel processing
- **Solution**: Some non-linear analyses may be unstable with many cores
- **Solution**: Try with fewer cores (4-6) for non-linear materials

## References

- CalculiX Documentation: https://www.dhondt.de/
- OpenMP Documentation: https://www.openmp.org/
- CalculiX Forum: https://calculix.discourse.group/

