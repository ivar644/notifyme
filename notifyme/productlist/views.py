from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from productdetail.models import productdetails
def productlist(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            id=request.user.id
            l=productdetails.objects.filter(userid=id)
            return render(request,'productlist.html',{'l':l})
        else:
            return redirect('login')

def delete(request):
    pass