import pandas as pd
import re

def getDF_A():
    d1 = pd.read_csv("cse 163 datasets/A/ds1.csv")
    d2 = pd.read_csv("cse 163 datasets/A/ds2.csv")
    d5 = pd.read_csv("cse 163 datasets/A/ds5.csv")

    d1 = d1.loc[12:62, :]
    d1.columns = ['Category', '2017 Total Population', '2017 Total Below Poverty', 'drop',
                  '2017 Percentage Below Poverty',
                  'drop', '2018 Total Population', '2018 Total Below Poverty', 'drop', '2018 Percentage Below Poverty',
                  'drop', 'drop', 'drop']
    d1 = d1.loc[:, d1.columns != 'drop']
    d1 = d1.dropna()
    d1["Category"].replace({"Under age 18": "Aged Under 65",
                            "Aged 18 to 64": "Aged Under 65",
                            "Aged 65 and older": "Aged Over 65"
                            }, inplace=True)

    d2 = d2.loc[9:12, :]
    d2.columns = ['Category', '2017 Total Population', '2017 Total Below Poverty', 'drop',
                  '2017 Percentage Below Poverty',
                  'drop', '2018 Total Population', '2018 Total Below Poverty', 'drop', '2018 Percentage Below Poverty',
                  'drop', 'drop', 'drop', 'drop']
    d2 = d2.loc[:, d2.columns != 'drop']
    d2 = d2.dropna()
    d2["Category"].replace({"Primary Families4…………………………………": "Primary Families"
                            }, inplace=True)

    d5 = d5.loc[6:43, :]
    d5.columns = ['Category', '2017 Number People', '2017 Median Income', 'drop', '2018 Number People',
                  '2018 Median Income', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop',
                  'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop',
                  'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop', 'drop']
    d5 = d5.loc[:, d5.columns != 'drop']
    d5 = d5.dropna()
    d5['Category'].replace({".  Married-couple": "Married-couple",
                            ".  Female householder, no spouse present": "Female householder, no spouse present",
                            ".  Male householder, no spouse present": "Male householder, no spouse present",
                            "   White, not Hispanic": "White, not Hispanic",
                            ".. Naturalized citizen": "Naturalized citizen",
                            ".. Not a citizen": "Not a citizen",
                            ".. Inside principal cities": "Inside principal cities",
                            ".. Outside principal cities": "Outside principal cities",
                            "Under 65 years": "Aged Under 65",
                            "65 years and older": "Aged Over 65"
                            }, inplace=True)

    frames = [d1, d2]
    df = pd.concat(frames)
    df = df.merge(d5, left_on='Category', right_on='Category', how='outer')

    columns = ['2017 Total Population', '2017 Total Below Poverty', '2018 Total Population', '2018 Total Below Poverty',
               '2017 Number People', '2017 Median Income', '2018 Number People', '2018 Median Income']

    for col in columns:
        df[col] = df[col].apply(lambda x: re.sub('[^A-Za-z0-9]+', '', str(x)))

    # sum_columns = ['2017 Total Population', '2017 Total Below Poverty', '2018 Total Population',
    #                '2018 Total Below Poverty',
    #                '2017 Number People', '2018 Number People']
    # mean_columns = ['2017 Percentage Below Poverty', '2018 Percentage Below Poverty', '2017 Median Income',
    #                 '2018 Median Income']
    #
    # df.groupby('Category')[mean_columns].apply(lambda x: x.astype(float).mean())
    # df.groupby('Category')[sum_columns].apply(lambda x: x.astype(float).sum())
    df.to_csv("test.csv")

    return df

def getDF_B():
    associates = getDegree("Associates", 26)
    below_associates = getDegree("Below_Associates", 25)
    bachelors = getDegree("Bachelors", 26)
    masters = getDegree("Masters", 26)
    doctors = getDegree("Doctors", 26)
    frames = [below_associates, associates, bachelors, masters, doctors]
    df = pd.concat(frames)
    return df

def getDegree(degree, ind):
    df = pd.read_csv("cse 163 datasets/B/" + degree + "_csv.csv")
    df = df.loc[[ind], :]
    df.columns = ['Degree', 'Num Total', 'Num White', 'Num Black', 'Num Hispanic', 'Num Asian/Pacific Islander',
                  'Num American Indian/ Alaskan native', 'Num Two or More', 'Num Non Resident', 'Perc Total',
                  'Perc White', 'Perc Black', 'Perc Hispanic', 'Perc Asian/Pacific Islander',
                  'Perc American Indian/ Alaskan native', 'Perc Two or More']
    df['Degree'] = degree
    return df

def getDF_C():
    df_C = pd.read_csv("cse 163 datasets/C/state_csv.csv")
    df_C.columns = ["0", '1', '2', '3', '4', '5', '6', '7', '8']
    df_C = df_C.loc[10:64, ['0', '5']]
    df_C = df_C.dropna()
    df_C.columns = ['State', '2017-2018 Percentage Poverty']
    return df_C

def getDF_D():
    df = pd.read_csv("cse 163 datasets/D/tableA1_csv.csv")
    df = df.loc[16:20, ['Table with row headers in column A and column headers in row 4 through 6.', 'Unnamed: 1',
                        'Unnamed: 2', 'Unnamed: 4', 'Unnamed: 5']]
    df.columns = ['Race', '2017 Number (thousands)', '2017 Median Income', '2018 Number (thousands)',
                  '2018 Median Income']
    return df
