from itertools import combinations
from collections import defaultdict

# Example list of transactions
transactions = [
    [1, 2, 5],
    [2, 3, 6],
    [3, 4, 5],
    [1,3,5],
    [2, 4, 7],
    [1, 5, 6],
    [2, 3, 4 ],
    [2,4,5,7],
    [3,5,7],
    [2,4]
    
]

# Support threshold
support_threshold = 5

# First pass: count individual items and create a hash table for pairs
item_counts = defaultdict(int)
pair_hash_table = defaultdict(int)
#--------------------------------
# DEFINE THE HASH FUNCTION
def hash_pair(pair):
    return (pair[0] * pair[1]) % 7  # Hash function : (i*j)MOD7
#-----------------------------------
# Count individual items and hash pairs
for transaction in transactions:
    for item in transaction:
        item_counts[item] += 1
    for pair in combinations(transaction, 2):
        pair_hash_table[hash_pair(pair)] += 1

# Filter out the frequent items
frequent_items = {item for item, count in item_counts.items() if count >= support_threshold}
print('Frequent items:', frequent_items)

# Create the bitmap from the hash table based on the support threshold
bitmap = {hash_value: count >= support_threshold for hash_value, count in pair_hash_table.items()}
print('Frequent buckets (hashed pairs):', {bucket for bucket, is_frequent in bitmap.items() if is_frequent})

# Second pass: generate candidate pairs using the bitmap and frequent items
candidates = set()
for transaction in transactions:
    # Filter transaction items based on frequent items
    frequent_transaction_items = [item for item in transaction if item in frequent_items]
    for pair in combinations(frequent_transaction_items, 2):
        if bitmap[hash_pair(pair)]:
            candidates.add(pair)

print('Candidate pairs:', candidates)

# Count the support for the candidate pairs
frequent_pairs = defaultdict(int)
infrequent_pairs = defaultdict(int)
for transaction in transactions:
    for pair in candidates:
        if set(pair).issubset(transaction):
            frequent_pairs[pair] += 1

# Separate frequent and infrequent pairs based on the support threshold
infrequent_pairs = {pair: count for pair, count in frequent_pairs.items() if count < support_threshold}
frequent_pairs = {pair: count for pair, count in frequent_pairs.items() if count >= support_threshold}

print('Frequent pairs with their support counts:')
for pair, count in frequent_pairs.items():
    print(f'{pair}: {count}')

print('Infrequent pairs with their support counts:')
for pair, count in infrequent_pairs.items():
    print(f'{pair}: {count}')

# Output the total support of every bucket
print('Support count for each bucket:')
for hash_value, count in pair_hash_table.items():
    print(f'Bucket {hash_value}: {count} support')