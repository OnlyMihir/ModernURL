from django.shortcuts import render, redirect
from django.contrib.gis.geoip2 import GeoIP2
from services.models import shortenedurl

# Create your views here.
def home(request):
    return render(request,"home.html")

def shurl(request,sh_id):
    if shortenedurl.objects.filter(sh_url=sh_id).exists():
        url_data=shortenedurl.objects.get(sh_url=sh_id)
        dict={'orgurl':url_data.org_url}
        print(url_data.org_url)
        return render(request,"servead.html",dict)
    else:
        return render(request,"error404.html")