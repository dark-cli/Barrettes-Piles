#!/bin/bash
# Script to run barrette FEA analysis with proper environment setup
#
# This script handles the environment setup automatically.
# You don't need to source anything or activate conda manually.

# Set FEniCS environment variables
export PKG_CONFIG_PATH="$HOME/.conda/envs/fenics-env/lib/pkgconfig:$PKG_CONFIG_PATH"

# Optional: Add conda environment to PATH for any subprocesses
export PATH="$HOME/.conda/envs/fenics-env/bin:$PATH"

# Run analysis using conda environment Python
echo "Running barrette FEA analysis..."
echo "Using FEniCS environment: $HOME/.conda/envs/fenics-env"
echo ""
~/.conda/envs/fenics-env/bin/python barrette_fea.py

