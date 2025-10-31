#!/usr/bin/env python3
"""
Test script to verify setup and dependencies
Run this before running barrette_fea.py
"""

print("=" * 60)
print("Barrette FEA Setup Verification")
print("=" * 60)

errors = []
warnings = []

# Test Python version
import sys
print(f"\n[1] Python version: {sys.version}")
if sys.version_info < (3, 7):
    errors.append("Python 3.7 or higher required")

# Test basic imports
print("\n[2] Testing basic dependencies...")
try:
    import numpy as np
    print(f"   ✓ NumPy {np.__version__}")
except ImportError:
    errors.append("NumPy not installed")

try:
    import matplotlib
    print(f"   ✓ Matplotlib {matplotlib.__version__}")
except ImportError:
    errors.append("Matplotlib not installed")

# Test FEniCS
print("\n[3] Testing FEniCS...")
try:
    import fenics
    fenics_version = getattr(fenics, '__version__', 'installed')
    print(f"   ✓ FEniCS {fenics_version}")
except ImportError:
    warnings.append("FEniCS not installed - required to run analysis")
    print("   ✗ FEniCS not found")
    print("\n   Install FEniCS using:")
    print("   conda install -c conda-forge fenics")

# Test config
print("\n[4] Testing configuration...")
try:
    import config
    print("   ✓ config.py loaded successfully")
    print(f"   - Barrette: {config.BARRETTE_LENGTH}x{config.BARRETTE_WIDTH}x{config.BARRETTE_DEPTH} m")
    print(f"   - Mesh: {config.MESH_DENSITY_X}x{config.MESH_DENSITY_Y}x{config.MESH_DENSITY_Z}")
    print(f"   - Load increments: {len(config.LOAD_INCREMENTS)}")
except Exception as e:
    errors.append(f"Error loading config.py: {e}")

# Test utils
print("\n[5] Testing utility functions...")
try:
    import utils
    print("   ✓ utils.py loaded successfully")
    
    # Test D matrix construction
    D = utils.construct_D_matrix(10000, 0.3)
    if D.shape == (6, 6):
        print("   ✓ construct_D_matrix() works")
    else:
        errors.append("construct_D_matrix() returns wrong shape")
    
    print(f"   ✓ FEniCS available: {utils.FENICS_AVAILABLE}")
except Exception as e:
    errors.append(f"Error loading utils.py: {e}")

# Test main script syntax
print("\n[6] Testing main script syntax...")
try:
    import py_compile
    py_compile.compile('barrette_fea.py', doraise=True)
    print("   ✓ barrette_fea.py syntax OK")
except py_compile.PyCompileError as e:
    errors.append(f"Syntax error in barrette_fea.py: {e}")

# Summary
print("\n" + "=" * 60)
if errors:
    print("❌ ERRORS FOUND:")
    for error in errors:
        print(f"   - {error}")
    print("\nPlease fix errors before running analysis.")
    sys.exit(1)
elif warnings:
    print("⚠️  WARNINGS:")
    for warning in warnings:
        print(f"   - {warning}")
    print("\nSetup OK, but analysis cannot run without FEniCS.")
    print("Install FEniCS to proceed with analysis.")
else:
    print("✅ All checks passed!")
    print("\nReady to run analysis:")
    print("   python barrette_fea.py")
print("=" * 60)

