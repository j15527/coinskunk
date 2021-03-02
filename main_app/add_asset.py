from .models import Asset, Portfolio
from cryptocompy import coin, price
import requests
from django.contrib.auth import get_user


def add_asset(request, asset, count):
    request = request
    asset = asset
    count = count
    user = get_user(request)
    obj, created = user.portfolio_set.first().assets.update_or_create(
        name=asset,
        count=count,



    )
    print(f'Test Add {asset}')
