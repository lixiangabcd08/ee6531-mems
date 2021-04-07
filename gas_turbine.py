class GasTurbine:
    def __init__(self,capacity,maintenance_factor,fual_cost,co2_coe,co2_cost,so2_coe,so2_cost,no_coe,no_cost):
        self.capacity = capacity
        self.powers = [None]*24
        self.maintenance_factor = maintenance_factor
        self.fual_cost = fual_cost
        self.co2_coe = co2_coe
        self.co2_cost = co2_cost
        self.so2_coe = so2_coe
        self.so2_cost = so2_cost
        self.no_coe = no_coe
        self.no_cost = no_cost

    def get_power(self, t):
        return self.powers[t]

    def set_powers(self, powers):
        self.powers = powers

    def set_power(self, t, power):
        self.powers[t] = power
    
    def get_capacity(self):
        return self.capacity