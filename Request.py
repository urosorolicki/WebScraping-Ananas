import requests
import csv
import os


res = requests.get('https://ananas.rs/login')

for x in range(2000, 3000):
    print('ID', x, sep=':')


def write_file('res, op2.csv'):
    with open(op2.csv, 'wb') as outfile:


f = open('op2.csv', 'w')
writer = csv.writer(f)
writer = csv.writer('op2.csv')
for row in res:  # ABOVE ERROR IS THROWN HERE
    writer.writerow(row)
f.close()
print(res.text)
print(res.status_code)
