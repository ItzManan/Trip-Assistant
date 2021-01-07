import requests
import json
from get_token import get_token
token = get_token()
# headers
headers= {
	"Authorization": f"Bearer {token}"
}

def hotels(cityCode):
  lst = []
  url = f'https://test.api.amadeus.com/v2/shopping/hotel-offers?adults=2&cityCode={cityCode}&includeClosed=false&paymentPolicy=NONE&radius=20&radiusUnit=KM&roomQuantity=1&sort=DISTANCE&view=FULL'
  # url1 = f'https://test.api.amadeus.com/v2/shopping/hotel-offers?adults=2&cityCode={cityCode}&includeClosed=false&paymentPolicy=NONE&radius=20&radiusUnit=KM&roomQuantity=1&sort=NONE&view=FULL&page[offset]=95EWTRHOTCN3_100'
  # url2 = f'https://test.api.amadeus.com/v2/shopping/hotel-offers?adults=2&cityCode={cityCode}&includeClosed=false&paymentPolicy=NONE&radius=20&radiusUnit=KM&roomQuantity=1&sort=NONE&view=FULL&page[offset]=95EWTRHOTCN3_200'

  response = requests.get(url, headers=headers).json()
  print(json.dumps(response, indent=2))
  # print(len(response['data']))

  # response = requests.get(url1, headers=headers).json()
  # print(json.dumps(response, indent=2))

  # response = requests.get(url2, headers=headers).json()
  # print(json.dumps(response, indent=2))
  while 'meta' in response.keys():
    # print(json.dumps(response, indent=2))
    url = response['meta']['links']['next']
    response = requests.get(url, headers=headers).json()
    # print(len(response['data']))
    print(json.dumps(response, indent=2))

hotels("DEL")