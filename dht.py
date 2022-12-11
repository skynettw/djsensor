import os
import django
import adafruit_dht
import board
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj.settings')
django.setup()
from mysite.models import SensorData

try:
    dht11 = adafruit_dht.DHT11(board.D4)
    t = dht11.temperature
    h = dht11.humidity
    data = SensorData(name="溫度", place="A304研究室", value=t)
    data.save()
    data = SensorData(name="濕度", place="A304研究室", value=h)
    data.save()
    print(t, h)
except:
    dht11.exit()
