import pandas as pd
import re

# df = pd.read_excel('DataStrategist.xlsx')
# df.sort_values(by=['Unique ID'], ascending=False)
# dr = df.tail(60)
# print(dr['Unique ID'])
# print(df['Unique ID'])
# print(df['Type'])
# print(df['Taxonomy'])
# print(df['Current Status'])
# print(df['Last Run Date'])
# print(df['Entities Extracted'])
# print(df['Source Country'])
# print(df['AML Type'])
# print(df['Entity Type'])
# print(df['URL'])


    

x="אבגדהוזחטיכךלמנסעפצקרשתםןףץ"
m=re.findall('[\u05D0-\u05EA]+', x)
print(m)
# inp = input()
# s = 'אבגדהוזחטיכךלמנסעפצקרשתםןףץ'
# for i in inp:
# 	if i in s:
# 		print('ccc')
# 	else:
# 		print('gggg')