from rng import q_1_rng, q_2_rng, q_3_rng, q_4_rng, q_5_rng, q_6_rng, q_6_rng, q_7_rng, q_8_rng, q_9_rng, q_10_rng
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as pltlyexp
import numpy as np
import seaborn as sns
import plotly.figure_factory as ff
from plotly.offline import iplot
import plotly.offline
import plotly.graph_objs as go
import random

q1_df = q_1_rng()
q2_df = q_2_rng()
q3_df = q_3_rng()
q4_df = q_4_rng()
q5_df = q_5_rng()
q7_df_bar = q_7_rng(isBar = True)
q7_df_heat = q_7_rng(isBar = False)
q6_df = q_6_rng()
q8_df = q_8_rng()
q9_df = q_9_rng()
q10_df = q_10_rng()

def plot_bar_q1():
    ax = q1_df.plot.bar(x="countries", title = 'Plastic pollution of different countries').set_ylabel("Plastic Pollution")
    plt.show()
    
def plot_bar_q2():
    ax = q2_df.plot.bar(x="countries", title = 'Plastic pollution of different countries').set_ylabel("Plastic Pollution")
    plt.show()
    
def plot_bar_q3():
    ax = q3_df.plot.bar(x="countries", title = 'Plastic pollution of different countries').set_ylabel("Plastic Pollution")
    plt.show()

def plot_bar_q4():
    ax = q4_df.plot.bar(x="countries", title = 'Plastic pollution of different countries').set_ylabel("Plastic Pollution")
    plt.show()
    
def plot_bar_q5():
    ax = q5_df.plot.bar(x="countries", stacked = True, title = 'Different types of plastic pollution of different countries').set_ylabel("Plastic Pollution")
    plt.legend = plt.legend(title="Plastic Types",
                   loc='upper right', fontsize='small', fancybox=True)
    plt.show()
    
def plot_choropleth_q1():
    data = dict(type = 'choropleth',
    locations =q10_df['countries'],
    locationmode = 'country names',
    colorscale= 'greens',
    text= q1_df['countries'],
    z=q1_df['PlasticPolution'],
    colorbar = {'title':'Polution produced'})
    layout = dict(geo={'scope':'europe'})
    chmap = go.Figure(data=[data],layout=layout)
    chmap.update_layout(
        title_text = 'Polution produced by western countries'
    )
    chmap.show()

     
def plot_tree_q2():
     sizes = q2_df['PlasticPolution'].values
     labels = q2_df['countries'].values
     fig = pltlyexp.treemap(q2_df, path=[labels], values=sizes, title="Countries which produces most polution")
     fig.show()


def plot_tree_q3():
     sizes = q3_df['PlasticPolution'].values
     labels = q3_df['countries'].values
     fig =pltlyexp.treemap(q3_df, path = [labels],values = sizes, color = q3_df['PlasticPolution'], title="Polution produced by western countries")
     fig.show()


def plot_tree_q4():
     sizes = q4_df['PlasticPolution'].values
     labels = q4_df['countries'].values
     fig = pltlyexp.treemap(q4_df, path=[labels], values=sizes, title="Polution produced by western countries")
     fig.show()

def plot_heat_q5():
  
 
       countries = q5_df['countries']
       Polution_Type = ["PET", "HDPE", "LDPE", "PVC"]

      
       harvest = np.array([q5_df['PET'],
                          q5_df['HDPE'],
                          q5_df['LDPE'],
                          q5_df['PVC']])


       fig, ax = plt.subplots()
       im = ax.imshow(harvest)

        # Show all ticks and label them with the respective list entries
       ax.set_xticks(np.arange(len(countries)), labels=countries)
       ax.set_yticks(np.arange(len(Polution_Type)), labels=Polution_Type)

        # Rotate the tick labels and set their alignment.
       plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
       for i in range(len(Polution_Type)):
            for j in range(len(countries)):
                text = ax.text(j, i, harvest[i, j],
                               ha="center", va="center", color="w")

       ax.set_title("Types of Plastic Polution emmitted ")
       fig.tight_layout()
       plt.show()

      
def plot_bar_q6():
    ax = q6_df.plot.bar(x='Countries', stacked=True, title='Plastic consumption (weight) vs pollution emmission (CO2) for countries in Western Europe').set_ylabel("Metric tonnes (kg)")
    plt.legend = plt.legend(title="Measure",
                   loc='upper right', fontsize='small', fancybox=True)
    plt.show()

