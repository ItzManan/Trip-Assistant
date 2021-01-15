from .amadeus import flights, get_token, pois
def full_flight(origin, origin_city, destination, destination_city, dep_date, arr_date):
    token = get_token.get_token()
    message = ''
    data = ''
    
    '''origin = request.form['origin']
    origin_city = request.form['origin_city']
    destination = request.form['destination']
    destination_city = request.form['destination_city']'''
    lat_destination, lon_destination = float(
        destination.split(", ")[0]), float(destination.split(", ")[1])
    lat_origin, lon_origin = float(origin.split(
        ", ")[0]), float(origin.split(", ")[1])
    departure_date = dep_date  #request.form['departureDate']
    return_date = arr_date #request.form['returnDate']
    data, airport_name1, airport_name2 = flights.flight_search(
        lat_origin, lon_origin, lat_destination, lon_destination, departure_date, return_date, token)
    if data:
        message = f'{len(data)} flights found!'
        for flight in data:
            flight["itineraries"][0]['segments'][0]['departure']['iataCode'] = airport_name1
            flight["itineraries"][0]['segments'][0]['arrival']['iataCode'] = airport_name2
            flight['website'] = flights.website(
                flight['validatingAirlineCodes'][0])
            flight['validatingAirlineCodes'][0] = [flights.airline(
                flight['validatingAirlineCodes'][0], token), f"https://content.airhex.com/content/logos/airlines_{flight['validatingAirlineCodes'][0]}_50_20_r.png?md5apikey=4d5669b5107fdc240dba0f03961c48e4"]

    if not data:
        message = f"No direct flights available from {origin_city} to {destination_city}"
    
    print(data)
    return [data, message]

def weather_get(cityname):
    weather = flights.weather(cityname)
    return weather

def get_hotels(lat, lon):
    hotel_data = pois.hotels(lat, lon)
    return hotel_data

def get_pois(lat, lon):
    poi_data = pois.poi(lat, lon)
    return poi_data