from battery import Battery
from gas_turbine import GasTurbine
from load import Load
from pv import PV
from wind_turbine import WindTurbine
from mems import MEMS
import constants

def forecast(l,p,w):
    l.forecast(constants.load_important_forecast,constants.load_interruptive_forecast,constants.load_transferrable_forecast)
    p.forecast(constants.pv_forecast)
    w.forecast(constants.wind_forecast)


b = Battery(constants.battery_max_charge,constants.battery_max_discharge)
g = GasTurbine(constants.gas_turbine_max)
l = Load()
p = PV(constants.pv_max)
w = WindTurbine(constants.wind_turbine_max)
m = MEMS(b,g,l,p,w)

forecast(l,p,w)
for t in range(24): # 24 hours
    b.generate_random_power()
    g.generate_random_power()
    m.control(t)