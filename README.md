# Molecular Dynamics Analysis Toolkit
This collection includes a variety of Python functions and classes for analyzing molecular dynamics (MD) simulation data. The code is organized into modules focusing on specific tasks, such as analyzing anion distributions, extracting z-coordinates with periodic boundary corrections, plotting interaction data, and generating insights from trajectory files. 

# Organized Structure of the Code
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
