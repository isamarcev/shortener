import pymongo
from django.shortcuts import render
from pymongo import MongoClient
from shortener.settings import env
# Create your views here.

client = pymongo.MongoClient(env('MONGO_STRING'))
db = client[env('DB_NAME')]
collection = db[env('DB_COLLECTION')]

