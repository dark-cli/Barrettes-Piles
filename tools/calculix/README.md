# CalculiX Installation

CalculiX 2.22 has been successfully built and installed.

## Location

- **Executable**: `CalculiX/ccx_2.22/src/ccx_2.22`
- **Source**: `CalculiX/ccx_2.22/src/`
- **Dependencies**: 
  - SPOOLES.2.2 (built)
  - ARPACK (built)

## Usage

### Basic Command

```bash
cd "/home/max/Documents/master/Barrettes Piles/tools/calculix/CalculiX/ccx_2.22/src"
./ccx_2.22 -i jobname
```

Where `jobname` is the name of your input file (without the `.inp` extension).

### Example

If you have a file called `barrette.inp`, run:

```bash
./ccx_2.22 -i barrette
```

This will generate:
- `barrette.dat` - output file with calculation results
- `barrette.frd` - results file for visualization (can be opened with CGX or other post-processors)

## Material Models

CalculiX supports Mohr-Coulomb material model for geotechnical analysis. The Mohr-Coulomb model can be defined in the input file with parameters:
- Cohesion ($c'$)
- Friction angle ($\phi'$)
- Young's modulus ($E_s$)
- Poisson's ratio ($\nu_s$)

## Input File Format

CalculiX uses ABAQUS-like input format (`.inp` files). You need to define:
1. Nodes and elements
2. Material properties
3. Boundary conditions
4. Loads
5. Analysis steps

## Next Steps

- Create input files for barrette analysis
- Use preprocessors (FreeCAD, Gmsh, PrePoMax) to generate input files
- For visualization, install CGX (CalculiX GraphiX) or use third-party tools

