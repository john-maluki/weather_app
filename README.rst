=====
weather
=====
weather is a simple django app that used to show weather state 
valid cities around the world
-----------
1. Add "weather" to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
...
'weather',
]
2. Include the polls URLconf in your project urls.py like this::
path('/', include('weather.urls')),
3. Run 'python3 manage.py migrate 'to create the City models.
