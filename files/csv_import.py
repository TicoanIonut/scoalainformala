import csv

masini = [
    ['Dacia', 'Logan', 2005, 75],
    ['Renault', 'Clio', 2005, 75]
]

with open('data.csv','a') as csv_file:
    csv_write =csv.writer(csv_file, delimiter =',')
    for masina in masini:
        csv_write.writerow(masina)