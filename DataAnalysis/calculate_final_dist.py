import pandas as pd

def calculate_weighted_average_distance(normalized_matrices, weights):
    # Validate that matrices and weights have the same names
    assert set(normalized_matrices.keys()) == set(weights.keys()), \
        "Matrix names and weight keys must match"
    
    # Validate that weights sum to 1
    assert sum(weights.values()) == 1, "Weights must sum to 1"
    
    # Initialize an empty matrix for storing the overall distances
    overall_distance_matrix = pd.DataFrame(0, 
                                           index=normalized_matrices[next(iter(normalized_matrices))].index, 
                                           columns=normalized_matrices[next(iter(normalized_matrices))].columns)
    
    # Calculate the weighted average distance
    for matrix_name, matrix in normalized_matrices.items():
        overall_distance_matrix += weights[matrix_name] * matrix
    
    return overall_distance_matrix


# Load normalized matrices
normalized_matrices = {
    'value': pd.read_csv('value_normalized.csv', index_col=0),
    'interests': pd.read_csv('interests_normalized.csv', index_col=0),
    'worktask': pd.read_csv('worktask_normalized.csv', index_col=0),
    'knowledge': pd.read_csv('knowledge_normalized.csv', index_col=0),
    'skill': pd.read_csv('skill_normalized.csv', index_col=0),
}

# Define weights
weights = {
    'value': 0.2,
    'interests': 0.2,
    'worktask': 0.2,
    'knowledge': 0.2,
    'skill': 0.2,
}

# Calculate the overall distance matrix
overall_distance_matrix = calculate_weighted_average_distance(normalized_matrices, weights)

# Save the overall distance matrix to a CSV file
overall_distance_matrix.to_csv('overall_distance_matrix.csv')