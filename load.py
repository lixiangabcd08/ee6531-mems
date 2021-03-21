class Load:
    def __init__(self):
        self.tranferrable = []
        self.interruptive = []
        self.important = []

    def forecast(self, important_forecast, interruptive_forecast, transferrable_forecast):
        self.important_forecast = important_forecast
        self.interruptive_forecast = interruptive_forecast
        self.transferrable_forecast = transferrable_forecast

    def get_total_forecast(t):
        return self.important_forecast[t]+self.interruptive_forecast[t]+self.transferrable_forecast[t]