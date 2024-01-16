
import csv

with open('./data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for id, row in enumerate(spamreader):
        if id == 0: 
            continue
        line = row[0].split(',')
        print('{}:{}'.format(line[3], line[1]))