from django.shortcuts import render, redirect
from services.models import shortenedurl,ent_url_data
from datetime import datetime
from ipware import get_client_ip
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request,"home.html")

def shurl(request,sh_id):
    if shortenedurl.objects.filter(sh_url=sh_id,is_ent_user=True).exists():
        client_ip, is_routable = get_client_ip(request)
        continent=''
        state_region=''
        country=''
        city=''
        postal_code=''
        time=''
        payload = {"api-key": "test"}
        url='https://api.ipdata.co/'
        url=url+str(client_ip)
        response = requests.get(url, params=payload).json()
        for key in response:
            if key in 'continent_name':
                continent = response[key]
            if key in 'region':
                state_region = response[key]
            if key in 'city':
                city = response[key]
            if key in 'country_name':
                country = response[key]
            if key in 'postal':
                postal_code = response[key]
            if key in 'time_zone':
                t=response[key]
                time=t['current_time']
        data = ent_url_data(sh_url=sh_id,continent=continent,state_region=state_region,country=country,city=city,postal_code=postal_code,date_time=time)
        data.save()
        url_data=shortenedurl.objects.get(sh_url=sh_id,is_ent_user=True)
        return redirect(url_data.org_url)
    elif shortenedurl.objects.filter(sh_url=sh_id,is_ent_user=False).exists():
        url_data=shortenedurl.objects.get(sh_url=sh_id)
        dict={'orgurl':url_data.org_url}
        print(url_data.org_url)
        return render(request,"servead.html",dict)
    else:
        return render(request,"error404.html")