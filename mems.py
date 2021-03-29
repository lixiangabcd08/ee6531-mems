class MEMS:
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
        gas_turbine_power = self.gas_turbine.get_power()
        net_load = load_power - (pv_power+wind_power+battery_power+gas_turbine_power)
        if net_load < 0: # excess production
            if -net_load < wind_power:
                wind_power = wind_power + net_load
            elif -net_load < (wind_power+pv_power):
                wind_power = 0
                pv_power += net_load
            else:
                wind_power = 0
                pv_power = 0
                # set transferrable to the maximum
        else: # shortage of production
            if net_load >= battery_power:
                if self.gas_turbine.get_capacity()+battery_power >= net_load:
                    gas_turbine_power = net_load - battery_power
                else:
                    load_power = net_load - battery_power - gas_turbine_power
            else:
                gas_turbine = 0
        
