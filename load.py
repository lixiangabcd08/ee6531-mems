class Load:
    
    def __init__(self):
        self.tranferrable = []
        self.important = []

    def set_forecast(self, important_forecasts, transferrable_forecasts):
        self.important_forecasts = important_forecasts
        self.transferrable_forecasts = transferrable_forecasts

    def get_total_forecast(self, t):
        return self.important_forecasts[t]+self.transferrable_forecasts[t]

    def set_load(self, t, power):
        if power > self.important[t]:
            self.tranferrable[t] = power - self.important[t]
        else:
            self.tranferrable[t] = 0
            self.important[t] = power


