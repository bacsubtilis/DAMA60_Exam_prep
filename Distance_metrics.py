import math
import hashlib
import numpy as np
from collections import defaultdict

memoization = {}


class Similarity:
    """
    This class contains instances of similarity / distance metrics. These are used in centroid-based clustering
    algorithms to identify similar patterns and put them into the same homogeneous subsets.
    :param minimum: the minimum distance between two patterns (so you don't divide by 0)
    """

    def __init__(self, minimum):
        self.e = minimum
        self.vector_operators = VectorOperations()

    def manhattan_distance(self, p_vec, q_vec):
        """
        This method implements the Manhattan distance metric.
        :param p_vec: vector one
        :param q_vec: vector two
        :return: the Manhattan distance between vector one and two
        """
        return max(np.sum(np.abs(p_vec - q_vec)), self.e)

    def square_euclidean_distance(self, p_vec, q_vec):
        """
        This method implements the squared Euclidean distance metric.
        :param p_vec: vector one
        :param q_vec: vector two
        :return: the squared Euclidean distance between vector one and two
        """
        diff = p_vec - q_vec
        return max(np.sum(diff ** 2), self.e)

    def euclidean_distance(self, p_vec, q_vec):
        """
        This method implements the Euclidean distance metric.
        :param p_vec: vector one
        :param q_vec: vector two
        :return: the Euclidean distance between vector one and two
        """
        return max(math.sqrt(self.square_euclidean_distance(p_vec, q_vec)), self.e)

    def half_square_euclidean_distance(self, p_vec, q_vec):
        """
        This method implements the half squared Euclidean distance metric.
        :param p_vec: vector one
        :param q_vec: vector two
        :return: the half squared Euclidean distance between vector one and two
        """
        return max(0.5 * self.square_euclidean_distance(p_vec, q_vec), self.e)

    def cosine_similarity(self, p_vec, q_vec):
        """
        This method implements the cosine similarity metric.
        :param p_vec: vector one
        :param q_vec: vector two
        :return: the cosine similarity between vector one and two
        """
        pq = self.vector_operators.product(p_vec, q_vec)
        p_norm = self.vector_operators.norm(p_vec)
        q_norm = self.vector_operators.norm(q_vec)
        return max(pq / (p_norm * q_norm), self.e)

    def tanimoto_coefficient(self, p_vec, q_vec):
        """
        This method implements the cosine Tanimoto coefficient metric.
        :param p_vec: vector one
        :param q_vec: vector two
        :return: the Tanimoto coefficient between vector one and two
        """
        pq = self.vector_operators.product(p_vec, q_vec)
        p_square = self.vector_operators.square(p_vec)
        q_square = self.vector_operators.square(q_vec)
        return max(pq / (p_square + q_square - pq), self.e)

    def minkowski_distance(self, p_vec, q_vec, p=3):
        """
        This method implements the Minkowski distance metric.
        :param p_vec: vector one
        :param q_vec: vector two
        :param p: the order of the Minkowski distance (default is 3)
        :return: the Minkowski distance between vector one and two
        """
        diff = np.abs(p_vec - q_vec) ** p
        return max(np.sum(diff) ** (1 / p), self.e)

    def infinity_norm(self, p_vec, q_vec):
        """
        This method implements the L∞ (L-infinity) distance metric, also known as the Chebyshev distance.
        :param p_vec: vector one
        :param q_vec: vector two
        :return: the L∞ distance between vector one and two
        """
        return max(np.max(np.abs(p_vec - q_vec)), self.e)

    def levenshtein_distance(self, s1, s2):
        """
        This method implements the Levenshtein distance (edit distance) metric for strings.
        :param s1: string one
        :param s2: string two
        :return: the Levenshtein distance between string one and two
        """
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    @staticmethod
    def get_key(p_vec, q_vec):
        """
        This method returns a unique hash value for two vectors.
        :param p_vec: vector one
        :param q_vec: vector two
        :return: a unique hash
        """
        p_hash = hashlib.sha1(p_vec).hexdigest()
        q_hash = hashlib.sha1(q_vec).hexdigest()
        return p_hash + q_hash


class VectorOperations:
    """
    This class contains useful implementations of methods which can be performed on vectors.
    """

    @staticmethod
    def product(p_vec, q_vec):
        """
        This method returns the product of two lists / vectors.
        :param p_vec: vector one
        :param q_vec: vector two
        :return: the product of p_vec and q_vec
        """
        return np.dot(p_vec, q_vec)

    @staticmethod
    def square(p_vec):
        """
        This method returns the square of a vector.
        :param p_vec: the vector to be squared
        :return: the squared value of the vector
        """
        return np.sum(p_vec ** 2)

    @staticmethod
    def norm(p_vec):
        """
        This method returns the norm value of a vector.
        :param p_vec: the vector to be normed
        :return: the norm value of the vector
        """
        return np.linalg.norm(p_vec)


# Example Usage
if __name__ == "__main__":
    similarity = Similarity(minimum=1e-9)
############################################   
    p_vec = np.array([1, 2, -1])    #INPUT1#
    q_vec = np.array([2, 1,  1])           #
############################################
    
    print("Manhattan Distance:", similarity.manhattan_distance(p_vec, q_vec))
    print("Euclidean Distance:", similarity.euclidean_distance(p_vec, q_vec))
    print("Cosine Similarity:", similarity.cosine_similarity(p_vec, q_vec))
    print("Minkowski Distance (p=3):", similarity.minkowski_distance(p_vec, q_vec, p=3))
    print("L∞ Distance:", similarity.infinity_norm(p_vec, q_vec))

############################    
    s1 = "ebook"    #INPUT2#
    s2 = "bucks"           #
############################
    print("Levenshtein(Edit) Distance:", similarity.levenshtein_distance(s1, s2))
