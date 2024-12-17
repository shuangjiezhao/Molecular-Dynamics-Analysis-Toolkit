# Molecular Dynamics Analysis Toolkit
This collection includes a variety of Python functions and classes for analyzing molecular dynamics (MD) simulation data. The code is organized into modules focusing on specific tasks, such as analyzing anion distributions, extracting z-coordinates with periodic boundary corrections, plotting interaction data, and generating insights from trajectory files. 

## Organized Structure of the Code
1. File Parsing and Data Processing

   - load_xyz_with_numpy(): Reads .xyz files into a structured format.
   - read_geometry_with_ase(): Parses geometry and lattice data using ASE.
 
2. Periodic Boundary Corrections

   - correct_pbc(): Adjusts z-coordinates to correct for periodic boundary conditions (PBC).
   - extract_z_coordinates_with_pbc(): Extracts z-coordinates of atoms with PBC corrections.

3. Analysis Classes

   - COFAnalyzer:
     - Analyzes anion distributions relative to specific atomic sites.
     - Calculates potential of mean force (PMF) along z-axes and distances.
   - HalideInteractionAnalyzer:
     - Tracks interactions between halide ions and positively charged atoms.
     - Generates per-step interaction data and rolling trends.
     - Saves results as CSV files and visualizes interaction patterns.
    
4. Data Visualization

   - plot_relative_displacement(): Visualizes z-displacements of atoms over time.
   - compare_halide_interactions(): Compares halide ion interactions using boxplots and KDE.
   - plot_pmf(): Creates PMF plots for atomic group interactions.
   - High-quality visualizations using libraries like Matplotlib and Seaborn.

5. Utility Functions

   - sphere_volume() and calculate_overlap(): Calculate sphere volumes and overlaps in molecular geometries.
   - calculate_minimum_distance(): Computes minimum distances between atoms considering periodicity.

## Features

- **Coordinate Processing**: Handles `.xyz` files and applies periodic boundary corrections.
- **Anion and Ion Analysis**:
  - Analyze distances and potential of mean force (PMF) for anions relative to molecular frameworks.
  - Track and compare halide ion interactions across time.
- **Visualization**: Create high-quality plots for relative displacements, PMF, interaction trends, and spatial overlaps.
- **Integration with Tools**: Compatible with ASE, MDAnalysis, and Matplotlib for efficient analysis.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/md-analysis-toolkit.git
   ```

2. Install required dependencies:
   ```bash
   pip install numpy pandas matplotlib seaborn ase MDAnalysis
   ```

## Usage
1. Analyze Z-Displacement with Periodic Boundaries
   ```python
from analysis import extract_z_coordinates_with_pbc, plot_relative_displacement

xyz_file_path = "path/to/structure.xyz"
atom_indices = [1, 2, 3]
c_vector_length = 10.0

z_coords, num_frames = extract_z_coordinates_with_pbc(xyz_file_path, atom_indices, c_vector_length)
plot_relative_displacement(z_coords, num_frames)
```
