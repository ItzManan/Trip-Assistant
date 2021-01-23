from project.covid_data import covid_cases
from flask import Blueprint, render_template, url_for, request, jsonify, session
#import requests
from .utils import full_flight, weather_get, get_hotels, get_pois
import time

main = Blueprint('main', __name__)


@main.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.get_json(force=True)
        result = full_flight(data['origin'], data['origin_city'], data['destination'], data['destination_city'], data['depDate'], data['arrDate'])

        if result == 'ERROR':
            return jsonify('ERROR')  

        weather = weather_get(data['destination_city'])
        lat_destination, lon_destination = float(
        data['destination'].split(", ")[0]), float(data['destination'].split(", ")[1])
        hotels = get_hotels(lat_destination, lon_destination)
        pois = get_pois(lat_destination, lon_destination)
        active_cases = covid_cases(data['countryCode'])
        # print(data['destination_city'])
        #time.sleep(2)
        
        session['data'] = [result,pois]
        session['weather'] = [weather, hotels]
        session['covid'] = active_cases
        session['coords'] = [lat_destination, lon_destination]

        # TESTING
        # print(origin)
        # print(destination)
        # print(departure_date)
        # print(return_date)
        return jsonify('Data Success!')
    return render_template('home.html')

'''@main.route('/trip', methods=['POST','GET'])
def trip():
    return render_template('index.html', data=session['data'])'''

@main.route('/trip')
def info():
    return render_template('test3.html', data=session['data'][0][0], weather=session['weather'][0], hotels=session['weather'][1], pois=session['data'][1], message=session['data'][0][1], covid=session['covid'], coords=session['coords'])
