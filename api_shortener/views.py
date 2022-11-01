import string
from random import choice
from datetime import datetime, timedelta
import re

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect

import pymongo

from shortener.settings import env


client = pymongo.MongoClient(env('MONGO_STRING'))
db = client[env('DB_NAME')]
collection = db[env('DB_COLLECTION')]


class MainPageView(TemplateView):
    template_name = 'api_shortener/main_page.html'

    def get(self, request, *args, **kwargs):
        exist = request.GET.get('exist')
        if exist:
            context = {'doesnotexists': True}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name)


def redirect(request, key):
    url = collection.find_one({'key': key})
    if len(key) != 5 or not url:
        return HttpResponseRedirect(
            f'{reverse_lazy("start_page")}?exist=False')
    new_count = url['counter'] + 1
    collection.update_one({'key': key}, {'$set':
                                             {'counter': new_count}})
    return HttpResponseRedirect(url['url'])


def generate_key():
    """Generate unique key"""
    chars = string.digits + string.ascii_letters
    key = ''.join([choice(chars) for _ in range(5)])
    elements = collection.find_one({'key': key})
    if not elements:
        return key
    else:
        return generate_key()


url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"


def validation_link(link):
    result = re.match(url_pattern, link)
    return result


def validation_date(date):
    if all([date.isdigit(), int(date) < 365, int(date) > 1]):
        return date


def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ShortUrlViewSet(APIView):

    def check_permissions(self, request):
        pass

    def get(self, request):
        """Get info by IP and return all link for this user"""
        ip = get_ip_address(self.request)
        list_date = collection.find({'ip': ip}, {'_id': False})
        answer = [value for value in list_date]
        return Response(answer)

    def post(self, request):
        """Create shortURL and dump to DB"""
        data = dict()
        errors = dict()
        url = request.POST.get('url')
        if validation_link(url):
            data['url'] = request.POST.get('url')
        else:
            errors['url'] = 'Incorrect URL entered'
        data['key'] = generate_key()
        expire_at = request.POST.get('expireAt')
        if expire_at:
            if not validation_date(expire_at):
                errors['expireAt'] = 'Entered incorrect date. Please try more'
        else:
            expire_at = 90
        data['ip'] = get_ip_address(request)
        data['counter'] = 0
        if errors:
            return Response({'errors': errors})
        data['expireAt'] = datetime.utcnow() + timedelta(
            days=int(expire_at))
        collection.insert_one(data)
        return Response(
            {'short_url': f'{request.get_host()}/{data["key"]}/'})
