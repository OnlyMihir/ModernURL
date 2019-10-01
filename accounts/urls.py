from django.urls import path

from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register_ent',views.registerent,name='register enterprise user'),
    path('login_ent',views.loginent,name='login enterprise user')
]