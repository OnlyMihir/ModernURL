from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import IUser
from ipware import get_client_ip

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
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        client_ip, is_routable = get_client_ip(request)
        if client_ip is None:
             messages.info(request,'Unable to get the clients IP address')
        else:
            #We got the client's IP address
            if is_routable:
                #i, r = get_client_ip(request, request_header_order=['X_FORWARDED_FOR'])
                messages.info(request,client_ip)
                # The client's IP address is publicly routable on the Internet
            else:
                messages.info(request,"The client's IP address is private")
        # Order of precedence is (Public, Private, Loopback, None)
        return render(request, 'login.html')

def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return redirect('/')