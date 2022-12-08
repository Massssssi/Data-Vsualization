#This file should randomly generate different values for each of the countries. Make a different function for each question which returns a pandas dataframe in the format you need to plot the graphs for that question.
import random
import numpy as np
import pandas as pd


countries = ['United Kingdom','Ireland','France','Spain','Portugal','Italy','Germany']
time = [2016, 2017, 2018, 2019, 2020]

#plastic consumption in metric tonnes kg 
#Pollution emission in metric tonnes kg (CO2)
def q_6_rng():
    pollution_country = []
    plastic_consumption = []
    pollution_emission = []
    for i in range (7):
        pc_num = random.randrange(100000000,1000000000,1)
        plastic_consumption.append(pc_num)
        pe_num = random.randrange(500000000,11000000000,1)
        pollution_emission.append(pe_num)
        pollution_country.append(countries[i])
    pc = np.asarray(plastic_consumption)
    pe = np.asarray(pollution_emission)
    c = np.asarray(pollution_country)
    df = pd.DataFrame({'Countries': c[:], 'Plastic consumption': pc[:], 'Pollution emmission': pe[:]})
    return df


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


