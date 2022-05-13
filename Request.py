import requests



res = requests.get('https://ananas.rs/login')

print(res.text)
print(res.status_code)