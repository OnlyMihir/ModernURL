from django.shortcuts import render, redirect
from services.models import shortenedurl,ent_url_data
from datetime import datetime
from ipware import get_client_ip
import requests as rq
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request,"home.html")

def shurl(request,sh_id):
    if shortenedurl.objects.filter(sh_url=sh_id,is_ent_user=True).exists():
        client_ip, is_routable = get_client_ip(request)
        url="https://whatismyipaddress.com/ip/"+client_ip
        r=rq.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.findAll("table")
        continent=''
        state_region=''
        country=''
        city=''
        postal_code=''
        for row in table[1].findAll("tr"):
            ls=row.get_text().split(':')
            if(str(ls[0])=='Continent'):
                continent=ls[1]
            if(str(ls[0])=='State/Region'):
                state_region=ls[1]
            if(str(ls[0])=='Country'):
                country=ls[1]
            if(str(ls[0])=='City'):
                city=ls[1]
            if(str(ls[0])=='Postal Code'):
                postal_code=ls[1]
        data = ent_url_data(sh_url=sh_id,continent=continent,state_region=state_region,country=country,city=city,postal_code=postal_code,date_time=datetime.today)
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