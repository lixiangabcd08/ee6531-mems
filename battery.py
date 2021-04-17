class Battery:
    def __init__(self, capacity, max_charging, max_discharge, nbatt, nbatt_c, nbatt_d, cost, life_time, round_trip):
        self.capacity = capacity
        self.max_charging = max_charging # negative
        self.max_discharge = max_discharge # positive
        self.socs = [None]*25
        self.socs[0] = 1 # start the simultation with 100% soc
        self.powers = [None]*24
        self.nbatt = nbatt # self-discharge effeciency
        self.nbatt_c = nbatt_c # charge efficiency
        self.nbatt_d = nbatt_d # discharge efficienty
        self.cost = cost # battey cost
        self.life_time = life_time # battery life time interm of hours
        self.round_trip = round_trip
    
    def get_power(self,t):
        return self.powers[t]

    def set_powers(self, powers):
        self.powers = powers

    def set_power(self, t, power):
        self.powers[t] = power
        if power > 0: # discharge
            self.socs[t+1] = self.socs[t]*self.nbatt - power/self.capacity/self.nbatt_d
        else: # charge
            self.socs[t+1] = self.socs[t]*self.nbatt - power/self.capacity*self.nbatt_c
        if self.socs[t+1] < 0: # discharge in the current run
            self.socs[t+1] = 0
            self.powers[t] = self.socs[t]*self.nbatt*self.capacity*self.nbatt_d # max discharge
            return power - self.powers[t]
        elif self.socs[t+1] > 1: # charge in the current run
            self.socs[t+1] = 1
            self.powers[t] = (self.socs[t]*self.nbatt-1)*self.capacity/self.nbatt_c # max charge
            return self.powers[t] - power
        else:
            return 0

    def get_soc(self, t):
        return self.socs[t]

    def get_max_discharge(self):
        return self.max_discharge

    def get_max_charging(self):
        return self.max_charging


        


    