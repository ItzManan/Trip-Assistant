import requests, json
CLIENT_ID = 'YHCW2HQMZMYVVW2N3RMODTZSRNRU30UICVXZJ52J22TCJZIZ'
CLIENT_SECRET = 'RMTUUKMNEC0BUWTUDI5DGZBACSRMQ1Q0WIZQ3ZSIYOVTXSTO'

#BHILAI = '21.1938,81.3509'
#MUMBAI = '19.0760,72.8777'

FOOD = '4d4b7105d754a06374d81259'
POI = '4d4b7104d754a06370d81259'
'4bf58dd8d48988d12d941735,4bf58dd8d48988d181941735,4bf58dd8d48988d182941735,4bf58dd8d48988d17b941735,4bf58dd8d48988d193941735,4bf58dd8d48988d184941735,4bf58dd8d48988d1f2931735' 
#'4bf58dd8d48988d12d941735,4bf58dd8d48988d181941735,4bf58dd8d48988d182941735,4bf58dd8d48988d193941735,4bf58dd8d48988d17b941735'
HOTELS = '4bf58dd8d48988d1fa931735'

def hotels(lat,lon):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        v='20200901',
        ll=f'{lat},{lon}',
        section='topPicks',
        categoryId=HOTELS,
    )
    resp = requests.get(url=url, params=params).json()
        
    venues_resp = resp['response']['groups'][0]['items']
    
    final_venues = []
    for i in venues_resp:
        if i['venue']['categories'][0]['name'] == 'Hotel':
            final_venues.append({'name': i['venue']['name'], 'address': i['venue']['location'].get('address', 'No Address')})
    
    print(json.dumps(final_venues, indent=2))
    return final_venues

def food(lat,lon):
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        v='20200901',
        ll=f'{lat},{lon}',
        categoryId=FOOD,
    )
    resp = requests.get(url=url, params=params).json()

    venues_resp = resp['response']['venues']

    final_venues = []
    for i in venues_resp:
        final_venues.append({'name': i['name'], 'address': i['location'].get('address', 'No Address')})
    print(json.dumps(final_venues, indent=2))
    return final_venues

def poi(lat,lon):
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        v='20200901',
        ll=f'{lat},{lon}',
        categoryId=POI,
    )
    resp = requests.get(url=url, params=params).json()
    
    venues_resp = resp['response']['venues']
    
    final_venues = []
    for i in venues_resp:
        final_venues.append({'name': i['name'], 'address': i['location'].get('address', 'No Address')})
    print(json.dumps(final_venues, indent=2))
    return final_venues


# TESTING
# hotels('19.0760','72.8777')
# food('19.0760','72.8777')
# poi('19.0760','72.8777')