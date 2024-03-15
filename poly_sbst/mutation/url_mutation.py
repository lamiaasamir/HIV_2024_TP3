from poly_sbst.mutation.abstract_mutation import AbstractMutation
import numpy as np

class UrlTestSuiteMutation(AbstractMutation):
    """
    Mutation operator for URL test suite generation.

    Inherits from AbstractMutation.
    """

    def __init__(self, mut_rate: float = 0.4, generator=None):
        """
        Initialize the URL test suite mutation operator.

        Args:
            mut_rate (float): The mutation rate, representing the probability of mutation for each individual (default: 0.4).
            generator: The random number generator to use for generating random numbers.
        """ 
        super().__init__(mut_rate,generator)
    
    def _do_mutation(self, x) -> np.ndarray:

        possible_mutations = [
            self._shuffle_elements,
            self._reverse_elements,
            self._duplicate_elements,
            self._remove_duplicates,
            self._insert_symbols           
        ]
        mutator = np.random.choice(possible_mutations)

        return mutator(x)

    def _shuffle_elements(self, s):
        """Returns s with its elements shuffled"""
        np.random.shuffle(s)
        return s

    def _reverse_elements(self, s):
        """Returns s with its elements reversed"""
        return s[::-1]

    def _duplicate_elements(self, s):
        """Returns s with a random element duplicated"""
        if len(s) > 0:
            index_to_duplicate = np.random.randint(len(s))
            return np.insert(s, index_to_duplicate, s[index_to_duplicate])
        return s

    def _remove_duplicates(self, s):
        """Returns s with duplicate elements removed"""
        return np.unique(s)
    def _insert_symbols(self, s):
        """Returns s with a random element duplicated"""
        index_to_insert = np.random.randint(len(s))
        return np.insert(s, index_to_insert, "///////")
   

    

    
    
