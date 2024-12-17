import numpy as np
import MDAnalysis as mda
import matplotlib.pyplot as plt

class HalideInteractionAnalyzer:
    def __init__(self, psf_file, dcd_file, positive_n_indices, interaction_cutoff=3.0, halide_name='CL', halide_resname='LIG'):
        self.universe = mda.Universe(psf_file, dcd_file)
        self.positive_n_indices = positive_n_indices
        self.interaction_cutoff = interaction_cutoff
        self.halide_name = halide_name.upper()
        self.halide_resname = halide_resname
        
        # Select N atoms and Halide ions
        self.n_atoms = self.universe.atoms[[idx-1 for idx in positive_n_indices]]
        halide_selection = f'name {self.halide_name} and resname {self.halide_resname}'
        self.halide_ions = self.universe.select_atoms(halide_selection)

    def analyze_interactions(self):
        per_step_interactions = []
        halide_interaction_matrix = []
        
        for ts in self.universe.trajectory:
            distances = np.zeros((len(self.n_atoms), len(self.halide_ions)))
            
            for n_idx, n_atom in enumerate(self.n_atoms):
                for halide_idx, halide_ion in enumerate(self.halide_ions):
                    distance = np.linalg.norm(n_atom.position - halide_ion.position)
                    distances[n_idx, halide_idx] = distance
            
            interactions_mask = distances <= self.interaction_cutoff
            step_interactions = np.sum(interactions_mask)
            per_step_interactions.append(step_interactions)
            
            step_halide_interactions = np.sum(interactions_mask, axis=0)
            halide_interaction_matrix.append(step_halide_interactions)
        
        halide_interaction_matrix = np.array(halide_interaction_matrix)
        return per_step_interactions, halide_interaction_matrix

    def plot_interactions(self, per_step_interactions):
        plt.figure(figsize=(12, 6))
        plt.plot(range(len(per_step_interactions)), per_step_interactions, label=f'{self.halide_name} Interactions')
        plt.xlabel('Trajectory Step')
        plt.ylabel('Number of Interactions')
        plt.title(f'{self.halide_name} Ion Interactions Over Time')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
