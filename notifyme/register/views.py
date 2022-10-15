from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.http import HttpResponse
def register(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['pass']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username taken")
        else:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
            user.save()
        return redirect('/register/login')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
