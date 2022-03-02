import pandas as pd

df = pd.read_csv('input.csv')
df = df.T
df = df.drop(df.index[0])
df = pd.DataFrame(df.values, columns=["id", "brand", "model", "hp", "price"])
df = df[df.duplicated(['brand'], keep=False)]
