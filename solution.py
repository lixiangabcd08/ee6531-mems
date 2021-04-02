import lib

class Solution:
    def __init__(self):
        self.battery_powers = []
        self.gas_turbine_powers = []
        self.objective_1 = 0
        self.objective_2 = 0
        self.objective_3 = 0

    def generate_random_power(self, battery_max_charge, battery_max_discharge, gas_turbine_max):
        for t in range(24): # 24 hours
            self.battery_powers[t] = lib.generate_random(battery_max_charge, battery_max_discharge)

        for t in range(24): # 24 hours
            self.gas_turbine_powers[t] = lib.generate_random(0, gas_turbine_max)

    def mutation(self, parent_1, parent2):
        pass

    def calc_objectives(self):
        pass
        