from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2

# Create your views here.
def home(request):
    message = request.GET.get('id')
    print(message)
    client_ip = request.META['REMOTE_ADDR']
    print(client_ip)
    return render(request,"home.html")