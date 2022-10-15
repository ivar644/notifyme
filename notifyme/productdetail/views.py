from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from .models import productdetails

def productdetail(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            return render(request,'product.html')
        else:
            return redirect('login')
    else:
        name=request.POST['product']
        url=request.POST['url']
        mail=request.POST['email']
        price=request.POST['price']
        p=productdetails(name=name,url=url,email=mail,price=price,userid_id=request.user.id)
        p.save()
        return redirect('productlist')