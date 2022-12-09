from rng import q_6_rng, q_7_rng, q_8_rng, q_9_rng, q_10_rng
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as pltlyexp
import numpy as np
import seaborn as sns
import plotly.figure_factory as ff
from plotly.offline import iplot
import plotly.graph_objs as go

q6_df = q_6_rng()
q8_df = q_8_rng()
q9_df = q_9_rng()
q10_df = q_10_rng()


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
    q7_df_bar = q_7_rng(isBar = True)
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
    q7_df_heat = q_7_rng(isBar = False)
    print(q7_df_heat.to_string())
    q7_df_heat = q7_df_heat.pivot(index='Countries',columns='Year')
    print(q7_df_heat.to_string())
    q7_df_heat.drop(q7_df_heat.tail(1).index,inplace=True)
    q7_df_heat.columns = q7_df_heat.columns.droplevel(0)

    plt.rcParams['font.size'] = '9'

    ax = sns.heatmap(q7_df_heat)

    plt.show()



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
    iplot(chmap)


def plot_bar_q10():
    q10_df.set_index('countries').plot(kind='bar', rot=0, title="Amount of money spent recycling plastic per country (2022)").set_ylabel("Money spent (€)")
    plt.show()
