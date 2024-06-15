from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+ '&units=metric&appid=0540c9870c7a44f472373b945d3f51fb').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) +'°C',
            "description": str(json_data['weather'][0]['main']),
            "pressure": str(json_data['main']['pressure']) + 'hPa',
            "humidity": str(json_data['main']['humidity']) + '%',

        }
    else:
        city = ''
        data = ''
    return render(request, 'index.html', {'city':city, 'data': data})