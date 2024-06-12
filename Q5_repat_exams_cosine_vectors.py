import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def modify_and_calculate_cosine_similarity(vectors, multipliers):
    # Convert vectors to numpy arrays for easier manipulation
    vectors = [np.array(vec) for vec in vectors]
    
    initial_vectors = [vec.copy() for vec in vectors]
    results = []

    for multiplier in multipliers:
        modified_vectors = [vec.copy() for vec in initial_vectors]

        # Modify the last element of each vector by the multiplier
        for vec in modified_vectors:
            vec[-1] *= multiplier
        
        # Calculate cosine similarities between pairs of modified vectors
        for i in range(len(modified_vectors)):
            for j in range(i + 1, len(modified_vectors)):
                cos_sim = cosine_similarity([modified_vectors[i]], [modified_vectors[j]])[0][0]
                results.append({
                    'multiplier': multiplier,
                    'vector_pair': (i, j),
                    'cosine_similarity': cos_sim
                })
    
    return results

# Example vectors
vectors = [
    [1,0,1,0,1,2],
    [1,1,0,0,1,6],
    [0,1,0,1,0,2]
]

# List of multipliers
multipliers = [0, 1, 2]

# Call the function and get the results
results = modify_and_calculate_cosine_similarity(vectors, multipliers)

# Print the results
for result in results:
    print(f"Multiplier: {result['multiplier']}, Vector Pair: {result['vector_pair']}, Cosine Similarity: {result['cosine_similarity']:.4f}")
