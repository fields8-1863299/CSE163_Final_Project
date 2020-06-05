"""
Sam Fields
CSE 163 AG

Contains methods to produce datasets for use in the final project.
Each dataset is created by importing a csv file, cleaning the file,
    and sometimes combining with other files based on similar row
    or column data.
"""

import pandas as pd
import re


def getDF_A():
    """
    Produces dataset A. Dataset A contains 2017 and 2018
        poverty and income data based on categories such as
        citizenship, ethnicity, residence, etc. based on
        3 different csv files.
    :return - pandas dataframe
    """
    d1 = pd.read_csv("cse 163 datasets/A/ds1.csv")
    d2 = pd.read_csv("cse 163 datasets/A/ds2.csv")
    d5 = pd.read_csv("cse 163 datasets/A/ds5.csv")

    d1 = d1.loc[12:62, :]
    d1.columns = ['Category', '2017 Total Population',
                  '2017 Total Below Poverty', 'drop',
                  '2017 Percentage Below Poverty',
                  'drop', '2018 Total Population', '2018 Total Below Poverty',
                  'drop', '2018 Percentage Below Poverty',
                  'drop', 'drop', 'drop']
    d1 = d1.loc[:, d1.columns != 'drop']
    d1 = d1.dropna()

    d2 = d2.loc[9:12, :]
    d2.columns = ['Category', '2017 Total Population',
                  '2017 Total Below Poverty', 'drop',
                  '2017 Percentage Below Poverty',
                  'drop', '2018 Total Population', '2018 Total Below Poverty',
                  'drop', '2018 Percentage Below Poverty',
                  'drop', 'drop', 'drop', 'drop']
    d2 = d2.loc[:, d2.columns != 'drop']
    d2 = d2.dropna()
    d2["Category"].replace({"Primary Families4…………………………………":
                            "Primary Families"}, inplace=True)

    d5 = d5.loc[6:43, :]
    d5.columns = ['Category', '2017 Number People', '2017 Median Income',
                  'drop', '2018 Number People',
                  '2018 Median Income', 'drop', 'drop', 'drop',
                  'drop', 'drop', 'drop', 'drop', 'drop', 'drop',
                  'drop', 'drop', 'drop', 'drop', 'drop', 'drop',
                  'drop', 'drop', 'drop', 'drop', 'drop', 'drop',
                  'drop', 'drop', 'drop', 'drop', 'drop', 'drop',
                  'drop', 'drop', 'drop', 'drop', 'drop']
    d5 = d5.loc[:, d5.columns != 'drop']
    d5 = d5.dropna()
    d5['Category'].replace({".  Married-couple": "Married-couple",
                            ".  Female householder, no spouse present":
                                "Female householder, no spouse present",
                            ".  Male householder, no spouse present":
                                "Male householder, no spouse present",
                            "   White, not Hispanic": "White, not Hispanic",
                            ".. Naturalized citizen": "Naturalized citizen",
                            ".. Not a citizen": "Not a citizen",
                            ".. Inside principal cities":
                                "Inside principal cities",
                            ".. Outside principal cities":
                                "Outside principal cities",
                            "Under 65 years": "Aged Under 65",
                            "65 years and older": "Aged Over 65"
                            }, inplace=True)

    frames = [d1, d2]
    df = pd.concat(frames)

    df = df.merge(d5, left_on='Category', right_on='Category', how='outer')

    columns = ['2017 Total Population', '2017 Total Below Poverty',
               '2018 Total Population', '2018 Total Below Poverty',
               '2017 Number People', '2017 Median Income',
               '2018 Number People', '2018 Median Income']

    for col in columns:
        df[col] = df[col].apply(lambda x: re.sub('[^A-Za-z0-9]+', '', str(x)))

    return df


def getDF_B():
    """
    Produces dataset B. Dataset A contains 2017 - 2018
        statistics of rewarded degree types (bachelors,
        masters etc) based on ethnicity. Pulls information
        from a number of different csv files.
    :return - pandas dataframe
    """
    associates = getDegree("Associates", 26)
    below_associates = getDegree("Below_Associates", 25)
    bachelors = getDegree("Bachelors", 26)
    masters = getDegree("Masters", 26)
    doctors = getDegree("Doctors", 26)
    frames = [below_associates, associates, bachelors, masters, doctors]
    df = pd.concat(frames)
    return df


def getDegree(degree, ind):
    """
    Helper function for getDF_B. Cleans and returns dataframe
        for a singular specific degree type.
    :param degree - String of degree type
    :param ind - Integer of index to start parsing from
    :return - pandas dataframe of singular degree type
    """
    df = pd.read_csv("cse 163 datasets/B/" + degree + "_csv.csv")
    df = df.loc[[ind], :]
    df.columns = ['Degree', 'Num Total', 'Num White',
                  'Num Black', 'Num Hispanic',
                  'Num Asian/Pacific Islander',
                  'Num American Indian/ Alaskan native', 'Num Two or More',
                  'Num Non Resident', 'Perc Total',
                  'Perc White', 'Perc Black', 'Perc Hispanic',
                  'Perc Asian/Pacific Islander',
                  'Perc American Indian/ Alaskan native', 'Perc Two or More']
    df['Degree'] = degree
    return df


def getDF_C():
    """
    Produces dataset C. Dataset C contains 2017 - 2018
        statistics of Percentage of population below
        poverty line by state in the united states.
    Pulls data from singular csv file
        "cse 163 datasets/C/state_csv.csv"
    :return - pandas dataframe
    """
    df_C = pd.read_csv("cse 163 datasets/C/state_csv.csv")
    df_C.columns = ["0", '1', '2', '3', '4', '5', '6', '7', '8']
    df_C = df_C.loc[10:64, ['0', '5']]
    df_C = df_C.dropna()
    df_C.columns = ['State', '2017-2018 Percentage Poverty']
    return df_C


def getDF_D():
    """
    Produces dataset D. Dataset D contains 2017 and 2018
        US Median Income statistics based off of categories
        household type, race, age, region, etc
    Pulls data from singular csv file
        "cse 163 datasets/D/tableA1_csv.csv"
    :return - pandas dataframe
    """
    df = pd.read_csv("cse 163 datasets/D/tableA1_csv.csv")
    df = df.loc[16:20, ['Table with row headers in column A and column \
                        headers in row 4 through 6.', 'Unnamed: 1',
                        'Unnamed: 2', 'Unnamed: 4', 'Unnamed: 5']]
    df.columns = ['Race', '2017 Number (thousands)', '2017 Median Income',
                  '2018 Number (thousands)',
                  '2018 Median Income']
    return df
