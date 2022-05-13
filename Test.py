import requests
from bs4 import BeautifulSoup
import csv
# Make a request
page = requests.get(
    "https://ananas.rs")
soup = BeautifulSoup(page.content, 'html.parser')

all_products = [4]
keys = (4)

products = soup.select('div.thumbnail')
for product in products:
    # TODO: Work, Done
    print("Done!")


keys = all_products[4].keys(4)

def all_products (f1,f2):     
    with open(f1, 'r', encoding='utf8') as File:
        with open(f2, 'w', encoding='utf8', newline='') as File2:
         dict_writer = csv.DictWriter(f1, f2)
         dict_writer.writeheader()
         dict_writer.writerows(all_products)
    for c in cdec:
     if c[0]==c[1]: same+=1   
     print(all_products, keys)

f1 = "/Users/ladmin/Desktop/TestClassla21.csv"
f2 = "/Users/ladmin/Desktop/TestClassla1.csv"