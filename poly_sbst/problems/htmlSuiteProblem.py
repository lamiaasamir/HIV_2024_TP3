from poly_sbst.problems.abstract_problem import AbstractProblem
from poly_sbst.common.abstract_executor import AbstractExecutor
import numpy as np

class HTMLTestSuiteProblem(AbstractProblem):
    """
    Class for defining the test evaluation metrics for HTML test suite generation.

    Inherits from AbstractProblem.
    """

    def __init__(self, executor: AbstractExecutor, n_var: int=1, n_obj=1, n_ieq_constr=0, xl=None, xu=None):
        """
        Initialize the HTML test suite problem.

        Args:
            executor (AbstractExecutor): The executor used for evaluating test cases.
            n_var (int): The number of decision variables (default: 1).
            n_obj (int): The number of objectives (default: 3).
            n_ieq_constr (int): The number of inequality constraints (default: 0).
            xl: Lower bounds of decision variables (default: None).
            xu: Upper bounds of decision variables (default: None).
        """
        super().__init__(executor=executor, n_var=n_var, n_obj=n_obj, n_ieq_constr=n_ieq_constr, xl=xl, xu=xu)
        self.executor = executor
        self._name = "HTMLTestSuiteProblem"
        self.previous_coverage = 0
        self.first_evaluation = True
        self.maxFitnessList=[]
        self.iterationsList=[]

    def _evaluate(self, x:np.ndarray, out, *args, **kwargs):
        """
        Evaluate the solution by running the test suite and calculating evaluation metrics.

         Args:
            x (numpy.ndarray): The decision variables.
            out (dict): The output dictionary.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        tests = x[0]
        self.executor._full_coverage = [] # reset the coverage evaluation
        self.executor._coverage = set()

        fitnessList=[]
        tests_used=len(tests)

        for test in tests:
            exceptions, execution_time, coverage = self.executor._execute_input(test)
            
            lines_covered = len(coverage)
            fitness=lines_covered / tests_used
            fitnessList.append(fitness)
            
        maxFitness =max(fitnessList)
        self.execution_data[self.n_evals] = {"input": test, "output": maxFitness, "execution_time": execution_time}

        self.n_evals += 1
        # print(maxFitness)
        self.maxFitnessList.append(maxFitness)
        self.iterationsList=range(len(self.maxFitnessList))
        # print(self.maxFitnessList)
        # print(self.iterationsList)

        out["F"] = -maxFitness

