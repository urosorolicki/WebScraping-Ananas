import requests
import bs4 as BeautifulSoup


page = requests.get(
    "https://ananas.rs/login")
soup = BeautifulSoup(page.content, 'html.parser')
# res = requests.get('https://ananas.rs/login')

print(res.text)
print(res.status_code)