import requests

BASE = "http://172.21.0.2:5000/"

response = requests.patch(BASE + "api/vocab", {})
print(response.json())