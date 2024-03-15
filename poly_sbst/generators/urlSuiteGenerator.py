from poly_sbst.generators.abstract_generator import AbstractGenerator
import numpy as np
import random
from poly_sbst.generators.urlGenerator import urlGenerator

class UrlTestSuiteGenerator(AbstractGenerator):
    """
    A class that generates test suites using a url generator.

    Attributes:
        _name (str): The name of the generator.
        test_gen (RandomGenerator): The url generator used to generate individual tests.
        max_length (int): The maximum length of the test suite.
        min_length (int): The minimum length of the test suite.
    """

    def __init__(self) -> None:
        super().__init__()
        self._name = "urlGenerator"
        self.test_gen = urlGenerator()
        self.max_length = 40
        self.min_length = 2

    @property
    def name(self) -> int:
        return self._name

    def cmp_func(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        Compare two test cases and return a similarity score.

        Args:
            x (np.ndarray): The first test case.
            y (np.ndarray): The second test case.

        Returns:
            float: The similarity score between the two test cases.
        """
        pass

    def generate_random_test(self) -> str:
        """
        Generate a random url test suite.

        Returns:
            str: The generated test suite.
        """
        n = random.randint(self.min_length, self.max_length)
        test_suite = []
        for i in range(n):
            test_suite.append(self.test_gen.generate_random_test())

        return np.array(test_suite)