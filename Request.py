import requests


res = requests.get('https://ananas.rs')

print(res.text)
print(res.status_code)