def plot_tree_q6():
    sizes = q6_df['Plastic consumption'].values
    labels = q6_df['Countries'].values

    fig = pltlyexp.treemap(q6_df, path = [labels],values = sizes, color = q6_df['Pollution emmission'], title="Plastic consumption shown by size (weight) vs pollution emmission (CO2) for countries in Western Europe")
    fig.show()


def plot_bar_q7():
    my_colors = list((['b', 'r', 'g', 'y', 'm']))
    labels = [2016, 2017, 2018, 2019, 2020]
    q7_df_bar.unstack().plot(kind='bar', stacked=True, color=my_colors)
    plt.xlabel("Country")
    plt.ylabel("Metric tonnes (kg)")
    plt.title("Plastic pollution emmission (CO2) by countries over time")
    plt.legend = plt.legend(labels=labels, title="Year",
                        loc='upper right', fontsize='small', fancybox=True)
    plt.show()


def plot_heat_q7():
    q7_df_heat = q7_df_heat.pivot(index='Countries',columns='Year')
    q7_df_heat.drop(q7_df_heat.tail(1).index,inplace=True)
    q7_df_heat.columns = q7_df_heat.columns.droplevel(0)

    plt.rcParams['font.size'] = '9'

    ax = sns.heatmap(q7_df_heat)

    plt.show()


def plot_bar_q8():
    ax = q8_df.plot.bar(x='Countries', stacked=True, title="Recyclable plastic (%) vs Non-recyclable plastic (%) for countries in Western Europe")
    plt.legend = plt.legend(title="Percentage",
                   loc='upper right', fontsize='small', fancybox=True)
    plt.show()



def plot_tree_q8():
    sizes = q8_df['Recyclable plastic %'].values
    labels = q8_df['Countries'].values

    fig = pltlyexp.treemap(q8_df, path = [labels],values = sizes, color = q8_df['Non-Recyclable plastic %'], title="Recyclable plastic (%) shown by size vs Non-recyclable plastic (%) for countries in Western Europe")
    fig.show()


def plot_bar_q9():
    q9_df.set_index('countries').plot(kind='bar', rot=0, title="Plastic Waste Generated per person (2022)").set_ylabel("Plastic Waste Per Person Per Year (Kg)")
    plt.show()
    

#make user interact with tree
def plot_tree_q9():
    labels = q9_df['countries'].values
    sizes = q9_df['plastic waste per capita'].values
    fig = pltlyexp.treemap(q9_df, path=[labels], values=sizes, title="Plastic Waste Generated per person (2022)")
    fig.show()



def plot_choropleth_q10():
    data = dict(type = 'choropleth',
            locations =q10_df['countries'],
            locationmode = 'country names',
            colorscale= 'greens',
            text= q10_df['countries'],
            z=q10_df['money spent processing plastic'],
            colorbar = {'title':'Amount Spent'})
    layout = dict(geo={'scope':'europe'})
    chmap = go.Figure(data=[data],layout=layout)
    chmap.update_layout(
        title_text = 'Amount of money spent recycling plastic in 2022'
    )
    chmap.show()

#Which country spends the most money recycling plastic?
def plot_bar_q10():
    q10_df.set_index('countries').plot(kind='bar', rot=0, title="Amount of money spent recycling plastic per country (2022)").set_ylabel("Money spent (€)")
    plt.show()

def return_options_q1():
    q1_df_sorted = q1_df
    q1_df_sorted = q1_df_sorted.sort_values(by = ['PlasticPolution'], ascending=False).head(4)
    options = q1_df_sorted['PlasticPolution'].to_list()
    for i in range(len(options)):
        options[i] = [options[i], 0]
    options[0][1] = 1
    random.shuffle(options)
    return options

def return_options_q2():
    q2_df_sorted = q2_df
    q2_df_sorted = q2_df_sorted.sort_values(by = ['PlasticPolution'], ascending=False).head(4)
    options = q2_df_sorted['countries'].to_list()
    for i in range(len(options)):
        options[i] = [options[i], 0]
    options[0][1] = 1
    random.shuffle(options)
    return options

def return_options_q3():
    q3_df_sorted = q3_df
    q3_df_sorted = q3_df_sorted.sort_values(by = ['PlasticPolution'], ascending=True).head(4)
    options = q3_df_sorted['PlasticPolution'].to_list()
    for i in range(len(options)):
        options[i] = [options[i], 0]
    options[0][1] = 1
    random.shuffle(options)
    return options

