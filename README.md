# shortener - service for creating short url

For run on local you should to sign in for free to https://www.mongodb.com/atlas/database and create Cluster. 
You can use temporary email from https://temp-mail.org/ or your own email.

Then Button "Connect" --> "Connect using MongoDbCompass" --> Download and install.
Finally you need to connect to Cluster and get from MongoDB connection string like:
"mongodb+srv://samartsevihorv:<YOURPASSWORD>@cluster0.ysdzv9e.mongodb.net/test"

Then needed to create .env file in the root of project and fill next fields(example):
DEBUG=True
SECRET_KEY=django-insecure-@918ix*mr!#s-1(r*y*e*ys$=9kfdyd!$4ohr492p!jhec0pc0
MONGO_STRING=mongodb+srv://samartsevihorv:YOURPASSWORD@cluster0.ysdzv9e.mongodb.net/test
DB_NAME=SHORTENER
DB_COLLECTION=ShortenerCollection

Then go to projects folder and follow next commands: activate venv, install requirements, 
create DB, indexes and auto-delete, then run server by manage.py or Makefile.
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py create_db
$ python manage.py runserver (or) $ make r
```
____
  
## API interface
Functionality to work with API interface is: send request on HOSTNAME:PORT/api/shorter/.

  **GET request** without parameters returns list of created links by request`s IP address.
  
  **POST request** should contains from required field 'url' with long URL which you like to make shorter and non requered field 'expireAt' with number(!!!) from 1 to 365. This figure means the lifetime (storage of the link on the server) - dafault 90 days.
## Testing
For run testing needed install next package:
```
$ pip install pytest
$ pip install pytest-django
```
and then run:
```
$ pytest -v
```

