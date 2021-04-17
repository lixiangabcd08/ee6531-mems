from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination, get_problem, get_reference_directions
from pymoo.optimize import minimize
import constants
from problem import MESMProblem, MyRepair
from pymoo.visualization.scatter import Scatter
from simulation import Simulation
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


problem = MESMProblem()
algorithm = NSGA2(
    pop_size=1000,
    sampling=get_sampling("real_random"),
    crossover=get_crossover("real_sbx", prob=0.8, eta=15),
    mutation=get_mutation("real_pm", prob=0.05, eta=20),
    eliminate_duplicates=True,
    repair=MyRepair()
)
termination = get_termination("n_gen", 200)
res = minimize(problem,
               algorithm,
               termination,
               seed=1,
               save_history=True,
               verbose=True)

# print(res.pop.get("X")[0])
# select the best one from the solution

solutions = res.pop
fs = np.array(res.F)
selected_solutions = []
for solution in solutions:
    objectives = solution.get("F")
    if objectives[0]<27 and objectives[1]<35 and objectives[2]<20:
        selected_solutions.append(solution)
best_objective = float('inf')
best_solution = None
for solution in selected_solutions:
    objectives = solution.get("F")
    if (objectives[0]+objectives[1]+objectives[2])<best_objective:
        best_objective = objectives[0]+objectives[1]+objectives[2]
        best_solution = solution.get("X")

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(fs[:,0], fs[:,1], fs[:,2], cmap='Greens')
plt.show()


battery_powers = []
gas_turbine_powers = []
for t in range(24):
    battery_powers.append(best_solution[t])
    gas_turbine_powers.append(best_solution[24+t])
new_simulation = Simulation()
new_simulation.simulate(battery_powers,gas_turbine_powers)
print(new_simulation.get_objective_1())
print(new_simulation.get_objective_2())
print(new_simulation.get_objective_3())
new_simulation.plot_power()
