# Helper functions that update the database with fresh prices from API
from cryptocompy import coin, price
from django.contrib.auth import get_user


def update(request):
    request = request
    user = get_user(request)
    assets = user.portfolio_set.first().assets.all()
    fiat = "USD"
    for i in assets:
        asset = price.get_current_price(i.name, fiat, e='all', full=False)
        asset_price = asset[i.name][fiat]
        i.price = asset_price
        i.save()

    return user





