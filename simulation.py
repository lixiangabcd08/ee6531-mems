from battery import Battery
from gas_turbine import GasTurbine
from load import Load
from pv import PV
from wind_turbine import WindTurbine
from mems import MEMS
from solution import Solution
import constants

class Simulation:

    def __init__(self):
        self.b = Battery(constants.battery_capacity,constants.battery_max_charge,constants.battery_max_discharge,constants.nbatt,constants.nbatt_c,constants.nbatt_d)
        self.g = GasTurbine(constants.gas_turbine_max)
        self.l = Load()
        self.p = PV(constants.pv_max)
        self.w = WindTurbine(constants.wind_turbine_max)
        self.m = MEMS(b,g,l,p,w)

        self.l.forecast(constants.load_important_forecast,constants.load_interruptive_forecast,constants.load_transferable_forecast)
        self.p.forecast(constants.pv_forecast)
        self.w.forecast(constants.wind_forecast)


    def simulate(self, battery_powers, gas_turbine_powers):
        self.b.set_powers(battery_powers)
        self.g.set_powers(gas_turbine_powers)
        for t in range(24): # 24 hours
            self.m.control(t)

    # cost
    def get_objective_1(self):
        total_cost = 0
        for t in range(24):
            # maintenance cost
            om_cost = self.w.maintenance_factor*self.w.get_power(t)+self.p.maintenance_factor*self.p.get_power(t)\
                +self.g.maintenance_factor*self.g.get_power(t)
            fual = self.g.fual_cost*self.g.get_power(t)
            battery_cost = self.b.cost/self.b.life_time/math.sqrt(self.b.round_trip)
            load_cost = self.l.shortage_cost*self.l.get_shortage(t)
            total_cost = total_cost + om_cost + fual + battery_cost + load_cost
        return total_cost

    # pollution
    def get_objective_2(self):
        pollution_cost = 0
        for t in range(24):
            hourly_cost = self.g.get_power(t)*self.g.co2_coe*self.g.co2_cost \
                +self.g.get_power(t)*self.so2_coe*self.so2_cost \
                +self.g.get_power(t)*self.no_coe*self.no_cost
            pollution_cost += hourly_cost
        return pollution_cost

    # over production
    def get_objective_3(self):
        waste = 0
        demand = 0
        for t in range(24):
            waste = waste+self.p.get_power(t)+self.w.get_power(t)+self.g.get_power(t)\
                +self.b.get_power(t)-self.l.get_load(t)
            demand = demand + self.l.get_load(t)
        return waste/demand

    def is_constraint_1(self): # soc is within 0 and 100
        for t in range(24):
            if self.b.socs[t] < 0 or self.b.socs > 1:
                return 1 # infeasible
        return 0 # feasible
    
    def is_constraint_2(self): # 
        expect_load = 0
        actual_load = 0
        for t in range(24):
            expect_load += self.l.get_total_forecast(t)
            actual_load += self.l.get_total_forecast(t)
        if expect_load > actual_load:
            return 1 # infeasible
        else: 
            return 0 #feasible