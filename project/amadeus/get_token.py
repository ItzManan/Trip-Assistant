import requests


def get_token():

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': 'QFqpTSEjKQBsaKNdVzFXWASwHpX4jh6o',
        'client_secret': 'qgvmqlG2DveTXF1B'
    }

    response = requests.post(
        'https://test.api.amadeus.com/v1/security/oauth2/token', headers=headers, data=data)
    token = response.json()
    token = token['access_token']
    return token
