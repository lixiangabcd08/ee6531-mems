from battery import Battery
from gas_turbine import GasTurbine
from load import Load
from pv import PV
from wind_turbine import WindTurbine
from mems import MEMS
import constants
import math
import matplotlib.pyplot as plt

class Simulation:

    def __init__(self):
        self.b = Battery(constants.battery_capacity,constants.battery_max_charge,constants.battery_max_discharge,constants.nbatt,constants.nbatt_c,constants.nbatt_d,\
            constants.battery_cost, constants.life_time, constants.round_trip)
        self.g = GasTurbine(constants.gas_turbine_max, constants.microgas_turbine_om_cost, constants.fual_cost, constants.co2_coe, constants.co2_cost, \
            constants.so2_coe, constants.so2_cost, constants.no_coe, constants.no_cost)
        self.l = Load(constants.shortage_cost)
        self.p = PV(constants.pv_max, constants.pv_om_cost)
        self.w = WindTurbine(constants.wind_turbine_max, constants.wind_turbine_om_cost)
        self.m = MEMS(self.b,self.g,self.l,self.p,self.w)

        self.l.set_forecast(constants.load_important_forecast,constants.load_transferable_forecast)
        self.p.set_forecast([ir/0.2*1000 for ir in constants.pv_forecast])
        self.w.set_forecast([0.2*wind_speed**3 for wind_speed in constants.wind_forecast])


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
                +self.g.get_power(t)*self.g.so2_coe*self.g.so2_cost \
                +self.g.get_power(t)*self.g.no_coe*self.g.no_cost
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
    

    def plot_power(self):
        plt.plot(self.p.powers,label='Solar')
        plt.plot(self.w.powers,label='Wind Turbine')
        plt.plot(self.b.powers,label='Battery')
        plt.plot(self.g.powers,label='Genset')
        plt.plot(self.l.important,label='Load')
        plt.legend()
        plt.show()