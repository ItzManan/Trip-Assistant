from flask import Blueprint, render_template, url_for, request, jsonify
#import requests
from .utils import full_flight
import time

main = Blueprint('main', __name__)


@main.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.get_json(force=True)
        result = full_flight(data['origin'], data['origin_city'], data['destination'], data['destination_city'])
        
        #time.sleep(2)
        return jsonify(result)

        # TESTING
        # print(origin)
        # print(destination)
        # print(departure_date)
        # print(return_date)
    return render_template('home.html')

'''@main.route('/trip', methods=['POST','GET'])
def trip():
    return render_template('index.html', data=session['data'])'''