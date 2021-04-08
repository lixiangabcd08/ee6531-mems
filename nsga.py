from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination, get_problem, get_reference_directions
from pymoo.optimize import minimize
import constants
from problem import MESMProblem
from pymoo.visualization.scatter import Scatter
from simulation import Simulation


problem = MESMProblem()
algorithm = NSGA2(
    pop_size=40,
    n_offsprings=10,
    sampling=get_sampling("real_random"),
    crossover=get_crossover("real_sbx", prob=0.9, eta=15),
    mutation=get_mutation("real_pm", eta=20),
    eliminate_duplicates=True
)
termination = get_termination("n_gen", 50)
res = minimize(problem,
               algorithm,
               termination,
               seed=1,
               save_history=True,
               verbose=True)

print(res.pop.get("X")[0])
# select the best one from the solution

solution = res.pop.get("X")[0]
battery_powers = []
gas_turbine_powers = []
for t in range(24):
    battery_powers.append(solution[t])
    gas_turbine_powers.append(solution[24+t])
new_simulation = Simulation()
new_simulation.simulate(battery_powers,gas_turbine_powers)
new_simulation.plot_power()