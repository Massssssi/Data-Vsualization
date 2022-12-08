#This file should randomly generate different values for each of the countries. Make a different function for each question which returns a pandas dataframe in the format you need to plot the graphs for that question.
import random
import numpy as np
import pandas as pd


countries = ['United Kingdom','Ireland','France','Spain','Portugal','Italy','Germany']

#plastic consumption in metric tonnes kg 
#Pollution emission in metric tonnes kg (CO2)
def q_6_rng():
    plastic_consumption = []
    pollution_emission = []
    for i in range (7):
        pc_num = random.randrange(1000000,10000000,1)
        plastic_consumption.append(pc_num)
        pe_num = random.randrange(500000000,11000000000,1)
        pollution_emission.append(pe_num)
    pc = np.asarray(plastic_consumption)
    pe = np.asarray(pollution_emission)
    stack = np.vstack((pc,pe))
    df = pd.DataFrame(stack,columns=countries)
    return df

df = q_6_rng()
print(df)
