import json
import time
import requests
# --------------------------------------------------------------------
name = "Mumbai"
# lat2, lon2 = 51.5073, -0.127647
# --------------------------------------------------------------------


def weather(city_name):
    API_KEY = '701726f03e98fea267e17f9e15b584f0'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    r = requests.get(link).json()
    sample = {
        'name': r['name'],
        'coor': [r['coord']['lon'], r['coord']['lat']],
        'main_weather_type': r['weather'][0]['main'],
        'current_temp': int(r['main']['temp'] - 273),
        'min_temp': int(r['main']['temp_min'] - 273),
        'max_temp': int(r['main']['temp_max'] - 273),
        'pressure': r['main']['pressure'],
        'humidity': r['main']['humidity'],
        'visibility': r['visibility'],
        'wind': [r['wind']['speed'], r['wind']['deg']],
        'dt': r['dt'],
        'country': r['sys']['country'],
        'sun_time': [r['sys']['sunrise'], r['sys']['sunset']],
        'timezone': r['timezone']
    }
    return sample

# print(weather(name))
# print()
# --------------------------------------------------------------------

# Airport Nearest Relevant


def nearest_airport(lat, lon, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f'https://test.api.amadeus.com/v1/reference-data/locations/airports?latitude={lat}&longitude={lon}'

    response = requests.get(url, headers=headers)
    data = response.json()['data']
    min = data[0]['distance']['value']
    min_loc = data[0]
    for location in data:
        if location['distance']['value'] < min:
            min = location['distance']['value']
            min_loc = location
    # print("{} - {}{}".format(min_loc['name'],min_loc['distance']['value'],min_loc['distance']['unit']))
    # print(min_loc['address']['cityCode'])
    return min_loc['address']['cityCode'], min_loc['name']

# --------------------------------------------------------------------
# Flight Inspiration Search


def flight_search(lat1, lon1, lat2, lon2, departure_date, return_date, token):
  start = time.time()
  # try:
  headers = {
      "Authorization": f"Bearer {token}"
  }
  import asyncio
  import aiohttp

  async def main():
    async with aiohttp.ClientSession() as session:
      tasks = []
      task1 = asyncio.ensure_future(get_it(session, lat1, lon1, token))
      task2 = asyncio.ensure_future(get_it(session, lat2, lon2, token))

      tasks.append(task1)
      tasks.append(task2)

      final = await asyncio.gather(*tasks)
    return final

  async def get_it(session, lat, lon, token):
    url = f'https://test.api.amadeus.com/v1/reference-data/locations/airports?latitude={lat}&longitude={lon}'
    async with session.get(url, headers=headers) as response:
      data = await response.json()
      data = data['data']
      min = data[0]['distance']['value']
      min_loc = data[0]
      for location in data:
          if location['distance']['value'] < min:
              min = location['distance']['value']
              min_loc = location
      # print("{} - {}{}".format(min_loc['name'],min_loc['distance']['value'],min_loc['distance']['unit']))
      # print(min_loc['address']['cityCode'])
      return [min_loc['address']['cityCode'], min_loc['name']]


  # city1, airport_name1 = nearest_airport(lat1, lon1, token)
  # city2, airport_name2 = nearest_airport(lat2, lon2, token)
  # ****************DONT CLEAR THIS****************
  # TESTING DATES
  # departure_date = '2021-01-20'
  # return_date = '2021-01-27'

  # INITIAL CODE STARTS
  # url = f"https://test.api.amadeus.com/v1/shopping/flight-destinations?origin={city1}&departureDate={departure_date}"
  # response = requests.get(url, headers=headers)
  # data = response.json()['data']
  # for flight in data:
  #     if flight['destination'] == city2:
  #         data_str = json.dumps(flight, indent=3)
  #         print(data_str)
  #         print("\nSEPARATOR\n")
  # INITIAL CODE ENDS
  # ****************DONT CLEAR THIS****************
  [city1, airport_name1],[city2, airport_name2] = asyncio.run(main())
  url = f"https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={city1}&destinationLocationCode={city2}&departureDate={departure_date}&returnDate={return_date}&adults=2"
  response = requests.get(url, headers=headers)
  data = response.json()['data']
  # print(data)
  # print("\n\n\n")
  print(time.time() - start)
  return data, airport_name1, airport_name2
  # except:
      # print(time.time() - start)
      # return False, False, False
  # return data_str

# --------------------------------------------------------------------


def check_in(code, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    print(f"NAHI\n\n{code}\n\n")
    url = f'https://test.api.amadeus.com/v2/reference-data/urls/checkin-links?airlineCode={code}'
    response = requests.get(url, headers=headers).json()['data'][0]['href']
    return response
# --------------------------------------------------------------------
# Airline CODE => LOGO, LINK


def lonk(code):
    dict = {
        "AI": ["Air India", "http://www.airindia.in/"],
        "AF": ["Air France", "http://www.airindia.in/"],
        "AK": ["Air Asia", "http://www.airindia.in/"],
        "BA": ["British Airways", "http://www.airindia.in/"],
        "DL": ["Delta", "http://www.airindia.in/"],
        "U2": ["EasyJet", "http://www.airindia.in/"],
        "EK": ["Emirates", "http://www.airindia.in/"],
        "G8": ["Go Air", "http://www.airindia.in/"],
        "6E": ["Indigo", "http://www.airindia.in/"],
        "9W": ["Jet Airways", "http://www.airindia.in/"],
        "LH": ["Lufthansa", "http://www.airindia.in/"],
        "NH": ["Nippon Airlines", "http://www.airindia.in/"],
        "SG": ["Spicejet", "http://www.airindia.in/"],
        "UA": ["United Airlines", "http://www.airindia.in/"],
        "IB": ["Iberia", "http://www.airindia.in/"]
    }
    return dict[code]


def website(code):
    url = "https://iata-and-icao-codes.p.rapidapi.com/airline"

    querystring = {"iata_code": code}

    headers = {
        'x-rapidapi-key': "b2c5d09d95msh761f4b7db94c313p17bff8jsn371b13a76e87",
        'x-rapidapi-host': "iata-and-icao-codes.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()[0]['website']

# --------------------------------------------------------------------
# Flight Offers Search


# def flight_offer_search(city1, city2, departure_date, return_date):
#     url = f"https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={city1}&destinationLocationCode={city2}&departureDate={departure_date}&returnDate={return_date}&adults=2&max=5"
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }

#     response = requests.get(url, headers=headers)
#     print(response.text)

# flight_offer_search()


# --------------------------------------------------------------------
# Airport & City Search by Keyword
# def airport(code, token):
#     import json
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }
#     url = f'https://test.api.amadeus.com/v1/reference-data/locations?subType=CITY,AIRPORT&keyword={code}'
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     print("\n\n\n")
#     print(json.dumps(data, indent=3))
    # return data[0]['name']


# print(airport("DEL"))

# --------------------------------------------------------------------

# Airline Code Lookup
def airline(code, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f'https://test.api.amadeus.com/v1/reference-data/airlines?airlineCodes={code}'
    response = requests.get(url, headers=headers)
    response_str = response.json()['data'][0]['businessName']
    return response_str

# --------------------------------------------------------------------


'''
SAMPLE FLIGHT OFFER SEARCH
{
   "type": "flight-destination",
   "origin": "DEL",
   "destination": "BOM",
   "departureDate": "2021-01-20",
   "returnDate": "2021-01-21",
   "price": {
      "total": "7961.00"
   },
   "links": {
      "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=DEL&destination=BOM&departureDate=2021-01-20&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
      "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=DEL&destinationLocationCode=BOM&departureDate=2021-01-20&returnDate=2021-01-21&adults=1&nonStop=false"
   }
}

SEPARATOR

{
  "meta" : {
    "count" : 5,
    "links" : {
      "self" : "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=DEL&destinationLocationCode=BOM&departureDate=2021-01-20&returnDate=2021-01-27&adults=2&max=5"
    }
  },
  "data" : [ {
    "type" : "flight-offer",
    "id" : "1",
    "source" : "GDS",
    "instantTicketingRequired" : false,
    "nonHomogeneous" : false,
    "oneWay" : false,
    "lastTicketingDate" : "2021-01-20",
    "numberOfBookableSeats" : 3,
    "itineraries" : [ {
      "duration" : "PT2H10M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-20T06:50:00"
        },
        "arrival" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-20T09:00:00"
        },
        "carrierCode" : "AI",
        "number" : "887",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H10M",
        "id" : "1",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    }, {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-27T07:00:00"
        },
        "arrival" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-27T09:15:00"
        },
        "carrierCode" : "AI",
        "number" : "866",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "3",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    } ],
    "price" : {
      "currency" : "EUR",
      "total" : "195.62",
      "base" : "164.00",
      "fees" : [ {
        "amount" : "0.00",
        "type" : "SUPPLIER"
      }, {
        "amount" : "0.00",
        "type" : "TICKETING"
      } ],
      "grandTotal" : "195.62"
    },
    "pricingOptions" : {
      "fareType" : [ "PUBLISHED" ],
      "includedCheckedBagsOnly" : true
    },
    "validatingAirlineCodes" : [ "AI" ],
    "travelerPricings" : [ {
      "travelerId" : "1",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "3",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    }, {
      "travelerId" : "2",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "3",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    } ]
  }, {
    "type" : "flight-offer",
    "id" : "2",
    "source" : "GDS",
    "instantTicketingRequired" : false,
    "nonHomogeneous" : false,
    "oneWay" : false,
    "lastTicketingDate" : "2021-01-20",
    "numberOfBookableSeats" : 3,
    "itineraries" : [ {
      "duration" : "PT2H10M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-20T06:50:00"
        },
        "arrival" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-20T09:00:00"
        },
        "carrierCode" : "AI",
        "number" : "887",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H10M",
        "id" : "1",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    }, {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-27T21:00:00"
        },
        "arrival" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-27T23:15:00"
        },
        "carrierCode" : "AI",
        "number" : "538",
        "aircraft" : {
          "code" : "77W"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "5",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    } ],
    "price" : {
      "currency" : "EUR",
      "total" : "195.62",
      "base" : "164.00",
      "fees" : [ {
        "amount" : "0.00",
        "type" : "SUPPLIER"
      }, {
        "amount" : "0.00",
        "type" : "TICKETING"
      } ],
      "grandTotal" : "195.62"
    },
    "pricingOptions" : {
      "fareType" : [ "PUBLISHED" ],
      "includedCheckedBagsOnly" : true
    },
    "validatingAirlineCodes" : [ "AI" ],
    "travelerPricings" : [ {
      "travelerId" : "1",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "5",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    }, {
      "travelerId" : "2",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "5",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    } ]
  }, {
    "type" : "flight-offer",
    "id" : "3",
    "source" : "GDS",
    "instantTicketingRequired" : false,
    "nonHomogeneous" : false,
    "oneWay" : false,
    "lastTicketingDate" : "2021-01-20",
    "numberOfBookableSeats" : 3,
    "itineraries" : [ {
      "duration" : "PT2H10M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-20T06:50:00"
        },
        "arrival" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-20T09:00:00"
        },
        "carrierCode" : "AI",
        "number" : "887",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H10M",
        "id" : "1",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    }, {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-27T10:00:00"
        },
        "arrival" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-27T12:15:00"
        },
        "carrierCode" : "AI",
        "number" : "809",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "4",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    } ],
    "price" : {
      "currency" : "EUR",
      "total" : "195.62",
      "base" : "164.00",
      "fees" : [ {
        "amount" : "0.00",
        "type" : "SUPPLIER"
      }, {
        "amount" : "0.00",
        "type" : "TICKETING"
      } ],
      "grandTotal" : "195.62"
    },
    "pricingOptions" : {
      "fareType" : [ "PUBLISHED" ],
      "includedCheckedBagsOnly" : true
    },
    "validatingAirlineCodes" : [ "AI" ],
    "travelerPricings" : [ {
      "travelerId" : "1",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "4",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    }, {
      "travelerId" : "2",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "4",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    } ]
  }, {
    "type" : "flight-offer",
    "id" : "4",
    "source" : "GDS",
    "instantTicketingRequired" : false,
    "nonHomogeneous" : false,
    "oneWay" : false,
    "lastTicketingDate" : "2021-01-20",
    "numberOfBookableSeats" : 5,
    "itineraries" : [ {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-20T10:40:00"
        },
        "arrival" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-20T12:55:00"
        },
        "carrierCode" : "AI",
        "number" : "865",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "2",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    }, {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-27T07:00:00"
        },
        "arrival" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-27T09:15:00"
        },
        "carrierCode" : "AI",
        "number" : "866",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "3",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    } ],
    "price" : {
      "currency" : "EUR",
      "total" : "195.62",
      "base" : "164.00",
      "fees" : [ {
        "amount" : "0.00",
        "type" : "SUPPLIER"
      }, {
        "amount" : "0.00",
        "type" : "TICKETING"
      } ],
      "grandTotal" : "195.62"
    },
    "pricingOptions" : {
      "fareType" : [ "PUBLISHED" ],
      "includedCheckedBagsOnly" : true
    },
    "validatingAirlineCodes" : [ "AI" ],
    "travelerPricings" : [ {
      "travelerId" : "1",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "2",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "3",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    }, {
      "travelerId" : "2",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "2",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "3",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    } ]
  }, {
    "type" : "flight-offer",
    "id" : "5",
    "source" : "GDS",
    "instantTicketingRequired" : false,
    "nonHomogeneous" : false,
    "oneWay" : false,
    "lastTicketingDate" : "2021-01-20",
    "numberOfBookableSeats" : 5,
    "itineraries" : [ {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-20T10:40:00"
        },
        "arrival" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-20T12:55:00"
        },
        "carrierCode" : "AI",
        "number" : "865",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "2",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    }, {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-27T21:00:00"
        },
        "arrival" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-27T23:15:00"
        },
        "carrierCode" : "AI",
        "number" : "538",
        "aircraft" : {
          "code" : "77W"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "5",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    } ],
    "price" : {
      "currency" : "EUR",
      "total" : "195.62",
      "base" : "164.00",
      "fees" : [ {
        "amount" : "0.00",
        "type" : "SUPPLIER"
      }, {
        "amount" : "0.00",
        "type" : "TICKETING"
      } ],
      "grandTotal" : "195.62"
    },
    "pricingOptions" : {
      "fareType" : [ "PUBLISHED" ],
      "includedCheckedBagsOnly" : true
    },
    "validatingAirlineCodes" : [ "AI" ],
    "travelerPricings" : [ {
      "travelerId" : "1",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "2",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "5",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    }, {
      "travelerId" : "2",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "2",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "5",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    } ]
  } ],
  "dictionaries" : {
    "locations" : {
      "BOM" : {
        "cityCode" : "BOM",
        "countryCode" : "IN"
      },
      "DEL" : {
        "cityCode" : "DEL",
        "countryCode" : "IN"
      }
    },
    "aircraft" : {
      "32B" : "AIRBUS A321 (SHARKLETS)",
      "77W" : "BOEING 777-300ER"
    },
    "currencies" : {
      "EUR" : "EURO"
    },
    "carriers" : {
      "AI" : "AIR INDIA"
    }
  }
}

'''
