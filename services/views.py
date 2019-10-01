from django.shortcuts import render, redirect
from django.contrib import messages
from services.models import shortenedurl
import random,string
from accounts.models import IUser

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
                return redirect('/mylinks')
    else:
        return render(request, 'ShortenLinks.html')

def myaccount(request):
    user_id = request.session['user_id']
    user_data=IUser.objects.get(id=user_id)
    dict={'email':user_data.email}
    return render(request, 'MyAccount.html',dict)

def mylinks(request):
    user_id = request.session['user_id']
    user_data=shortenedurl.objects.filter(user_id=user_id).values()
    return render(request,'MyLinks.html',{'user_data':user_data})