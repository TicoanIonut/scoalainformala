# import numpy as np
# The given code includes a list of heights for various basketball players.
# You need to calculate and output how many players are in the range of one standard deviation from the mean.
# Output
# mean = sum(elements) / len(elements)
# variance = sum([(elem-mean)**2 for elem in elements]) / len(elements)
# standard_deviation = variance**.5

# players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
# mean = sum(players)/len(players)
# variance = sum([(ele-mean)**2 for ele in players])/len(players)
# std = variance ** .5
# lll = [i for i in players if (mean - std) <= i <= (mean + std)]
# print(len(lll))

# x = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
# mean = np.mean(x)
# print(mean)
# median = np.median(x)
# print(median)
# var = np.var(x)
# print(var)
# std = np.std(x)
# print(std)
# rrr = [i for i in x if (mean - std) <= i <= (mean + std)]
# print(len(rrr))
# res = [i for i in x if (np.mean(x) - np.std(x)) <= i <= (np.mean(x) + np.std(x))]
# print(len(res))


# You are given an array that represents house prices.
# Calculate and output the percentage of houses that are within one standard deviation from the mean.
# To calculate the percentage, divide the number of houses that satisfy the condition by the total
# number of houses, and multiply the result by 100.

# data = np.array([150000, 125000, 320000, 540000, 200000, 120000,
#                  160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
# mean = np.mean(data)
# # print(mean, "mean")
# std = np.std(data)
# # print(std, 'std')
# r = mean + std
# s = mean - std
# # print(s, 'mean - std')
# # print(r, 'mean + std')
# satisf = [i for i in data if s < i < r]
# # print(satisf)
# # print(len(satisf))
# res = (len(satisf)/len(data)) * 100
# print(res)


# You are working with the COVID dataset for California,
# which includes the number of cases and deaths for each day of 2020.
# Find the day when the deaths/cases ratio was largest.
# To do this, you need to first calculate the deaths/cases ratio and add
# it as a column to the DataFrame with the name 'ratio', then find the row that corresponds to the largest value.
# Important: The output should be a DataFrame, containing all of the columns of the dataset for the corresponding row.

import pandas as pd
df = pd.read_csv("ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)
df['ratio'] = df['deaths'] / df['cases']
print(df[df['ratio'] == df['ratio'].max()])
