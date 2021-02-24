from django.shortcuts import render
import main_app
from .models import Portfolio, Asset
# from django.contrib.auth.models import User
from django.contrib import auth
import json
import requests
import urllib.request
from django.contrib.auth.decorators import login_required
from . import asset_search as search
from . import testdata
from django.core import serializers
from . import testdata as td
from django.http import JsonResponse, response
from cryptocompy.price import get_current_trading_info, get_current_price


profile_URL = "https://randomuser.me/api/"


def test_page(request):  # A diagnostic page to view incoming and db update data
    #
    #     user = request.user
    #     assets = user.portfolio_set.first().assets.all()
    #
    #     context = {
    #         'assets': assets,
    #         'user': user,
    #         'net': user.portfolio_set.first().net_worth(),
    #
    #     }
    coin = 'dash'
    fiat = "USD"
    result = search.coin_search(coin)

    context = {
        'name': result['name'],
        'price': result['price'],
        'desc': result['desc'],
        'img': result['img'],
    }

    return render(request, "main_app/test.html", context)


@login_required
def index(request):
    data = requests.get(profile_URL, {'results': 'gender'})
    response = data.json()
    pic = response['results'][0]['picture']['large']
    user = request.user
    context = {
        'profile_pic': pic,
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
