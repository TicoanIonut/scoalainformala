import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)
df[df['month'] == 12]['cases'].plot()
(df[df['month']==12])[['cases', 'deaths']].plot()
# plt.savefig('plot.png')
(df.groupby('month')['cases'].sum()).plot(kind="bar")
df = df.groupby('month')[['cases', 'deaths']].sum()
df.plot(kind="bar", stacked=True)
plt.show()
