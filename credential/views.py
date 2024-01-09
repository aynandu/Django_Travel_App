from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def Register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_Name=request.POST['first_name']
        last_Name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password == cpassword :
            if User.objects.filter(username=username).exists():
                messages.info(request,"User Name Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email id already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_Name,last_name=last_Name,password=password,email=email)
                user.save()
                return redirect('login')

        else:
            messages.info(request,'Password error')
            return redirect('register')
        return  redirect('/')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['userName']
        password=request.POST['password']
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Not a Valid User')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')