import numpy as np
import matplotlib.pyplot as plt
from utils import correct_pbc, load_xyz_with_numpy

def extract_z_coordinates_with_pbc(xyz_file_path, atom_indices_1_based, c_vector_length):
    data, num_atoms, num_frames = load_xyz_with_numpy(xyz_file_path)
    atom_indices = [index - 1 for index in atom_indices_1_based]
    z_coords_multi_corrected = []

    for atom_index in atom_indices:
        z_coords = data[atom_index::num_atoms, 3].astype(float)
        z_coords_corrected = correct_pbc(z_coords, c_vector_length)
        z_coords_multi_corrected.append(z_coords_corrected)
    
    return np.array(z_coords_multi_corrected), num_frames

def subtract_first_frame(z_coords_multi):
    return z_coords_multi - z_coords_multi[:, 0][:, np.newaxis]

def plot_relative_displacement(z_coords_multi_relative, num_frames, start_frame=0, end_frame=None):
    if end_frame is None:
        end_frame = num_frames
    frames = np.arange(start_frame, end_frame)
    
    plt.figure(figsize=(10, 6))
    
    for i, z_displacement in enumerate(z_coords_multi_relative):
        plt.plot(frames, z_displacement[start_frame:end_frame], label=f'Atom {i+1}')
    
    plt.xlabel('Frame Number')
    plt.ylabel('Relative Z-Displacement')
    plt.title(f'Relative Z-Displacement of Atoms (Frames {start_frame} to {end_frame})')
    plt.legend()
    plt.grid(True)
    plt.show()
