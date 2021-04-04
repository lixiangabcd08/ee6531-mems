class PV:
    def __init__(self, capacity, maintenance_factor):
        self.capacity = capacity
        self.powers = []
        self.maintenance_factor = maintenance_factor
    
    def forecast(self, forecasts):
        self.forecasts = forecasts
    
    def get_forecast(self, t):
        return self.forecasts[t]

    def set_power(self, t, power):
        self.powers[t] = power

    def get_power(self, t):
        return self.powers[t]