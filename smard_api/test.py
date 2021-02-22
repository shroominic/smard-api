### ModulIDs ###

# power generation 
REALIZED_POWER_GENERATION    = [1001224,1004066,1004067,1004068,1001223,1004069,1004071,1004070,1001226,1001228,1001227,1001225]
INSTALLED_POWER_GENERATION   = [3004072,3004073,3004074,3004075,3004076,3000186,3000188,3000189,3000194,3000198,3000207,3003792]
FORECASTED_POWER_GENERATION  = [2000122, 2000715, 2000125, 2003791, 2000123]

# power consumption
FORECASTED_POWER_CONSUMPTION = [6000411, 6004362]
REALIZED_POWER_CONSUMPTION   = [5000410, 5004359]

# market
WHOLESALE_PRICES             = [8004169,8004170,8000252,8000253,8000251,8000254,8000255,8000256,8000257,8000258,8000259,8000260,8000261,8000262]
COMMERCIAL_FOREIGN_TRADE     = [8004169,8004170,8000252,8000253,8000251,8000254,8000255,8000256,8000257,8000258,8000259,8000260,8000261,8000262]
PHYSICAL_POWER_FLOW          = [31000714,31000140,31000569,31000145,31000574,31000570,31000139,31000568,31000138,31000567,31000146,31000575,31000144,31000573,31000142,31000571,31000143,31000572,31000141]

import smard_api as smard
import pandas as pd
import time 

def last_valid_value(list):
    nnlist = []
    for i in list:
        if(i != "-"):
            nnlist.append(i)
    return float(nnlist[-1])

def getCurrentGreenEnergyPercentage(realized_power_generation):
    erneuerbar = ['Biomasse[MWh]', 'Wasserkraft[MWh]',
       'Wind Offshore[MWh]', 'Wind Onshore[MWh]', 'Photovoltaik[MWh]',
       'Sonstige Erneuerbare[MWh]']
    konventionell = ['Kernenergie[MWh]', 'Braunkohle[MWh]',
       'Steinkohle[MWh]', 'Erdgas[MWh]', 'Pumpspeicher[MWh]',
       'Sonstige Konventionelle[MWh]']
    e_power_gen = 0.0
    k_power_gen = 0.0
    
    for e in erneuerbar:
        e_power_gen = e_power_gen + last_valid_value(realized_power_generation[e])
        
    for k in konventionell:     
        k_power_gen = k_power_gen + last_valid_value(realized_power_generation[k])
        
    return e_power_gen/(e_power_gen + k_power_gen)


modules = REALIZED_POWER_GENERATION

df = smard.requestSmardData(modulIDs=modules, timestamp_from_in_milliseconds = (int(time.time()) * 1000) - (24*3600)*1000)

print(df)

print("\nCurrentGreenEnergyPercentage: " + str(getCurrentGreenEnergyPercentage(df)))