from django.core.management import BaseCommand
from api_shortener.views import client, collection, db
from shortener.settings import env
import pymongo

one_day = 60*60*24


class Command(BaseCommand):
    help = "create DB and table from .env file"

    def handle(self, *args, **options):
        db.createCollection(env('DB_COLLECTION'), {'max': 1000000})
        collection.create_index([('expireAt', pymongo.DESCENDING)],
                                expireAfterSeconds=one_day*90)
        collection.create_index([('key', pymongo.ASCENDING)], unique=True)






