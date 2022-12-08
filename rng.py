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







#Plastic waste generation per person for every country per year (KG per year)
def q_9_rng():
    columns = ['countries','plastic waste per capita']
    plastic_waste_per_person = []
    for i in range(7):
        pwg_num = random.randrange(20,110,1)
        row = [countries[i],pwg_num]
        plastic_waste_per_person.append(row)
    df_q9 = pd.DataFrame(plastic_waste_per_person, columns=columns)
    return df_q9
    
def q_10_rng():
    columns = ['countries','money spent processing plastic']
    plastic_money = []
    for i in range(7):
        mpc_num = random.randrange(500000000,5000000000,1)
        row = [countries[i], mpc_num]
        plastic_money.append(row)
    df_q10 = pd.DataFrame(plastic_money, columns=columns)
    return df_q10

