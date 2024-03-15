import numpy as np
from poly_sbst.crossover.abstract_crossover import AbstractCrossover

class HTMLTestSuiteCrossover(AbstractCrossover):
    def __init__(self, cross_rate: float = 0.9):
        super().__init__(cross_rate)


    def _do_crossover(self, problem, a, b) -> tuple:

        """
        Performs one-point crossover between two HTML parents and returns the offspring.

        Parameters:
        - problem: The optimization problem.
        - a: The first parent.
        - b: The second parent.

        Returns:
        - tuple: The offspring generated from crossover.
        """
        #  length of the parents
        length = len(a)

        # checking if the length is too short for crossover
        if length <= 1:
            return a, b  # Return the original parents

        # selecting a random crossover point
        crossover_point = np.random.randint(1, length)

        # performing crossover
        off_a = np.concatenate((a[:crossover_point], b[crossover_point:]))
        off_b = np.concatenate((b[:crossover_point], a[crossover_point:]))

        return off_a, off_b