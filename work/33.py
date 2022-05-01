desc = ('Country', ['2011 ', '2012 b', '2013 ', ':', ': ', '2016 b', '2017 ', '2018 b', '2019'])
ddict = {}
ddict[desc[0]] = ddict.get(desc[0], desc[1])
print(ddict)
doi = []
ddd = {}
for k, v in ddict.items():
	for i in v:
		r1 = i.replace(' ', '')
		r2 = r1.replace('b', '')
		r3 = r2.replace(':', '0')
		r3 = int(r3)
		print(r3)
		doi.append(r3)
ddd[desc[0]] = ddd.get(desc[0], doi)
print(ddd)
