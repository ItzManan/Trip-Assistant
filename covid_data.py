import requests
import json

def covid_cases(country):
    url = "https://corona.lmao.ninja/v2/countries/"+country

    payload = {}
    headers= {}

    #Requesting API
    response = requests.request("GET", url, headers=headers, data = payload)

    byte = response.text.encode('utf8')

    #converts byte string to string
    decoded = byte.decode("utf-8")

    #converts string dictionary to dictionary
    converted = json.loads(decoded)

    return converted["countryInfo"]["flag"], converted["active"]
