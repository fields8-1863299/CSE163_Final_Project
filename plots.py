"""
Contains methods to produce plots for use in the final project.
Plots use dataframes generated from the process_files.py file.
"""

from process_files import getDF_A as getDFA
from process_files import getDF_B as getDFB
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def race(df):
    """
    Plots a bar chart comparing the poverty percentage for different racial
    groups in the year 2017 and 2018. Each group has two bars, one to
    represent each year.
    """
    df_2017_race = df.loc[0:4, ['Category', '2017 Percentage Below Poverty',
                                '2018 Percentage Below Poverty']]
    df_2017_race.columns = ['Race', '2017', '2018']
    df_2017_race = df_2017_race.drop(1)
    df_2017_race = pd.melt(df_2017_race, id_vars="Race", var_name="Year",
                           value_name="Percent")
    sns.catplot(x='Race', y='Percent', hue='Year',
                data=df_2017_race, kind='bar')
    plt.title('Percentage of Poverty Based on Race')
    plt.xlabel('Race')
    plt.ylabel('Poverty Percentage')
    plt.savefig('plots/race.png', bbox_inches='tight')


def sex(df):
    """
    Plots a bar chart comparing the poverty percentage for different gender
    groups in the year 2017 and 2018. Each group has two bars, one to
    represent each year.
    """
    df_2017_sex = df.loc[5:6, ['Category', '2017 Percentage Below Poverty',
                               '2018 Percentage Below Poverty']]
    df_2017_sex.columns = ['Sex', '2017', '2018']
    df_2017_sex = pd.melt(df_2017_sex, id_vars="Sex", var_name="Year",
                          value_name="Percent")
    sns.catplot(x='Sex', y='Percent', hue='Year', data=df_2017_sex, kind='bar')
    plt.title('Percentage of Poverty Based on Sex')
    plt.xlabel('Sex')
    plt.ylabel('Poverty Percentage')
    plt.savefig('plots/sex.png', bbox_inches='tight')


def state(df, states):
    """
    Creates an image plot map, and an interactive html plot map comparing the
    poverty rates of different states within the US. Each state is colored
    based on a scale indicating its level of poverty.
    """
    df_2017_state = df.loc[5: 64, ['Table with row headings in column A ' +
                                   'and column headings in rows 5 to 10.',
                                   'Unnamed: 5']]
    df_2017_state.columns = ['State', 'Poverty']
    df_2017_state['State'] = df_2017_state['State'].str.replace('.', '')
    df_2017_state['State'] = df_2017_state['State'].str.replace('…', '')
    df_2017_state['Poverty'] = pd.to_numeric(df_2017_state['Poverty'])
    merged = states.merge(df_2017_state, left_on='State', right_on='State')
    fig = go.Figure(data=go.Choropleth(
        locations=merged['Code'],
        z=merged['Poverty'],
        locationmode='USA-states',
        colorscale='Reds',
        colorbar_title="Poverty (%)",
    ))
    fig.update_layout(
        title_text='2017- 2018 US Poverty by State',
        geo_scope='usa',
    )
    fig.write_image('plots/states.png')
    fig.write_html("plots/states.html")


def graph_pov_education(x):
    """"
    This method takes in a parameter x, which is the dataframe for
    dataset A after its been processed.
    This method graphs a double bar graph for the different types of
    education levels compared to
    the number of people in poverty
    The bar graph is for the years 2017-2018 (inclusive).
    Saves bar graph in file called bar_chart_education.png.
    """
    no_dip = x['Category'] == 'No high school diploma'
    high_school = x['Category'] == 'High school, no college'
    college = x['Category'] == 'Some college'
    bach = x['Category'] == "Bachelor's degree or higher"
    pov_education = x[no_dip | high_school | college | bach]
    sns.set()
    pov_education = pov_education.loc[:, ['Category',
                                      '2017 Total Below Poverty',
                                          '2018 Total Below Poverty']]
    pov_education = pd.melt(pov_education, id_vars="Category",
                            var_name="Year", value_name="Poverty")
    sns.catplot(x='Category', y='Poverty',
                hue='Year', data=pov_education, kind='bar')
    plt.xlabel('Education')
    plt.xticks(rotation=-75)
    plt.ylabel('Poverty')
    plt.title('Number of people in Poverty By  Education in 2017  and 2018')
    plt.savefig('plots/bar_chart_education.png', bbox_inches='tight')


