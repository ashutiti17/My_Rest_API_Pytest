import requests

res = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities")

print(res.status_code)
print(res.json())

