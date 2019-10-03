from django.shortcuts import render, redirect
from django.contrib import messages
from services.models import shortenedurl,ent_url_data
import random,string
from accounts.models import IUser,EUser

# Create your views here.
def shortenurl(request):
    if request.method == 'POST':
        if request.session['is_ent_user'] is True:
            org_url = request.POST['org_url']
            desc = request.POST['desc']
            user_id=request.session['user_id']
            if shortenedurl.objects.filter(org_url=org_url,user_id=user_id).exists():
                messages.info(request, 'This url is already shortened')
                return redirect('shortenurl')
            else:
                flag=0
                while(flag!=1):
                    sh_url=''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                    if shortenedurl.objects.filter(sh_url=sh_url).exists():
                        flag=0
                    else:
                        flag=1
                data = shortenedurl(org_url=org_url,sh_url=sh_url,user_id=user_id,is_ent_user=True,desc=desc)
                data.save()
                return redirect('/mylinks')
        else:
            org_url = request.POST['org_url']
            desc = request.POST['desc']
            user_id=request.session['user_id']
            if shortenedurl.objects.filter(org_url=org_url,user_id=user_id).exists():
                messages.info(request, 'This url is already shortened')
                return redirect('shortenurl')
            else:
                flag=0
                while(flag!=1):
                    sh_url=''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                    if shortenedurl.objects.filter(sh_url=sh_url).exists():
                        flag=0
                    else:
                        flag=1
                data = shortenedurl(org_url=org_url,sh_url=sh_url,user_id=user_id,is_ent_user=False,desc=desc)
                data.save()
                return redirect('/services/mylinks')
    else:
        return render(request, 'ShortenLinks.html')

def myaccount(request):
    if(request.session['is_ent_user']==False):
        user_id = request.session['user_id']
        user_data=IUser.objects.get(id=user_id)
        dict={'email':user_data.email}
    else:
        user_id = request.session['user_id']
        user_data=EUser.objects.get(id=user_id)
        dict={'email':user_data.email}
        return render(request, 'MyAccount.html',dict)

def mylinks(request):
    user_id = request.session['user_id']
    if(request.session['is_ent_user']==False):
        url_data=shortenedurl.objects.filter(user_id=user_id,is_ent_user=False).values()
    elif(request.session['is_ent_user']==True):
        url_data=shortenedurl.objects.filter(user_id=user_id,is_ent_user=True).values()
    return render(request,'MyLinks.html',{'user_data':url_data})

def linkstats(request):
    if request.method=='POST' and 'btnform1' in request.POST:
        url_data=ent_url_data.objects.filter(sh_url=request.POST['link_id']).values()
        return render(request,'LinkStats.html',{'user_data':url_data})
    if request.method=='POST' and 'btnform2' in request.POST:
        return redirect('/')