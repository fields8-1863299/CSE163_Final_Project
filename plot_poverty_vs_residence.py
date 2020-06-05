"""
Sam Fields
CSE 163 AG

Produces 4 bar plots using dataset A to depict relationship
    between population, poverty, and income based on residence type.
1) "2017 & 2018 Total Population by Residence"
2) "2017 & 2018 Total Population Below Poverty Line by Residence"
3) "2017 & 2018 Percentage of Population Below Poverty Line by Residence"
4) "2017 & 2018 Median Income by Residence"
Writes out plots as png to plots directory
"""

from process_files import getDF_A as getDF
import plotly.graph_objects as go


def getPlotPop(df, categories_pop):
    """
    Plots population versus residence.
    :param df - pandas dataframe with relevant info
    :param categories_pop - list of strings of relevant
        column names in the dataframe.
    :return - plotly bar go plot
    """
    fig_pop = go.Figure(data=[
        go.Bar(name='Inside metropolitan statistical areas', x=categories_pop,
               y=df[df['Category'] == 'Inside metropolitan statistical areas']
               .loc[18, categories_pop].to_numpy()),
        go.Bar(name='Inside principal cities', x=categories_pop,
               y=df[df['Category'] == 'Inside principal cities']
               .loc[19, categories_pop].to_numpy()),
        go.Bar(name='Outside principal cities', x=categories_pop,
               y=df[df['Category'] == 'Outside principal cities']
               .loc[20, categories_pop].to_numpy()),
        go.Bar(name='Outside metropolitan statistical areas', x=categories_pop,
               y=df[df['Category'] == 'Outside metropolitan statistical areas']
               .loc[21, categories_pop].to_numpy())])
    fig_pop.update_layout(barmode='group',
                          title="2017 & 2018 Total Population by Residence",
                          yaxis_title="Population")
    return fig_pop


def getPlotTotPov(df, categories_tot_pov):
    """
    Plots population below poverty line versus residence.
    :param df - pandas dataframe with relevant info
    :param categories_tot_pov - list of strings of relevant
        column names in the dataframe.
    :return - plotly bar go plot
    """
    fig_tot_pov = go.Figure(data=[
        go.Bar(name='Inside metropolitan statistical areas',
               x=categories_tot_pov,
               y=df[df['Category'] == 'Inside metropolitan statistical areas']
               .loc[18, categories_tot_pov].to_numpy()),
        go.Bar(name='Inside principal cities', x=categories_tot_pov,
               y=df[df['Category'] == 'Inside principal cities']
               .loc[19, categories_tot_pov].to_numpy()),
        go.Bar(name='Outside principal cities', x=categories_tot_pov,
               y=df[df['Category'] == 'Outside principal cities']
               .loc[20, categories_tot_pov].to_numpy()),
        go.Bar(name='Outside metropolitan statistical areas',
               x=categories_tot_pov,
               y=df[df['Category'] == 'Outside metropolitan statistical areas']
               .loc[21, categories_tot_pov].to_numpy())])
    fig_tot_pov.update_layout(barmode='group',
                              title="2017 & 2018 Total Population \
                                  Below Poverty Line by Residence",
                              yaxis_title="Population Below Poverty Line")
    return fig_tot_pov


def getPlotPerPov(df, categories_per_pov):
    """
    Plots percentage of population below poverty line versus residence.
    :param df - pandas dataframe with relevant info
    :param categories_per_pov - list of strings of relevant
        column names in the dataframe.
    :return - plotly bar go plot
    """
    fig_per_pov = go.Figure(data=[
        go.Bar(name='Inside metropolitan statistical areas',
               x=categories_per_pov,
               y=df[df['Category'] == 'Inside metropolitan statistical areas']
               .loc[18, categories_per_pov].to_numpy()),
        go.Bar(name='Inside principal cities', x=categories_per_pov,
               y=df[df['Category'] == 'Inside principal cities']
               .loc[19, categories_per_pov].to_numpy()),
        go.Bar(name='Outside principal cities', x=categories_per_pov,
               y=df[df['Category'] == 'Outside principal cities']
               .loc[20, categories_per_pov].to_numpy()),
        go.Bar(name='Outside metropolitan statistical areas',
               x=categories_per_pov,
               y=df[df['Category'] ==
                    'Outside metropolitan statistical areas']
               .loc[21, categories_per_pov].to_numpy())])
    fig_per_pov.update_layout(barmode='group',
                              title="2017 & 2018 Percentage of Population \
                                  Below Poverty Line by Residence",
                              yaxis_title="Percentage")
    return fig_per_pov


def getPlotIncome(df, categories_inc):
    """
    Plots median income versus residence.
    :param df - pandas dataframe with relevant info
    :param categories_inc - list of strings of relevant
        column names in the dataframe.
    :return - plotly bar go plot
    """
    fig_inc = go.Figure(data=[
        go.Bar(name='Inside metropolitan statistical areas', x=categories_inc,
               y=df[df['Category'] == 'Inside metropolitan statistical areas']
               .loc[18, categories_inc].to_numpy()),
        go.Bar(name='Inside principal cities', x=categories_inc,
               y=df[df['Category'] == 'Inside principal cities']
               .loc[19, categories_inc].to_numpy()),
        go.Bar(name='Outside principal cities', x=categories_inc,
               y=df[df['Category'] == 'Outside principal cities']
               .loc[20, categories_inc].to_numpy()),
        go.Bar(name='Outside metropolitan statistical areas', x=categories_inc,
               y=df[df['Category'] ==
                    'Outside metropolitan statistical areas']
               .loc[21, categories_inc].to_numpy())])
    fig_inc.update_layout(barmode='group',
                          title="2017 & 2018 Median Income by Residence",
                          yaxis_title="Income")
    return fig_inc


def main():
    df = getDF()
    df = df[(df['Category'] == 'Inside metropolitan statistical areas') |
            (df['Category'] == 'Inside principal cities') |
            (df['Category'] == 'Inside principal cities') |
            (df['Category'] == 'Outside principal cities') |
            (df['Category'] == 'Outside metropolitan statistical areas')]

    categories_pop = ['2017 Total Population', '2018 Total Population']
    categories_tot_pov = ['2017 Total Below Poverty',
                          '2018 Total Below Poverty']
    categories_per_pov = ['2017 Percentage Below Poverty',
                          '2018 Percentage Below Poverty']
    categories_inc = ['2017 Median Income', '2018 Median Income']

    pop = getPlotPop(df, categories_pop)
    pop.write_image("plots/R2017 & 2018 Total Population by Residence.png")

    tot_pov = getPlotTotPov(df, categories_tot_pov)
    tot_pov.write_image("plots/2017 & 2018 Total Population Below \
            Poverty Line by Residence.png")

    per_pov = getPlotPerPov(df, categories_per_pov)
    per_pov.write_image(
        "plots/2017 & 2018 Percentage of Population Below \
        Poverty Line by Residence.png")

    income = getPlotIncome(df, categories_inc)
    income.write_image("plots/2017 & 2018 Median Income by Residence.png")


if __name__ == '__main__':
    main()
