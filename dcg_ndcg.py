import numpy as np

# Given data
ranks = np.array([1, 2, 3, 4, 5])
hits = np.array([1, 0, 1, 0, 1])

def dcg_at_k(r, k):
    """Calculate the Discounted Cumulative Gain at rank k."""
    r = np.asfarray(r)[:k]
    if r.size:
        return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
    return 0.

def ndcg_at_k(r, k):
    """Calculate the Normalized Discounted Cumulative Gain at rank k."""
    dcg_max = dcg_at_k(sorted(r, reverse=True), k)
    if not dcg_max:
        return 0.
    return dcg_at_k(r, k) / dcg_max

# Calculate nDCG for the given hits and ranks
k = len(hits)  # Calculate nDCG at full length of hits array
ndcg_score = ndcg_at_k(hits, k)

print(f"Normalized Discounted Cumulative Gain (nDCG) score: {ndcg_score:.4f}")
