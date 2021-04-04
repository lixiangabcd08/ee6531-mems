from simulation import Simulation
import numpy as np
from pymoo.model.problem import Problem
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import constants

problem = MESMProblem()
algorithm = NSGA2(
    pop_size=40,
    n_offsprings=10,
    sampling=get_sampling("real_random"),
    crossover=get_crossover("real_sbx", prob=0.9, eta=15),
    mutation=get_mutation("real_pm", eta=20),
    eliminate_duplicates=True
)
termination = get_termination("n_gen", 40)
res = minimize(problem,
               algorithm,
               termination,
               seed=1,
               save_history=True,
               verbose=True)



class MESMProblem(Problem):
    def __init__(self):
        super().__init__(n_var=48,
                    n_obj=3,
                    n_constr=2,
                    xl=np.concatenate((np.full(constants.battery_max_charge,24),np(0,24))),
                    xu=np.concatenate((np.full(constants.battery_max_discharge,24),np(constants.gas_turbine_max,24))),
                    elementwise_evaluation=True)

    def _evaluate(self,x,out,*args,**kwargs):
        battery_powers = []
        gas_turbine_powers = []
        for t in range(24):
            battery_powers.append(x[t])
            gas_turbine_powers.append(x[24+t])
        new_simulation = Simulation()
        new_simulation.simulate(battery_powers,gas_turbine_powers)

        f1 = new_simulation.get_objective_1()
        f2 = new_simulation.get_objective_2()
        f3 = new_simulation.get_objective_3()

        

        out["F"] = [f1, f2, f3]
        out["G"] = [g1, g2]

