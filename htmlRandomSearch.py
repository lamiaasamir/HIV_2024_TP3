import matplotlib.pyplot as plt
from datetime import datetime
from poly_sbst.common.random_seed import get_random_seed
from poly_sbst.common.abstract_executor import AbstractExecutor
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.algorithms.soo.nonconvex.random_search import RandomSearch
from poly_sbst.sampling.abstract_sampling import AbstractSampling
from poly_sbst.crossover.random_crossover import OnePointCrossover
from poly_sbst.problems.test_suite_problem import TestSuiteProblem
from poly_sbst.generators.test_suite_generator import TestSuiteGenerator
from poly_sbst.mutation.test_suite_mutation import TestSuiteMutation
from pymoo.optimize import minimize
from html.parser import HTMLParser
from pymoo.operators.selection.rnd import RandomSelection
from pymoo.algorithms.soo.nonconvex.random_search import RandomSearch

from poly_sbst.generators.htmlSuiteGenerator import HTMLTestSuiteGenerator
from poly_sbst.problems.htmlSuiteProblem import HTMLTestSuiteProblem
from poly_sbst.mutation.html_mutation import HTMLTestSuiteMutation
from poly_sbst.crossover.html_crossover import HTMLTestSuiteCrossover

def optimize(runs=5):
    all_iterations_list = []
    all_max_fitness_list = []

    for run in range(runs):
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y")

        seed = get_random_seed()
        pop_size = 500
        num_gen = 10

        generator = HTMLTestSuiteGenerator() 

        executor = AbstractExecutor(HTMLParser().feed) 
        problem = HTMLTestSuiteProblem(executor) 
        
        method = GA(pop_size=pop_size,
                n_offsprings=int(pop_size/2),
                sampling=AbstractSampling(generator),
                selection=RandomSearch(),
                mutation=HTMLTestSuiteMutation(generator=generator),
                crossover=HTMLTestSuiteCrossover(cross_rate=0.9),
                eliminate_duplicates=False
                )
        
        res = minimize(problem,
                method,
                termination=('n_gen', num_gen),
                seed=seed,
                verbose=True,
                eliminate_duplicates=False,
                save_history=True
                )
        
        print("Best solution found: %s" % res.X)
        print("Function value: %s" % res.F)
        print("Execution data:", res.problem.execution_data)

        all_iterations_list.append(problem.iterationsList)
        all_max_fitness_list.append(problem.maxFitnessList)

    return all_iterations_list, all_max_fitness_list, pop_size, num_gen

plt.figure(1)
# Plotting all runs on the same graph next to each other
all_iterations, all_max_fitness, pop_size, num_gen = optimize()
increment = max(len(iterations) for iterations in all_iterations)
for i, iterations in enumerate(all_iterations):
    x_values = [x + i * increment for x in range(len(iterations))]
    plt.plot(x_values, all_max_fitness[i], linestyle='-', linewidth=0.5, label=f'Run {i+1}')

# Adding labels and title
plt.xlabel('Iterations')
plt.ylabel('Max Fitness')
plt.title(f'Iterations vs Max Fitness for HTML Random Selection for Population size of {pop_size} and Number of Generations of {num_gen}')

# Adding legend
plt.legend()

# Displaying the plot
plt.grid(True)
plt.tight_layout() 
plt.show()

plt.figure(2)
# Plotting all runs on the same graph on top of each other
for i in range(len(all_iterations)):
    plt.plot(all_iterations[i], all_max_fitness[i], linestyle='-', linewidth=0.4, label=f'Run {i+1}')

# Adding labels and title
plt.xlabel('Iterations')
plt.ylabel('Max Fitness')
plt.title(f'Iterations vs Max Fitness for HTML Random Search for Population size of {pop_size} and Number of Generations of {num_gen}')

# Adding legend
plt.legend()

# Displaying the plot
plt.grid(True)
plt.tight_layout() 
plt.show()