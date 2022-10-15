from django.urls import path
from . import views
urlpatterns = [
    path('', views.productlist,name='productlist'),
    path('delete', views.delete, name = 'delete')

]