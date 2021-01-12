CLIENT_ID = 'YHCW2HQMZMYVVW2N3RMODTZSRNRU30UICVXZJ52J22TCJZIZ'
CLIENT_SECRET = 'RMTUUKMNEC0BUWTUDI5DGZBACSRMQ1Q0WIZQ3ZSIYOVTXSTO'
import json, requests
url = 'https://api.foursquare.com/v2/venues/explore'
# url = 'https://api.foursquare.com/v2/venues/trending'

params = dict(
client_id=CLIENT_ID,
client_secret=CLIENT_SECRET,
v='20200901',
ll='48.864716,2.349014',
near='city',
# limit=1
)
resp = requests.get(url=url, params=params).json()
# data = json.loads(resp.text).text
print(json.dumps(resp, indent=3))


# url2 = f'https://api.foursquare.com/v2/photos/'
# r = requests.get(url2, params=params)
# print(r.json())

# KEY = '563492ad6f91700001000001f637ce29f4d44a138a4059155d6c6b8d'
# import requests

# headers = {
#     'Authorization': KEY,
# }

# params = (
#     ('query', ''),
#     ('per_page', '1'),
# )

# response = requests.get('https://api.pexels.com/v1/search', headers=headers, params=params)
# print(response.json()['photos'][0]['src']['original'])

