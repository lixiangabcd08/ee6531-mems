class GasTurbine:
    def __init__(self, capacity):
        self.capacity = capacity
        self.powers = []

    def get_power(self, t):
        return self.powers[t]

    def set_powers(self, powers):
        self.powers = powers
    
    def get_capacity(self):
        return self.capacity