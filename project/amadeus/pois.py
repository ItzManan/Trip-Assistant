import requests
from get_token import get_token

token = get_token()

latitude = 51.5073219
longitude = -0.1276474

url = f"https://test.api.amadeus.com/v1/reference-data/locations/pois?latitude={latitude}&longitude={longitude}&radius=2"

payload = {}
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.request("GET", url, headers=headers, data=payload)

show = response.json()

for el in show:
    for i in show[el]:
        print(i)
        print("\n")
    break
