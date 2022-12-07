from django.shortcuts import render
import random
from mysite.models import SensorData

def index(request):

	data = SensorData.objects.all()
	
	return render(request, "index.html", locals())

def lucky(request):
	no = random.randint(1, 49)
	return render(request, "lucky.html", locals())