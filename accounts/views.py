from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import IUser,EUser

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['confirmp']
        email = request.POST['email_address']
        if password1 == password2:
            if IUser.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif IUser.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('register')
            else:
                user = IUser(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                messages.info(request, 'user succesfully created')
                return redirect('login')
        else:
            messages.info(request, 'passwords does not match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email=request.POST['email_address']
        password=request.POST['password']
        user=IUser.objects.filter(email=email,password=password).exists()
        if user is True:
            user_data=IUser.objects.get(email=email,password=password)
            request.session['user_id'] = user_data.id
            request.session['user_name'] = user_data.username
            request.session['is_ent_user'] = False
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    del request.session['is_ent_user']
    return redirect('/')

def registerent(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        org_name = request.POST['organization']
        password1 = request.POST['password']
        password2 = request.POST['confirmp']
        email = request.POST['email_address']
        if password1 == password2:
            if EUser.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif EUser.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('register')
            else:
                user = EUser(username=username,password=password1,org_name=org_name,first_name=first_name,last_name=last_name,email=email)
                user.save()
                messages.info(request, 'user succesfully created')
                return redirect('loginent')
        else:
            messages.info(request, 'passwords does not match')
            return redirect('/accounts/register_ent')
        return redirect('/')
    else:
        return render(request, 'register_ent.html')


def loginent(request):
    if request.method == 'POST':
        email=request.POST['email_address']
        password=request.POST['password']
        user=EUser.objects.filter(email=email,password=password).exists()
        if user is True:
            user_data=EUser.objects.get(email=email,password=password)
            request.session['user_id'] = user_data.id
            request.session['user_name'] = user_data.username
            request.session['is_ent_user'] = True
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/accounts/login_ent')
    else:
        return render(request, 'login_ent.html')