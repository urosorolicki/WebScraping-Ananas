from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pandas
import csv as pd

driver = webdriver.Chrome("/Users/ladmin/Downloads/chromedriver 3")
ipaddress = []
prices = []
ratings = []
driver.get(
    "<a href="">https://ananas.rs/")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'})
    price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
    ipaddress.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame(
    {'Product Name': ipaddress, 'Price': prices, 'Rating': ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
