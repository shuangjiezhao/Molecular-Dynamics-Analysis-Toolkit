import numpy as np

def correct_pbc(z_coords, c_vector_length):
    corrected_z_coords = np.copy(z_coords)
    half_c = c_vector_length / 2.0
    
    for i in range(1, len(z_coords)):
        dz = z_coords[i] - z_coords[i - 1]
        
        if dz > half_c:
            corrected_z_coords[i:] -= c_vector_length
        elif dz < -half_c:
            corrected_z_coords[i:] += c_vector_length
    
    return corrected_z_coords

def load_xyz_with_numpy(xyz_file_path):
    data = []
    with open(xyz_file_path, 'r') as file:
        lines = file.readlines()
    
    index = 0
    while index < len(lines):
        num_atoms = int(lines[index].strip())
        index += 2
        for atom_line in lines[index:index + num_atoms]:
            atom_data = atom_line.split()
            data.append(atom_data)
        index += num_atoms
    
    return np.array(data, dtype=object), num_atoms, len(lines) // (num_atoms + 2)

def apply_periodic_boundaries(coordinates, cell_vectors):
    inv_cell = np.linalg.inv(cell_vectors)
    frac_coords = np.dot(coordinates, inv_cell)
    frac_coords = frac_coords - np.floor(frac_coords)
    return np.dot(frac_coords, cell_vectors)
