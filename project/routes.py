from flask import Blueprint, render_template, url_for, request, jsonify, session
from werkzeug.utils import redirect
#import requests
from .utils import full_flight
import time

main = Blueprint('main', __name__)


@main.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.get_json(force=True)
        result = full_flight(data['origin'], data['origin_city'], data['destination'], data['destination_city'], data['depDate'], data['arrDate'])
        
        #time.sleep(2)
        session['data'] = result
        
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
    return render_template('test3.html', data=session['data'][0])