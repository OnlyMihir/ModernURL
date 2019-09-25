from django.urls import path

from . import views

urlpatterns = [
    path('shortenurl',views.shortenurl,name='shortenurl'),
    path('myaccount',views.myaccount,name='My Account'),
    path('mylinks',views.mylinks,name='My Links')
]