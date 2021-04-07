# load
load_important_forecast = [500,100,100,150,200,250,300,400,500,1300,2100,2250,2350,1900,1500,1700,1900,2000,1700,4400,4450,1700,1500,1100]
#                           0   1   2   3   4   5   6   7   8   9    10   11   12   13   14   15   16   17   18   19   20   21   22   23
load_transferable_forecast = [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0]
shortage_cost = 1 

# battery
battery_max_discharge = 159.8
battery_max_charge = -21
battery_capacity = 4*1.887
nbatt = 0.9
nbatt_c = 0.9
nbatt_d = 0.9
battery_cost = 18480
life_time = 10*365*24 # 10 years
round_trip = 0.8
battery_om_cost = 0.00414

# micro-gas turbine
gas_turbine_max = 2000
fual_cost = 1.346
co2_coe = 0.0016
co2_cost = 0.0131
so2_coe = 0.000008
so2_cost = 0.9487
no_coe = 0.00044
no_cost = 3.9904
microgas_turbine_om_cost = 0.00604

# pv
pv_max = 1000
pv_forecast = [0,0,0,0,0,0,0.02,0.075,0.13,0.11,0.15,0.17,0.175,0.155,0.12,0.07,0.05,0.02,0,0,0,0,0,0]
            #  0 1 2 3 4 5   6   7      8   9    10   11    12    13   14   15   16   17
pv_om_cost = 0.00145

# wind
wind_turbine_max = 1650
wind_forecast = [12.2,11.9,12,9.5,11,13.5,12,13,11.5,14,8.9,11.5,12.4,12.4,14,15.2,16.8,16.5,12,10.2,6.3,12,13.5,11.5]
                # 0     1   2  3   4   5   6  7   8   9  10  11    12  13  14   15   16   17 18   19  20 21  22   23
wind_turbine_om_cost = 0.00446

## NSGAII setting
population = 50
cycle = 200
crossover = 0.8
variation = 0.05
