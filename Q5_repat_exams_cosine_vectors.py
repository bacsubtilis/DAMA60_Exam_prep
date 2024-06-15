import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def modify_and_calculate_cosine_similarity(vectors, multipliers):
    # Convert vectors to numpy arrays for easier manipulation
    vectors = {name: np.array(vec) for name, vec in vectors.items()}
    
    initial_vectors = {name: vec.copy() for name, vec in vectors.items()}
    results = []

    for multiplier in multipliers:
        modified_vectors = {name: vec.copy() for name, vec in initial_vectors.items()}

        # Modify the last element of each vector by the multiplier
        for name in modified_vectors:
            modified_vectors[name][-1] *= multiplier
        
        # Calculate cosine similarities between pairs of modified vectors
        vector_names = list(modified_vectors.keys())
        for i in range(len(vector_names)):
            for j in range(i + 1, len(vector_names)):
                name_i = vector_names[i]
                name_j = vector_names[j]
                cos_sim = cosine_similarity([modified_vectors[name_i]], [modified_vectors[name_j]])[0][0]
                results.append({
                    'multiplier': multiplier,
                    'vector_pair': (name_i, name_j),
                    'cosine_similarity': cos_sim
                })
    
    return results

# Example vectors
vectors = {
    'A': [1, 0, 1, 0, 1, 2],
    'B': [1, 1, 0, 0, 1, 6],
    'C': [0, 1, 0, 1, 0, 2]
}

# List of multipliers
multipliers = [0, 1, 2]

# Call the function and get the results
results = modify_and_calculate_cosine_similarity(vectors, multipliers)

# Print the results
for result in results:
    print(f"Multiplier: {result['multiplier']}, Cosine similarity {result['vector_pair'][0]}{result['vector_pair'][1]}: {result['cosine_similarity']:.4f}")
