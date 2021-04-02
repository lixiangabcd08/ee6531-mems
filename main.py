from battery import Battery
from gas_turbine import GasTurbine
from load import Load
from pv import PV
from wind_turbine import WindTurbine
from mems import MEMS
from solution import Solution
import constants

def forecast(l,p,w):
    l.forecast(constants.load_important_forecast,constants.load_interruptive_forecast,constants.load_transferrable_forecast)
    p.forecast(constants.pv_forecast)
    w.forecast(constants.wind_forecast)


b = Battery(constants.battery_capacity,constants.battery_max_charge,constants.battery_max_discharge,constants.nbatt,constants.nbatt_c,constants.nbatt_d)
g = GasTurbine(constants.gas_turbine_max)
l = Load()
p = PV(constants.pv_max)
w = WindTurbine(constants.wind_turbine_max)
m = MEMS(b,g,l,p,w)

forecast(l,p,w)
solution = Solution()
solution.generate_random_power(constants.battery_max_charge,constants.battery_max_discharge,constants.gas_turbine_max)
b.set_powers(solution.battery_powers)
g.set_powers(solution.gas_turbine_powers)
for t in range(24): # 24 hours
    m.control(t)