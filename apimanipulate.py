import requests

response = requests.get("https://api.exchangerate.host/latest")

print(response)
print(response.json())
