import constants
from pymoo.model.problem import Problem
import numpy as np
from simulation import Simulation
from pymoo.model.repair import Repair

class MESMProblem(Problem):
    def __init__(self):
        super().__init__(n_var=48,
                    n_obj=3,
                    xl=np.concatenate((np.full(24,constants.battery_max_charge),np.full(24,0))),
                    xu=np.concatenate((np.full(24,constants.battery_max_discharge),np.full(24,constants.gas_turbine_max))),
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

class MyRepair(Repair):

    def _do(self, problem, pop, **kwargs):
        for k in range(len(pop)):
            x = pop[k].X
            battery_powers = []
            gas_turbine_powers = []
            for t in range(24):
                battery_powers.append(x[t])
                gas_turbine_powers.append(x[24+t])
            new_simulation = Simulation()
            new_simulation.simulate(battery_powers,gas_turbine_powers)
            solution = np.concatenate((np.array(new_simulation.b.powers),np.array(new_simulation.g.powers)))
            x = solution
        return pop