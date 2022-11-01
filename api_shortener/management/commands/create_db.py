from django.core.management import BaseCommand
from api_shortener.views import collection
import pymongo

one_day = 60*60*24


class Command(BaseCommand):
    help = "set the collection from .env file, set indexes and auto deleting"

    def handle(self, *args, **options):
        collection.create_index(
            [('expireAt', pymongo.DESCENDING)], expireAfterSeconds=0)
        collection.create_index([('key', pymongo.ASCENDING)], unique=True)






