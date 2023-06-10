from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Market
from django.shortcuts import render
from .forms import TimeFilterForm, AddressFilterForm
from .filters import FilterMarketInfo
import requests
import json
from django.core.cache import caches, cache
from datetime import datetime
import re
import environ

env = environ.Env()
environ.Env.read_env()

def markets(request):
  
  mymarket = get_update(request)
  template = loader.get_template('homepage.html')
  context = {
    'mymarket': mymarket,
  }
  return HttpResponse(template.render(context, request))

def get_update(request):
  # Check if the data is already cached
  cached_data = cache.get('market_data')

  if cached_data is not None:
      # Data is cached, return the cached response
      print("get_update() is cached!")
      return cached_data
  
  print("get_update() not cache!")
  # The API endpoint
  fromBlock = env("FROMBLOCK")
  topic0 = env("TOPIC0")
  apikey = env("APIKEY")
  url = "https://api.etherscan.io/api"
  params = {'module':'logs',
              'action':'getLogs',
              'fromBlock': fromBlock,
              'topic0': topic0,
              'page': '1',
              'offset':'1000',
              'apikey': apikey
              }
  r = requests.get(url,params)
  if r.status_code == requests.codes.ok:
        print("OK")
        response_dict = json.loads(r.text)
        markets = response_dict['result']
        Market.objects.all().delete()  #Clear the existing data in the Market table
        for market in markets:
            new_market = Market(
                timestamp=market['timeStamp'],
                transactionhash=market['transactionHash'],
                address=market['address']
            )
            new_market.save()
        mymarket = Market.objects.all().values()
        cache.set('market_data', mymarket, 10)
  return mymarket

def filter_time(request):
    error = None
    form = TimeFilterForm(request.POST or None)
    mymarket = []
    if request.method == 'POST' and form.is_valid():
        timestamp = form.cleaned_data['filter_time']
        if not re.match(r'^0x[0-9a-fA-F]+$', timestamp):
          error = "Error: Invalid timestamp format"
          mymarket = Market.objects.all()
        else:
          mymarket = Market.objects.filter(timestamp__lt=timestamp)

    context = {
        'form': form,
        'mymarket': mymarket,
        'error': error
    }
    
    return render(request, 'homepage.html', context)

def filter_address(request):
    error = None
    form = AddressFilterForm(request.POST or None)
    mymarket = []
    if request.method == 'POST' and form.is_valid():
        address = form.cleaned_data['filter_address']
        if not re.match(r'^0x[0-9a-fA-F]+$', address):
            error = "Error: Invalid address format"
            mymarket = Market.objects.all()
        else:
          mymarket = Market.objects.filter(address=address)
    context = {
        'form': form,
        'mymarket': mymarket,
        'error': error
    }
    return render(request, 'homepage.html', context)