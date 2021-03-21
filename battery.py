import lib

class Battery:
    def __init__(self, max_charging, max_discharge):
        self.max_charging = max_charging # negative
        self.max_discharge = max_discharge # positive
        self.soc = 1 # start the simultation with 100% soc
    
    def generate_random_power(self):
        self.power = lib.generate_random(self.max_charging, self.max_discharge)
        return self.power
    
    def get_power(self):
        return self.power
        


    