from process_files import getDF_A as getDF
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def main():
    df = getDF()
    df = df[(df['Category'] == 'Inside metropolitan statistical areas') | (df['Category'] == 'Inside principal cities') |
            (df['Category'] == 'Inside principal cities') | (df['Category'] == 'Outside principal cities') |
            (df['Category'] == 'Outside metropolitan statistical areas')]

    categories_pop = ['2017 Total Population', '2018 Total Population']
    categories_tot_pov = ['2017 Total Below Poverty', '2018 Total Below Poverty']
    categories_per_pov = ['2017 Percentage Below Poverty', '2018 Percentage Below Poverty']
    categories_inc = ['2017 Median Income', '2018 Median Income']

    fig_pop = go.Figure(data=[
        go.Bar(name='Inside metropolitan statistical areas', x=categories_pop,
          y=df[df['Category'] == 'Inside metropolitan statistical areas']\
               .loc[18, categories_pop].to_numpy()),
        go.Bar(name='Inside principal cities', x=categories_pop,
            y=df[df['Category'] == 'Inside principal cities'] \
               .loc[19, categories_pop].to_numpy()),
        go.Bar(name='Outside principal cities', x=categories_pop,
            y=df[df['Category'] == 'Outside principal cities'] \
               .loc[20, categories_pop].to_numpy()),
        go.Bar(name='Outside metropolitan statistical areas', x=categories_pop,
            y=df[df['Category'] == 'Outside metropolitan statistical areas'] \
               .loc[21, categories_pop].to_numpy())])
    fig_pop.update_layout(barmode='group',
                          title="2017 & 2018 Total Population by Residence",
                          yaxis_title="Population")
    fig_pop.write_image("plots/R2017 & 2018 Total Population by Residence.png")

    fig_tot_pov = go.Figure(data=[
        go.Bar(name='Inside metropolitan statistical areas', x=categories_tot_pov,
               y=df[df['Category'] == 'Inside metropolitan statistical areas'] \
               .loc[18, categories_tot_pov].to_numpy()),
        go.Bar(name='Inside principal cities', x=categories_tot_pov,
               y=df[df['Category'] == 'Inside principal cities'] \
               .loc[19, categories_tot_pov].to_numpy()),
        go.Bar(name='Outside principal cities', x=categories_tot_pov,
               y=df[df['Category'] == 'Outside principal cities'] \
               .loc[20, categories_tot_pov].to_numpy()),
        go.Bar(name='Outside metropolitan statistical areas', x=categories_tot_pov,
               y=df[df['Category'] == 'Outside metropolitan statistical areas'] \
               .loc[21, categories_tot_pov].to_numpy())])
    fig_tot_pov.update_layout(barmode='group',
                          title="2017 & 2018 Total Population Blow Poverty Line by Residence",
                          yaxis_title="Population Below Poverty Line")
    fig_tot_pov.write_image("plots/2017 & 2018 Total Population Blow Poverty Line by Residence.png")

    fig_per_pov = go.Figure(data=[
        go.Bar(name='Inside metropolitan statistical areas', x=categories_per_pov,
               y=df[df['Category'] == 'Inside metropolitan statistical areas'] \
               .loc[18, categories_per_pov].to_numpy()),
        go.Bar(name='Inside principal cities', x=categories_per_pov,
               y=df[df['Category'] == 'Inside principal cities'] \
               .loc[19, categories_per_pov].to_numpy()),
        go.Bar(name='Outside principal cities', x=categories_per_pov,
               y=df[df['Category'] == 'Outside principal cities'] \
               .loc[20, categories_per_pov].to_numpy()),
        go.Bar(name='Outside metropolitan statistical areas', x=categories_per_pov,
               y=df[df['Category'] == 'Outside metropolitan statistical areas'] \
               .loc[21, categories_per_pov].to_numpy())])
    fig_per_pov.update_layout(barmode='group',
                          title="2017 & 2018 Percentage of Population Blow Poverty Line by Residence",
                          yaxis_title="Percentage")
    fig_per_pov.write_image("plots/2017 & 2018 Percentage of Population Blow Poverty Line by Residence.png")

    fig_inc = go.Figure(data=[
        go.Bar(name='Inside metropolitan statistical areas', x=categories_inc,
               y=df[df['Category'] == 'Inside metropolitan statistical areas'] \
               .loc[18, categories_inc].to_numpy()),
        go.Bar(name='Inside principal cities', x=categories_inc,
               y=df[df['Category'] == 'Inside principal cities'] \
               .loc[19, categories_inc].to_numpy()),
        go.Bar(name='Outside principal cities', x=categories_inc,
               y=df[df['Category'] == 'Outside principal cities'] \
               .loc[20, categories_inc].to_numpy()),
        go.Bar(name='Outside metropolitan statistical areas', x=categories_inc,
               y=df[df['Category'] == 'Outside metropolitan statistical areas'] \
               .loc[21, categories_inc].to_numpy())])
    fig_inc.update_layout(barmode='group',
                          title="2017 & 2018 Median Income by Residence",
                          yaxis_title="Income")
    fig_inc.write_image("plots/2017 & 2018 Median Income by Residence.png")

if __name__ == '__main__':
    main()