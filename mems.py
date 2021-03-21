class MESM:
    def __init__(self, battery, gas_turbine, load, pv, wind_turbine):
        self.battery = battery
        self.gas_turbine = gas_turbine
        self.load = load
        self.pv = pv
        self.wind = wind_turbine
    
    def control(self, t):
        load_power = self.load.get_total_forecast(t)
        pv_power = self.pv.get_forecast(t)
        wind_power = self.wind.get_forecast(t)
        battery_power = self.battery.get_power()
        gas_turbine = self.gas_turbine.get_power()
        net_load = load_power - (pv_power+wind_power+battery_power+gas_turbine)
        if net_load < 0: # excess production
            if -net_load < wind_power:
                wind_power = wind_power + net_load