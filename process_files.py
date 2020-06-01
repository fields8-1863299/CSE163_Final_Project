import pandas as pd

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

def main():
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

    d2 = d2.loc[9:12, :]
    d2.columns = ['Category', '2017 Total Population', '2017 Total Below Poverty', 'drop',
                  '2017 Percentage Below Poverty',
                  'drop', '2018 Total Population', '2018 Total Below Poverty', 'drop', '2018 Percentage Below Poverty',
                  'drop', 'drop', 'drop', 'drop']
    d2 = d2.loc[:, d2.columns != 'drop']
    d2 = d2.dropna()
    d2["Category"].replace({"Primary Families4…………………………………": "Primary Families"
                            }, inplace=True)

    d2.to_csv("cse 163 datasets/test/ds2.csv")
    d1.to_csv("cse 163 datasets/test/ds1.csv")




if __name__ == '__main__':
    main()
