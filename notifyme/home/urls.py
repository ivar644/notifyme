from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('productdetail',views.productdetail,name='productdetail'),
    path('checkprice',views.checkprice,name='checkprice')
]