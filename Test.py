import requests
from bs4 import BeautifulSoup
import csv


# Make a request
page = requests.get(
    "https://ananas.rs/login")
soup = BeautifulSoup(page.content, 'html.parser')

all_products = [4]
keys = (4)
range = (1000)
products = soup.select('div.thumbnail')
for product in products:
    # TODO: Work, Done
    print("csv.writer")
product = ["Size", "Weight", "/", "/"]

for product in range(1000):
    print(product)
    print(products[product])

keys = all_products[4].keys(4)
range = (1000)

def all_products(f1, f2):
    with open(f1, 'r', encoding='utf8') as File:
        with open(f2, 'w', encoding='utf8', newline='') as File2:
            csvwriter = csv.writer(File2)
            dict_writer = csv.DictWriter(f1, f2)
            dict_writer.writeheader()
            dict_writer.writerows(all_products)
    for c in all_products:
        if c[0] == c[1]:
            same += 1
        print(all_products, keys)


f1 = "/Users/ladmin/Desktop/testpy.csv"
f2 = "/Users/ladmin/Desktop/TestPy2.csv"
