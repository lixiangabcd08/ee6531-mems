class Battery:
    def __init__(self, capacity, max_charging, max_discharge, nbatt, nbatt_c, nbatt_d):
        self.capacity = capacity
        self.max_charging = max_charging # negative
        self.max_discharge = max_discharge # positive
        self.socs = [] 
        self.socs[0] = 1 # start the simultation with 100% soc
        self.powers = []
        self.nbatt = nbatt # self-discharge effeciency
        self.nbatt_c = nbatt_c # charge efficiency
        self.nbatt_d = nbatt_d # discharge efficienty
    
    def get_power(self,t):
        return self.powers[t]

    def set_powers(self, powers):
        self.powers = powers

    def set_power(self, t, power):
        self.powers[t] = power
        #TODO: calculate soc
        if t > 0:
            if power > 0: # discharge
                self.socs[t] = (1-self.nbatt) - power/self.capacity/self.nbatt_d
            else: # charge
                self.socs[t] = (1-self.nbatt) - power/self.capacity*self.nbatt_c



        


    