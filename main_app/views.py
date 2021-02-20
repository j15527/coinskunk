from django.shortcuts import render
from .models import Portfolio, Asset
# from django.contrib.auth.models import User
from django.contrib import auth
import json
import requests
from django.contrib.auth.decorators import login_required
# from nomics import Nomics
from . import testdata
from django.core import serializers

KEY = "key=6fefbc3e132ad0009443f5be19ce5a3a"
MY_NOMICS_KEY = "6fefbc3e132ad0009443f5be19ce5a3a"
URL = f"https://api.nomics.com/v1/currencies/ticker?{KEY}&interval=1d,30d&per-page=100&page=1"


def index2(request):
    # api_request = requests.get(URL)  # type class requests.models.Response
    # coins = nomics.Currencies.get_currencies(ids="BTC, ETH")
    # results = Asset.objects.all()
    # tasks.db_update()
    # try:
    # api = json.loads(api_request.content)  # type list
    # markets = nomics.Markets.get_markets(exchange='binance')
    # api_request.content type bytes
    # api = api_request.json()# list
    # except Exception as e:
    # api = "Error..."
    return render(request, "main_app/index.html", {}, )


def test_page(request):  # A diagnostic page to view incoming and db update data
    user = request.user
    assets = user.portfolio_set.first().assets.all()
    data = serializers.serialize("json", assets)

    context = {
        'data': data,
    }
    return render(request, "main_app/test.html", context)


@login_required
def index(request):
    user = request.user

    context = {
        'user': user,
        'port': user.portfolio_set.first(),
        'value': user.portfolio_set.first().value,
        'net': user.portfolio_set.first().net_worth(),
        'asset': user.portfolio_set.first().assets.all(),
        'count': user.portfolio_set.first().asset_count,
        'principal': user.portfolio_set.first().principal_sum

    }
    return render(request, 'main_app/index.html', context)


# noinspection DuplicatedCode
@login_required
def profile(request):
    user = request.user

    context = {
        'user': user,
        'port': user.portfolio_set.first(),
        'value': user.portfolio_set.first().value,
        'net': user.portfolio_set.first().net_worth(),
        'asset': user.portfolio_set.first().assets.all(),
        'principal': user.portfolio_set.first().principal_sum

    }
    return render(request, 'main_app/profile.html', context)


@login_required
def my_assets(request):
    user = request.user

    context = {
        'user': user,
        'port': user.portfolio_set.first(),
        'value': user.portfolio_set.first().value,
        'net': user.portfolio_set.first().net_worth(),
        'asset': user.portfolio_set.first().assets.all(),
        'principal': user.portfolio_set.first().principal_sum

    }
    return render(request, "main_app/assets.html", context)
