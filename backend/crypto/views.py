from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from datetime import datetime
from .models import Price

# Create your views here.
class MyAPIView(APIView):
    def get(self, request, currency=''):
        # code to handle GET requests
        currency = request.GET.get('currency')
        current_url = "https://api.coincap.io/v2/rates/"+currency
        print(current_url)
        if (currency):
          current_rate = requests.get(current_url)
          historical_rate = requests.get("https://api.coincap.io/v2/assets/"+currency+"/history?interval=h1")
          if historical_rate.status_code == 200:
            data = historical_rate.json()
            time = datetime.now()
            date = datetime.now()
            res_arr = []
            # res_arr = [{'rate': current_rate.json()['data']['rateUsd'], 'id': current_rate.json()['data']['id']}]
            # res_arr.extend([{'rate': data['data'][-1]['priceUsd'], 'id': current_rate.json()['data']['id']}, {'rate': data['data'][-4]['priceUsd'], 'id': current_rate.json()['data']['id']}, {'rate': data['data'][-8]['priceUsd'], 'id': current_rate.json()['data']['id']}, {'rate': data['data'][-24]['priceUsd'], 'id': current_rate.json()['data']['id']}])
            res_arr.append([{'id': current_rate.json()['data']['id'], 'current_price': current_rate.json()['data']['rateUsd'], '1h_ago': data['data'][-1]['priceUsd'], '4h_ago': data['data'][-4]['priceUsd'], '8h_ago': data['data'][-8]['priceUsd'], '24h_ago': data['data'][-24]['priceUsd']}])
            print(res_arr)
            return Response(res_arr)
            # price, created = Price.objects.get_or_create(currency_name=current_rate.json()['data']['id'])

            # if price:
            #   price.current_price = current_rate.json()['data']['id']
            #   price.price_1h_ago = data['data'][-1].priceUsd
            #   price.price_4h_ago = data['data'][-4].priceUsd
            #   price.price_8h_ago = data['data'][-8].priceUsd
            #   price.price_24h_ago = data['data'][-24].priceUsd
            #   if current_rate.json()['data'].rateUsd > data['data'][-24].priceUsd:
            #     up_by = current_rate.json()['data'].rateUsd - data['data'][-24].priceUsd
            #   else:
            #     up_by = 0
            #   price.up_by = up_by
            #   price.time = time
            #   price.date = date
            #   price.save()
            # else:
            #   price = Price(currency_name=current_rate.json()['data']['id'],
            #         current_price=current_rate.json()['data'].rateUsd,
            #         price_1h_ago=data['data'][-1].priceUsd,
            #         price_4h_ago=data['data'][-4].priceUsd,
            #         price_8h_ago=data['data'][-8].priceUsd,
            #         price_24h_ago=data['data'][-24].priceUsd,
            #         up_by=up_by,
            #         time=time,
            #         date=date)
            #   price.save()
          
          # If the request failed, return an error message
          else:
              return Response({'error': 'Failed to retrieve data from external API'})
        else:
          return Response({'error': 'Did not receive currency'})
    
    def post(self, request):
        # code to handle POST requests
        return Response({'message': 'POST request processed.'})
