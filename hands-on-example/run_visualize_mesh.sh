#!/bin/bash
# Script to visualize mesh with proper environment setup
#
# This script handles the environment setup automatically.
# You don't need to source anything or activate conda manually.

# Set FEniCS environment variables
export PKG_CONFIG_PATH="$HOME/.conda/envs/fenics-env/lib/pkgconfig:$PKG_CONFIG_PATH"

# Optional: Add conda environment to PATH for any subprocesses
export PATH="$HOME/.conda/envs/fenics-env/bin:$PATH"

# Run mesh visualization using conda environment Python
echo "Generating mesh visualization..."
echo "Using FEniCS environment: $HOME/.conda/envs/fenics-env"
echo ""
~/.conda/envs/fenics-env/bin/python visualize_mesh.py

