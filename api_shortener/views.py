import string
from random import choice
from datetime import datetime, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response

import pymongo
from django.http import HttpResponseRedirect, JsonResponse

from shortener.settings import env, ALLOWED_HOSTS
# Create your views here.

client = pymongo.MongoClient(env('MONGO_STRING'))
db = client[env('DB_NAME')]
collection = db[env('DB_COLLECTION')]

def generate_key():
    chars = string.digits + string.ascii_letters
    key = ''.join([choice(chars) for _ in range(5)])
    elements = collection.find_one({'key': key})
    if not elements:
        return key
    else:
        return generate_key()

data_model = { '_id': int, 'url': 'https...', 'key': 'short_url',
               'expireAt': 'Date', 'IP': 'ip', 'counter': int }


def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request, key):
    url = collection.find_one({'key': key})
    new_count = url['counter'] + 1
    collection.update_one({'key': key}, {'$set':
                                            {'counter': new_count}})
    return HttpResponseRedirect(url['url'])


class ShortUrlViewSet(APIView):

    def check_permissions(self, request):
        pass

    def get(self, request):
        """Get info by IP"""
        ip = get_ip_address(self.request)
        list_date = collection.find({'ip': ip}, {'_id': False})
        answer = [value for value in list_date]
        return Response(answer)

    def post(self, request):
        """Create shortURL"""
        data = dict()
        data['url'] = request.POST.get('url')
        data['key'] = generate_key()
        date = request.POST.get('expireAt')
        if not date:
            date = datetime.now() + timedelta(days=90)
        data['expireAt'] = date
        data['ip'] = get_ip_address(request)
        data['counter'] = 0
        collection.insert_one(data)
        return JsonResponse({'short_url': f'{ALLOWED_HOSTS[0]}:8000/{data["key"]}/'})
