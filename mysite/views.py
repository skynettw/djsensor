from django.shortcuts import render
import random
from mysite.models import SensorData
#import board
#import adafruit_dht

#dht11 = adafruit_dht.DHT11(board.D4)

def index(request):

    data = SensorData.objects.all()[:15]
    temperature = SensorData.objects.filter(name="溫度")[0].value
    humidity = SensorData.objects.filter(name="濕度")[0].value
    return render(request, "index.html", locals())

def lucky(request):
    no = random.randint(1, 49)
    return render(request, "lucky.html", locals())
