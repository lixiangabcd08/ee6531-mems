class Load:
    
    def __init__(self, shortage_cost):
        self.transferable = []
        self.important = []
        self.shortage_cost = shortage_cost

    def set_forecast(self, important_forecasts, transferable_forecasts):
        self.important_forecasts = important_forecasts
        self.transferable_forecasts = transferable_forecasts

    def get_total_forecast(self, t):
        return self.important_forecasts[t]+self.transferable_forecasts[t]

    def set_load(self, t, power):
        if power > self.important_forecasts[t]:
            self.transferable.append(power - self.important_forecasts[t])
            self.important.append(self.important_forecasts[t])
        else:
            self.transferable.append(0)
            self.important.append(power)

    def get_shortage(self,t):
        return self.important[t]-self.important_forecasts[t]

    def get_load(self, t):
        return self.important[t]+self.transferable[t]

    def get_max_transferable(self,t):
        return sum(self.transferable_forecasts)-sum(self.transferable)-self.transferable_forecasts[t]