def return_options_q4():
    q4_df_sorted = q4_df
    q4_df_sorted = q4_df_sorted.sort_values(by = ['PlasticPolution'], ascending=True).head(4)
    options = q4_df_sorted['countries'].to_list()
    for i in range(len(options)):
        options[i] = [options[i], 0]
    options[0][1] = 1
    random.shuffle(options)
    return options

def return_options_q5():
    q5_df_sorted = q5_df
    q5_df_sorted = q5_df_sorted.head(1)
    options = ['PET', 'HDPE', 'LDPE','PVC']
    x = 0
    high = ''
    for i in options:
        if q5_df_sorted[i][0]>x:
            x = q5_df_sorted[i][0]
            high = i
    options2 = []
    options2.append([high, 1])
    for i in options:
        options2.append([i, 0])
    
    options2.remove([high, 0])
    random.shuffle(options2)
    return options2
    



# returns shuffled list of options for q6
def return_options_q6():
    q6_df_sorted = q6_df
    q6_df_sorted['Ratio'] = q6_df['Plastic consumption']/q6_df['Pollution emmission']
    q6_df_sorted = q6_df_sorted.sort_values(by=['Ratio'],ascending=False).head(4)
    options = q6_df_sorted['Countries'].to_list()
    for i in range(len(options)):
        options[i] = [options[i], 0]
    options[0][1] = 1
    random.shuffle(options)
    return options


def return_options_q7():
    q7_df_options = q7_df_bar.groupby('Countries')['Pollution emmission'].sum().reset_index()
    q7_df_options = q7_df_options.sort_values(by='Pollution emmission', ascending=False).head(4)
    options = q7_df_options['Pollution emmission'].to_list()
    for i in range(len(options)):
        options[i] = [options[i], 0]
    options[0][1]=1
    random.shuffle(options)
    return options


#returns shuffled list of options for q8
def return_options_q8():
    q8_df_sorted = q8_df
    q8_df_sorted['Ratio'] = q8_df['Recyclable plastic %']/q8_df['Non-Recyclable plastic %']
    q8_df_sorted = q8_df_sorted.sort_values(by=['Ratio'],ascending=False).head(4)
    options = q8_df_sorted['Countries'].to_list()
    for i in range(len(options)):
        options[i] = [options[i], 0]
    options[0][1] = 1
    random.shuffle(options)
    return options

#returns shuffled list of options for q9
def return_options_q9():
    q9_df_sorted = q9_df.sort_values(by=['plastic waste per capita'], ascending=False).head(4)
    options = q9_df_sorted['countries'].to_list()
    for i in range(len(options)):
        options[i] = [options[i], 0]
    options[0][1] = 1
    random.shuffle(options)
    return options

#returns shuffled list of options for q10
def return_options_q10():
    q10_df_sorted = q10_df.sort_values(by=['money spent processing plastic'], ascending=False).head(4)
    options = q10_df_sorted['countries'].to_list()
    for i in range(len(options)):
        options[i] = [options[i], 0]
    options[0][1] = 1
    random.shuffle(options)
    return options


def display_charts(x,type):
    if x == 1:
        if type == "bar":
            plot_bar_q1()
        else:
            plot_choropleth_q1()
    if x == 2:
        if type == "bar":
            plot_bar_q2()
        else:
            plot_tree_q2()
    if x == 3:
        if type == "bar":
            plot_bar_q3()
        else:
            plot_tree_q3()
    if x == 4:
        if type == "bar":
            plot_bar_q4()
        else:
            plot_tree_q4()
    if x == 5:
        if type == "bar":
            plot_bar_q5()
        else:
            plot_heat_q5()
    if x == 6:
        if type == "bar":
            plot_bar_q6()
        else:
            plot_tree_q6()
    if x == 7:
        if type == "bar":
            plot_bar_q7()
        else:
            plot_heat_q7()
    if x == 8:
        if type == "bar":
            plot_bar_q8()
        else:
            plot_tree_q8()
    if x == 9:
        if type == "bar":
            plot_bar_q9()
        else:
            plot_tree_q9()
    if x == 10:
        if type == "bar":
            plot_bar_q10()
        else:
            plot_choropleth_q10()   



#need to finish this
def return_options(x):
    to_return = []
    if x == 6:
        to_return = return_options_q6()
    if x == 7:
        to_return = return_options_q7()
    if x == 8:
        to_return = return_options_q8()
    if x == 9:
        to_return = return_options_q9()
    if x == 10:
        to_return = return_options_q10()
    return to_return



