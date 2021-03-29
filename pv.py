class PV:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def forecast(self, forecasts):
        self.forecasts = forecasts
    
    def get_forecast(self, t):
        return self.forecasts[t]