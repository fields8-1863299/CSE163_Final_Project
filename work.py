from process_files import getDF_A as getDFA
from process_files import getDF_C as getDFC
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
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
    plt.savefig('race.png', bbox_inches='tight')


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
    plt.savefig('sex.png', bbox_inches='tight')


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
    print(df_2017_state['State'])
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
    fig.write_image('states.png')
    fig.write_html("states.html")


def main():
    # Research Question 1
    race(getDFA())
    sex(getDFA())
    # Research Question 4
    df_4 = getDFC()
    df_4 = df_4.drop([0, 1, 2, 3, 5, 6, 7, 9, 20, 31, 42, 53])
    country = pd.read_file('country.csv')
    country = country[(country['State'] != 'Alaska') &
                      (country['State'] != 'Hawaii')]
    state(df_4, country)


if __name__ == '__main__':
    main()