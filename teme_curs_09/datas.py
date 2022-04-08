import pandas as pd
description = ('Country', ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017', '2018 ', '2019 '])
dataset = [
 ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ':']),
 ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
 ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
 ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
 ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
 ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
 ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
 ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
 ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
 ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
 ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
 ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
 ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
 ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
 ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
 ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
 ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
 ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
 ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
 ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99', '98 ']),
 ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
 ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
 ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
 ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
 ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
 ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79', '82 ']),
 ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
 ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
 ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
 ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
 ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
 ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
 ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
 ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
 ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
 ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
 ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84', '88 ']),
 ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
 ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']), ]
ddict = {}
ddict[description[0]] = ddict.get(description[0], description[1])
ddict[dataset[0][0]] = ddict.get(dataset[0][0], dataset[0][1])
ddict[dataset[1][0]] = ddict.get(dataset[1][0], dataset[1][1])
ddict[dataset[2][0]] = ddict.get(dataset[2][0], dataset[2][1])
ddict[dataset[3][0]] = ddict.get(dataset[3][0], dataset[3][1])
ddict[dataset[4][0]] = ddict.get(dataset[4][0], dataset[4][1])
ddict[dataset[5][0]] = ddict.get(dataset[5][0], dataset[5][1])
ddict[dataset[6][0]] = ddict.get(dataset[6][0], dataset[6][1])
ddict[dataset[7][0]] = ddict.get(dataset[7][0], dataset[7][1])
ddict[dataset[8][0]] = ddict.get(dataset[8][0], dataset[8][1])
ddict[dataset[9][0]] = ddict.get(dataset[9][0], dataset[9][1])
ddict[dataset[10][0]] = ddict.get(dataset[10][0], dataset[10][1])
ddict[dataset[11][0]] = ddict.get(dataset[11][0], dataset[11][1])
ddict[dataset[12][0]] = ddict.get(dataset[12][0], dataset[12][1])
ddict[dataset[13][0]] = ddict.get(dataset[13][0], dataset[13][1])
ddict[dataset[14][0]] = ddict.get(dataset[14][0], dataset[14][1])
ddict[dataset[15][0]] = ddict.get(dataset[15][0], dataset[15][1])
ddict[dataset[16][0]] = ddict.get(dataset[16][0], dataset[16][1])
ddict[dataset[17][0]] = ddict.get(dataset[17][0], dataset[17][1])
ddict[dataset[18][0]] = ddict.get(dataset[18][0], dataset[18][1])
ddict[dataset[19][0]] = ddict.get(dataset[19][0], dataset[19][1])
ddict[dataset[20][0]] = ddict.get(dataset[20][0], dataset[20][1])
ddict[dataset[21][0]] = ddict.get(dataset[21][0], dataset[21][1])
ddict[dataset[22][0]] = ddict.get(dataset[22][0], dataset[22][1])
ddict[dataset[23][0]] = ddict.get(dataset[23][0], dataset[23][1])
ddict[dataset[24][0]] = ddict.get(dataset[24][0], dataset[24][1])
ddict[dataset[25][0]] = ddict.get(dataset[25][0], dataset[25][1])
ddict[dataset[26][0]] = ddict.get(dataset[26][0], dataset[26][1])
ddict[dataset[27][0]] = ddict.get(dataset[27][0], dataset[27][1])
ddict[dataset[28][0]] = ddict.get(dataset[28][0], dataset[28][1])
ddict[dataset[29][0]] = ddict.get(dataset[29][0], dataset[29][1])
ddict[dataset[30][0]] = ddict.get(dataset[30][0], dataset[30][1])
ddict[dataset[31][0]] = ddict.get(dataset[31][0], dataset[31][1])
ddict[dataset[32][0]] = ddict.get(dataset[32][0], dataset[32][1])
ddict[dataset[33][0]] = ddict.get(dataset[33][0], dataset[33][1])
ddict[dataset[34][0]] = ddict.get(dataset[34][0], dataset[34][1])
ddict[dataset[35][0]] = ddict.get(dataset[35][0], dataset[35][1])
ddict[dataset[36][0]] = ddict.get(dataset[36][0], dataset[36][1])
ddict[dataset[37][0]] = ddict.get(dataset[37][0], dataset[37][1])
ddict[dataset[38][0]] = ddict.get(dataset[38][0], dataset[38][1])
df = pd.DataFrame(ddict)
df = df.T
print(df)

