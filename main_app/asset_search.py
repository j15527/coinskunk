from cryptocompy import coin, price
import requests

API_KEY = "BFDE1212-4CFD-46D7-B992-E2225B5190BD"
URL = 'https://rest.coinapi.io/v1/assets/icons/256/'
headers = {'X-CoinAPI-Key': API_KEY}
response = requests.get(URL, headers=headers)

coins = coin.get_coin_list(coins='all')
# search_term = "btc"
fiat = "USD"


def get_icon(search_term):
    search_term = search_term.upper()
    icons = response.json()
    for asset in icons:
        if asset['asset_id'] == search_term:
            return asset['url']


def coin_search(search_term):
    search_term = search_term.upper()
    if search_term in coins.keys():
        coin = coins[search_term]
        coin_name = coin['Name']
        img = coin['ImageUrl']
        get_coin_price = price.get_current_price(search_term,
                                                 fiat, e='all',
                                                 try_conversion=True,
                                                 full=False,
                                                 format='raw'
                                                 )
        coin_price = get_coin_price[search_term][fiat]
        description = coin['Description']
        img = get_icon(search_term)
        return {'name': coin_name, 'price': coin_price, 'desc': description, 'img': img}
    else:
        return 'No such coin'
