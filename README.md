# Useful scripts for DAMA60 final

Most of the scripts on the repo have been based on the HWs of this year and on the last year’s finals. Most of them are “generalizable” i.e. they are designed to work with all the similar exercises. Despite that, the following list of exercises depicts the exercises that each script has been tested on. Feel free to contribute by uploading your scripts as well.

- Note: For the last year’s final exams we assume the files downloaded from the DAMA60 forum.

## Scripts in alphabetical order

### 0_1_scores_DCGpos_NDCGpos_Precision_Recall.ipynb

Calculates DCGpos, NDCGpos, Precision@N and Recall@N when we are given binary data (Hit=1, Miss=0) Kudos to Kiriakos for sharing! Tested on:

1. Question 19, DAMA60_Final-Exam_22-23

### BFR_-_MAHALANOBIS_CALCULATIONS_2.ipynb

Performs the BFR algorithm. Kudos to Kiriakos for sharing! Tested on:

1. HW3, Topic-4

### cosine_sim.py

Calculates cosine similarity

### Distance_metrics.py

Collection of similarity/distance metrics calculations along with some functions to perform vector calculations. Kudos to Nikos for sharing! It contains two classes so if you want to use them in another script you have to import them first.

### GENERALIZED_BALANCE_AND_BALANCE_ALGORITHM_1.ipynb

BALANCE and Generalized BALANCE algorithm. Kudos to Kiriakos!

### GN_edge_betweenness.py

Girvan - Newman. Performs calculation for betweenness centrality of edge and of node. Two functions for each calculation. Call one function at a time to avoid graphs displaying one on top of the other. Tested on:

1. Question 10, DAMA60_Final-Exam_22-23 (`betweenness_edge()` function)
2. HW4 Topic-4(b) (`betweenness_node()` function)

### HITS.py

Perform the HITS algorithm. Tested on:

1. Question 9, DAMA60_Final-Exam_22-23

### **ITEM_BASED_COLABORATIVE_FILTERING2.ipynb**

Item - item based collaboration filtering. Kudos to Kiriakos!

### Jaccard.py

Performs Jaccard similarity calculation both in binary  and numerical vectors. Tested on:

1. HW2, Topic-3 (b)

### laplacian_ui.py

Requests user input of the nodes and the connections between them. Creates the adjacency matrix, returns it and then returns its Laplacian form (undirected graphs). Tested on:

1. Question 13, DAMA60_Final-Exam_22-23

### LSH.py

Performs Locality Sensitive Hashing. Use if given the hashed permutations (here H1, H2, H3) and the initial sets (here S1, S2, S3) and asked to find the signatures. Tested on:

1. HW2, Topic-3 (a)

### MAE_MSE_RMSE.py

Calculates MAE, MSE and RMSE. Tested on:

1. HW4, Topic-3(a)

### margin.py

Calculates the margin of of a linear separator. Kudos to Petros and NIkos! Tested on:

1. Question 18, DAMA60_Final-Exam_22-23

### neuron.py

Calculates the MSE of a neuron based on different activation functions (selected in the script). Kudos to Petros! Tested on:

1. Question 16, DAMA60_Repeat-Exam_22-23-Updated

### Pagerank_UI.py

Requests user input of the nodes and the connections between them, along with the beta and the number of iterations. It constructs the transition probability matrix (M) and performs the PageRank algorithm with or without teleport (use beta=1 for no teleport), for the given iterations. Tested on:

1. HW3, Topic-2
2. Question 16, DAMA60_Final-Exam_22-23

### PCY.py

It accepts an array/list of transactions and returns all of the intermediate and final results of the algorithm (frequent items, hashed pairs/buckets, candidate pairs, frequent pairs, infrequent pairs). Kudos to Kiriakos for providing it! Tested on:

1. HW3, Topic-3

### perceptron.py

Simulates a perceptron and accepts all possible parameters. Returns the predicted y’s and the updated weights after n iterations. Tested on:

1. HW5, Topic-2(a)

### RWR.py

Performs Random Walk with Restart. Tested on:

1. HW4, Topic-4(a)

### SVM (Folder)

Contains two versions of the SVM classifier. One that accepts and returns fractions and one that accepts and returns floats. Tested on:

1. HW5, Topic-2(b)
2. HW5 - Quiz, Question 1

### USER__ITEM_BASED_COLLABORATIVE_FILTERING_1.ipynb

User - Item based collaborative filtering. Kudos to Kiriakos!

### UV_RMSE.py

Calculates the RMSE of the UV decomposition. In the initial matrix use `None` to all of the unknown ratings. Tested on:

1. Question 8, DAMA60_Final-Exam_22-23

### with_scores_DCGpos_NDCGpos_Precision_Recall.ipynb

Calculates DCGpos, NDCGpos, Precision@N and Recall@N when we are given scores instead of binary data. Kudos to Kiriakos for sharing! Tested on: