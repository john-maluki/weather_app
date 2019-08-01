import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm


# Create your views here.
def index (request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&Appid=e4288b0485a26cabc2e99a4b61562e32'
    # url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=e4288b0485a26cabc2e99a4b61562e32'
    # city = 'nairobi'
    err_msg = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_cities = City.objects.filter(name = new_city).count()
            
            if existing_cities == 0:
                r = requests.get(url.format(new_city)).json()
                
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'The city does not exist in the world'    
            else:
                err_msg = 'The city already exists in the database'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'                
    
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:   
        r = requests.get(url.format(city)).json()
        
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)


    
    #print(city_weather)
    context = {
        'weather_data' : weather_data,
         'form' : form,
         'message' : message,
         'message_class' : message_class
         }

    return render(request, 'weather/weather.html', context)



def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')