import random

class GasTurbine:
    def __init__(self, capacity):
        self.capacity = capacity

    def generate_random_power(self):
        self.power = lib.generate_random(0, self.capacity)
        return self.power

    def get_power(self):
        return self.power