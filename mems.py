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
        battery_power = self.battery.get_power(t)
        gas_turbine_power = self.gas_turbine.get_power(t)
        net_load = load_power - (pv_power+wind_power+battery_power+gas_turbine_power)

        if net_load < 0: # excess production
            max_transferable = self.load.get_max_transferable(t)
            # set transferable to the maximum
            load_power += min(max_transferable, -net_load) 
            if -net_load > max_transferable:
                net_load = net_load + max_transferable
                if -net_load < wind_power: # curtail wind first
                    wind_power = wind_power + net_load
                elif -net_load < (wind_power+pv_power): #curtail both wind and 
                    net_load += wind_power
                    wind_power = 0
                    pv_power += net_load
                else: 
                    net_load = net_load + wind_power + pv_power
                    wind_power = 0
                    pv_power = 0
                    if -net_load < gas_turbine_power: # redce gas_turbine
                        gas_turbine_power += net_load
                    else:
                        net_load += gas_turbine_power
                        gas_turbine_power = 0
                        battery_power += net_load 
        else: # shortage of production
            # cut off transferable load
            transferable = self.load.get_transferable(t)
            net_load -= transferable
            load_power -= transferable
            if net_load < (self.battery.max_discharge-battery_power): # oncrease the battery
                battery_power += net_load
            else:
                battery_power = self.battery.max_discharge
                gas_turbine_power += (net_load-self.battery.max_discharge+battery_power)


        self.load.set_load(t,load_power)
        self.pv.set_power(t,pv_power)
        self.wind.set_power(t,wind_power)
        shortage = self.battery.set_power(t,battery_power) # battery cannot charge/discharge so much due to soc limit
        self.gas_turbine.set_power(t,gas_turbine_power+shortage)
        
