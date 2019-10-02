from django.shortcuts import render, redirect
from services.models import shortenedurl,ent_url_data
from ipware import get_client_ip
from ipdata import ipdata

ipdata = ipdata.IPData('6e5377b93bec490ff6500b084cba36f1c025a0c9057215a082636d3d')

# Create your views here.
def home(request):
    return render(request,"home.html")

def shurl(request,sh_id):
    if shortenedurl.objects.filter(sh_url=sh_id,is_ent_user=True).exists():
        client_ip, is_routable = get_client_ip(request)
        response = ipdata.lookup(client_ip, fields=['continent_name','country_name','region','city','postal','time_zone'])
        data = ent_url_data(sh_url=sh_id,continent=response['continent_name'],state_region=response['region'],country=response['country_name'],city=response['city'],postal_code=response['postal'],date_time=response['time_zone']['current_time'])
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