import pandas as pd
# data = {'ages': [14, 18, 24, 42], 'heights': [165, 180, 176, 184], 'iq': [111, 112, 122, 222]}
# df = pd.DataFrame(data)
# print(df)
# df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
# print(df)
# print(df.loc[["Bob", 'Amy']], '\nBob and Amy')
# print(df.loc["Bob"], '\nBob')
# print(df[["ages"]], '\nages')
# print(df[["ages", 'heights']], '\nages and heights')
# print(df.iloc[2], '\nthird row')
# print(df.iloc[:3], '\nfirst 3 rows')
# print(df.iloc[1:3], '\nrows 2 to 3')
# print(df[(df['ages'] > 18) & (df['heights'] > 175)], '\n ages > 18 and heights > 175')
df = pd.read_csv("ca-covid.csv")
# print(df.head(10))                              # header default is 5
df['month'] = pd.to_datetime(df['date'], format="%d.%m.%y").dt.month_name()
df.set_index('date', inplace=True)
# df['test'] = df['cases'] * df['deaths']             test
# print(df.head(10))
df.drop('state', axis=1, inplace=True)
# df.drop([0], axis=0, inplace=True)                # delete by index
# print(df.head(10))
# df.info()
print(df.describe())
# print(df['cases'].describe())                       # specific cases
print(df['month'].value_counts())
print('\nsum of cases by month', df.groupby('month')['cases'].sum())
print('\nsum of all cases is', df['cases'].sum())
print('\nmedia of all cases is', df['cases'].mean())
