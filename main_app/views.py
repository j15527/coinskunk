from django.shortcuts import render, redirect, reverse
import main_app
from django.http import HttpResponse
from .models import Portfolio, Asset
# from django.contrib.auth.models import User
from django.contrib import auth
import json
import requests
import urllib.request
from django.contrib.auth.decorators import login_required
from . import asset_search as search
from django.http import JsonResponse, response
from cryptocompy.price import get_current_trading_info, get_current_price
from . import update_data as up
from . import add_asset

# from . import Add_asset as add
profile_URL = "https://randomuser.me/api/"


def coin_name(name):
    return name


searched_str = ""  # GLOBAL VARIABLE - BE CAREFUL!!!


def search_asset(request):
    result = {}
    try:
        if request.GET.get('search-btn'):
            result = search.coin_search(request.GET.get("search-box"))
            global searched_str  # YES I KNOW THIS IS BAD!!!!!!!!!!!!!
            searched_str = result['name']
            context = {
                'name': result['name'],
                'price': result['price'],
                'desc': result['desc'],
                'img': result['img'],
            }

            return render(request, "main_app/add-search.html", context)
    except KeyError:
        context = {
            'img': 'static/img/question-mark.png'
        }
        return render(request, "main_app/add-search.html")
    except TypeError:
        return HttpResponse("<http><body> <h1><p> Incorrect input in search field.  </p></h1></body></http>")


@login_required
def index(request):
    up.update(request)
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
        'principal': user.portfolio_set.first().principal_sum,
        'logo': pic,

    }
    return render(request, 'main_app/index.html', context)


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


def add(request):
    try:
        if request.GET.get('add-btn'):
            print("adding asset...")
            count = request.GET.get('count')
            img = request.GET.get('img')
            asset = add_asset.add_asset(request, searched_str, count)
            print(f'Added {count} of {searched_str}')
            user = request.user
            context = {
                'user': user,
                'port': user.portfolio_set.first(),
                'value': user.portfolio_set.first().value,
                'net': user.portfolio_set.first().net_worth(),
                'assets': user.portfolio_set.first().assets.all(),
                'principal': user.portfolio_set.first().principal_sum,
                'search': searched_str,

            }
            return render(request, "main_app/assets.html", context)
    except KeyError:
        return HttpResponse("<http><body> <h1><p> No Such Coin </p></h1></body></http>")
    except TypeError:
        return HttpResponse("<http><body> <h1><p> Incorrect input in search field.  </p></h1></body></http>")


@login_required
def my_assets(request):
    up.update(request)
    # print(searched_str)
    user = request.user
    context = {
        'user': user,
        'port': user.portfolio_set.first(),
        'value': user.portfolio_set.first().value,
        'net': user.portfolio_set.first().net_worth(),
        'assets': user.portfolio_set.first().assets.all(),
        'principal': user.portfolio_set.first().principal_sum,
        'search': searched_str,

    }

    return render(request, "main_app/assets.html", context)
