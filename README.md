# Useful scripts for DAMA60 final

Most of the scripts on the repo have been based on the HWs of this year and on the last year’s finals. Most of them are “generalizable” i.e. they are designed to work with all the similar exercises. Despite that, the following list of exercises depicts the exercises that each script has been tested on. Feel free to contribute by uploading your scripts as well.

- Note: For the last year’s final exams we assume the files downloaded from the DAMA60 forum.

## Scripts in alphabetical order

### dcg_ndcg.py

Calculates DCG and NDCG. Tested on:

1. Question 19, DAMA60_Final-Exam_22-23 

### HITS.py

Perform the HITS algorithm. Tested on:

1. Question 9, DAMA60_Final-Exam_22-23

### Jaccard.py

Performs Jaccard similarity calculation both in binary  and numerical vectors. Tested on:

1. HW2, Topic-3 (b)

### laplacian_ui.py

Requests user input of the nodes and the connections between them. Creates the adjacency matrix, returns it and then returns its Laplacian form (undirected graphs). Tested on:

1. Question 13, DAMA60_Final-Exam_22-23

### LSH.py

Performs Locality Sensitive Hashing. Use if given the hashed permutations (here H1, H2, H3) and the initial sets (here S1, S2, S3) and asked to find the signatures. Tested on:

1. HW2, Topic-3 (a)

### Pagerank_UI.py

Requests user input of the nodes and the connections between them, along with the beta and the number of iterations. It constructs the transition probability matrix (M) and performs the PageRank algorithm with or without teleport (use beta=1 for no teleport), for the given iterations. Tested on:

1. HW3, Topic-2
2. Question 16, DAMA60_Final-Exam_22-23

### PCY.py

It accepts an array/list of transactions and returns all of the intermediate and final results of the algorithm (frequent items, hashed pairs/buckets, candidate pairs, frequent pairs, infrequent pairs). Kudos to Kiriakos for providing it! Tested on:

1. HW3, Topic-3