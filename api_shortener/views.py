import string
from random import choice

import pymongo
from django.http import HttpResponseRedirect

from shortener.settings import env
# Create your views here.

client = pymongo.MongoClient(env('MONGO_STRING'))
db = client[env('DB_NAME')]
collection = db[env('DB_COLLECTION')]

def generate_key():
    chars = string.digits + string.ascii_letters
    print(chars)
    key = ''.join([choice(chars) for _ in range(5)])
    return key, chars

data_model = { '_id': int, 'url': 'https...', 'key': 'short_url',
               'expireAt': 'Date', 'IP': 'ip', 'counter': int }


def index(request, key):
    url = collection.find_one({'url': key})
    return HttpResponseRedirect(url['key'])