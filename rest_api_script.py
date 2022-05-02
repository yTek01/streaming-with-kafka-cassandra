import requests
import json

def data_from_coins_api():
    response_from_api = requests.get(url="https://api.coinranking.com/v2/coins",
                                 headers={'Authorization': 'x-access-token: '.format("coinrankingb5ba281582c06d654d54314404e498f9346ffd6d83459e44")})

    json_data = json.loads(response_from_api.text)
    return json_data