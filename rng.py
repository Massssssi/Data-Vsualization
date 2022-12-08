#This file should randomly generate different values for each of the countries. Make a different function for each question which returns a pandas dataframe in the format you need to plot the graphs for that question.
import random
import numpy as np
import pandas as pd


countries = ['United Kingdom','Ireland','France','Spain','Portugal','Italy','Germany']
time = [2016, 2017, 2018, 2019, 2020]

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
#print(df)

def q_7_rng():
    pollution_country = []
    pollution_emission = []
    pollution_year=[]
    for i in range (7):
        for j in range(len(time)):
            pe_num = random.randrange(500000000,11000000000,1)
            pollution_year.append(time[j])
            pollution_country.append(countries[i])
            pollution_emission.append(pe_num)
    timearr = np.asarray(pollution_year)
    countryarr = np.asarray(pollution_country)
    pe = np.asarray(pollution_emission)
    df = pd.DataFrame({'Countries': countryarr[:], 'Year': timearr[:], 'Pollution emmission': pe[:]})
    df = df.set_index('Countries', append=True).swaplevel(1,0).sort_index(level=0)
    return df

df7 = q_7_rng()
#print(df7.to_string())


def q_8_rng():
    pollution_country = []
    percentage_recyclable = []
    percentage_nonrecyclable = []
    for i in range (7):
        per_rec = random.randrange(0,100,1)
        percentage_recyclable.append(per_rec)
        pollution_country.append(countries[i])
        percentage_nonrecyclable.append(100-per_rec)
    rec_arr = np.asarray(percentage_recyclable)
    countryarr = np.asarray(pollution_country)
    nrec_arr = np.asarray(percentage_nonrecyclable)
    df = pd.DataFrame({'Countries': countryarr[:], 'Recyclable plastic %': rec_arr[:], 'Non-Recyclable plastic %': nrec_arr[:]})
    df = df.set_index('Countries', append=True).swaplevel(1,0).sort_index(level=0)
    return df

df8 = q_8_rng()
print(df8.to_string())