def graph_pov_work(x):
    """"
    This method takes in a parameter x, which is the dataframe for
    dataset A after its been processed.
    This method graphs a double bar graph for the different
    work experiences compared to
    the number of people in poverty
    The bar graph is for the years 2017-2018 (inclusive).
    Saves bar graph in file called bar_chart_work.png.
    """
    full_time = x['Category'] == 'Worked full-time, year-round'
    less_full_time = x['Category'] == 'Less than full-time, year-round'
    no_work = x['Category'] == 'Did not work at least 1 week'
    pov_work = x[full_time | less_full_time | no_work]
    pov_work = pov_work.loc[:, ['Category', '2017 Total Below Poverty',
                                '2018 Total Below Poverty']]
    pov_work = pd.melt(pov_work, id_vars="Category", var_name="Year",
                       value_name="Poverty")
    sns.set()
    sns.catplot(x='Category', y='Poverty', hue='Year',
                data=pov_work, kind='bar')
    plt.xlabel('Work Experience')
    plt.xticks(rotation=-75)
    plt.ylabel('People in Poverty')
    plt.title('Number of people in Poverty By Work Experience in'
              '2017 and 2018')
    plt.savefig('plots/bar_chart_work.png', bbox_inches='tight')


def graph_degree_race(b):
    """"
    This method takes in a parameter b, which is the dataframe for
    dataset B after its been processed.
    This method plots 5 bar graphs (each of a degree) comparing different races
    to the amount of people who have received the degree.
    The bar graph is for the years 2016-2017 (inclusive).
    """
    b = b.loc[:, ['Degree', 'Num White', 'Num Black', 'Num Hispanic',
                  'Num Asian/Pacific Islander',
                  'Num American Indian/ Alaskan native']]
    b = pd.melt(b, id_vars="Degree", var_name="Race",
                value_name="Number of People")
    b["Number of People"] = b["Number of People"].str.replace(",", "")
    b['Number of People'] = b['Number of People'].astype(float)
    # below associates
    deg_below_associates = b[b['Degree'] == 'Below_Associates']
    sns.set()
    sns.catplot(x='Race', y='Number of People',
                data=deg_below_associates, kind='bar')
    plt.xlabel('Race')
    plt.xticks(rotation=-75)
    plt.ylabel("People with Degree")
    plt.title("Number of people below Associate's Degree"
              "According to Race in 2016 - 2017")
    plt.savefig('plots/Below_Associates.png', bbox_inches='tight')
    # associates
    deg_associates = b[b['Degree'] == 'Associates']
    sns.set()
    sns.catplot(x='Race', y='Number of People', data=deg_associates,
                kind='bar')
    plt.xlabel('Race')
    plt.xticks(rotation=-75)
    plt.ylabel("People with Degree")
    plt.title("Number of people with Associate's Degree According"
              "to Race in 2016 - 2017")
    plt.savefig('plots/associates.png', bbox_inches='tight')
    #  Bachelors
    deg_bachelors = b[b['Degree'] == 'Bachelors']
    sns.set()
    sns.catplot(x='Race', y='Number of People', data=deg_bachelors,
                kind='bar')
    plt.xlabel('Race')
    plt.xticks(rotation=-75)
    plt.ylabel("People with Degree")
    plt.title("Number of people with Bachelors's Degree According"
              "to Race in 2016 - 2017")
    plt.savefig('plots/bachelors.png', bbox_inches='tight')
    # Masters
    deg_masters = b[b['Degree'] == 'Masters']
    sns.set()
    sns.catplot(x='Race', y='Number of People', data=deg_masters,
                kind='bar')
    plt.xlabel('Race')
    plt.xticks(rotation=-75)
    plt.ylabel("People with Degree")
    plt.title("Number of people with Masters Degree According"
              "to Race in 2016 - 2017")
    plt.savefig('plots/masters.png', bbox_inches='tight')
    # Doctors
    deg_doctors = b[b['Degree'] == 'Doctors']
    sns.set()
    sns.catplot(x='Race', y='Number of People', data=deg_doctors,
                kind='bar')
    plt.xlabel('Race')
    plt.xticks(rotation=-75)
    plt.ylabel("People with Degree")
    plt.title("Number of people with Doctors Degree According"
              "to Race in 2016 - 2017")
    plt.savefig('plots/doctors.png', bbox_inches='tight')


