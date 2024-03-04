from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        UN=request.POST['username']
        PW=request.POST['password']
        user=auth.authenticate(username=UN, password=PW)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        FN=request.POST['first_name']
        LN=request.POST['last_name']
        PASS=request.POST['password']
        CPASS=request.POST['cpassword']
        email=request.POST['email']
        if PASS==CPASS:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"Email already exists")
                 return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=PASS,first_name=FN,last_name=LN,email=email)
                user.save();
                return redirect('login')
                print('user created')

        else:
            messages.info(request,"Password does not Match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
