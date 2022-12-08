from rng import q_9_rng, q_10_rng
import matplotlib.pyplot as plt
import plotly.express as pltlyexp
import pandas as pd
from plotly.offline import iplot
import plotly.graph_objs as go

plt.show()
q9_df = q_9_rng()
q10_df = q_10_rng()


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