def graph_household_income(x):
    """"
    This method takes in a parameter x, which is the dataframe for
    dataset A after its been processed.
    This method plots 2 double bar graphs, with one graph about
    different types of family households and their income and
    the other about different types
    of non-family households and their incom.
    The bar graph is for the years 2017-2018 (inclusive).
    Saves bar graphs in files called fam_household_income.png and
    non_fam_household_income.png"""

    # 36, 37, 38, 42, 43 is total number of rows
    # for family
    income_fam = x.loc[[36, 37, 38], ['Category', '2017 Median Income',
                                      '2018 Median Income']]
    sns.set()
    income_fam = pd.melt(income_fam, id_vars="Category", var_name="Year",
                         value_name="Money")
    sns.catplot(x='Category', y="Money", hue='Year', data=income_fam,
                kind='bar')
    plt.xlabel('Types of Family Household')
    plt.xticks(rotation=-75)
    plt.ylabel('Median Income')
    plt.title('Median Income for Family Households in 2017  and 2018')
    plt.savefig('plots/fam_household_income.png', bbox_inches='tight')
    # for non family
    income_non = x.loc[[42, 43], ['Category', '2017 Median Income',
                                  '2018 Median Income']]
    income_non = pd.melt(income_non, id_vars="Category", var_name="Year",
                         value_name="Money")
    sns.catplot(x='Category', y="Money", hue='Year', data=income_non,
                kind='bar')
    plt.xlabel('Types of Non-Family Household')
    plt.xticks(rotation=-75)
    plt.ylabel('Median Income')
    plt.title('Median Income for Non-Family Households in 2017  and 2018')
    plt.savefig('plots/non_fam_household_income.png', bbox_inches='tight')


def graph_race_income(x):
    """"
    This method takes in a parameter x, which is the dataframe
    dataset A after its been processed.
    This method plots a double bar graph about the different
    races and their income.
    The bar graph is for the years 2017-2018 (inclusive).
    Saves bar graphs in files called ncome_race.png
    """
    white = x['Category'] == 'White'
    white_n_hisp = x['Category'] == 'White, not Hispanic'
    black = x['Category'] == 'Black'
    asian = x['Category'] == 'Asian'
    hisp = x['Category'] == 'Hispanic (any race)'
    race_inc = x[white | white_n_hisp | black | asian | hisp]
    race_inc = race_inc.loc[:, ['Category', '2017 Median Income',
                                '2018 Median Income']]
    sns.set()
    race_inc = pd.melt(race_inc, id_vars="Category", var_name="Year",
                       value_name="Income")
    sns.catplot(x='Category', y='Income', hue='Year', data=race_inc,
                kind='bar')
    plt.xlabel('Race')
    plt.xticks(rotation=-75)
    plt.ylabel('Income')
    plt.title('Median Income by Race in 2017  and 2018')
    plt.savefig('plots/income_race.png', bbox_inches='tight')


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
    # ishitas plots
    x = getDFA()
    b = getDFB()
    graph_pov_education(x)  # graph 1
    graph_pov_work(x)  # graph 2
    graph_degree_race(b)  # graph 3 (of degrees)
    graph_household_income(x)  # graph 4
    graph_race_income(x)  # graph 5

    # vinnay plots
    # Research Question 1
    race(getDFA())
    sex(getDFA())
    # Research Question 4
    df_4 = pd.read_csv("cse 163 datasets/C/state_csv.csv")
    df_4 = df_4.drop([0, 1, 2, 3, 5, 6, 7, 9, 20, 31, 42, 53])
    country = pd.read_csv('cse 163 datasets/country.csv')
    country = country[(country['State'] != 'Alaska') &
                      (country['State'] != 'Hawaii')]
    state(df_4, country)

    # For getting poverty vs residence plots
    df = getDFA()

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
