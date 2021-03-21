def WindTurbine:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def forecast(self, forecast):
        self.forecast = forecast
    
    def get_forecast(self, t):
        return self.forecast[t]
