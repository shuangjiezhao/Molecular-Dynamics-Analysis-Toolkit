from cof_analyzer import COFAnalyzer
from halide_interaction_analyzer import HalideInteractionAnalyzer

def main():
    # Example usage for COFAnalyzer
    cell_vectors = np.array([
        [45.603, 0.0, 0.0],
        [20.899221, 38.3637979, 0.0],
        [0.36934865, -0.99820589, 10.97249938]
    ])
    
    analyzer = COFAnalyzer("trajectory.dcd", cell_vectors)
    distances, pmf = analyzer.analyze_anion_distribution("F")
    analyzer.plot_pmf(distances, pmf)

    # Example usage for HalideInteractionAnalyzer
    psf_file = 'path/to/topology.psf'
    dcd_file = 'path/to/trajectory.dcd'
    positive_n_indices = [1, 2, 3]
    
    halide_analyzer = HalideInteractionAnalyzer(psf_file, dcd_file, positive_n_indices)
    interactions, matrix = halide_analyzer.run_analysis()
    
if __name__ == "__main__":
    main()
