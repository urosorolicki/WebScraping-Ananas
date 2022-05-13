import requests
from bs4 import BeautifulSoup

# Make a request to https://ananas.rs/
page = requests.get(
    "https://ananas.rs/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title.text

# print the result
print(page_title)