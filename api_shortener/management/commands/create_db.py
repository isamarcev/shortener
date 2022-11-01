from django.core.management import BaseCommand
from api_shortener.views import client, collection, db
from shortener.settings import env
import pymongo

one_day = 60*60*24


class Command(BaseCommand):
    help = "create DB and table from .env file"

    def handle(self, *args, **options):
        db.create_collection(env('DB_COLLECTION'), capped=True, max=1000000,
                             size=1000000)
        db[env('DB_COLLECTION')].create_index([('expireAt', 1)],
                                              expireAfterSeconds=2)
        # collection.create_index('expireAt',
        #                         expireAfterSeconds=0)
        collection.create_index([('key', pymongo.ASCENDING)], unique=True)






