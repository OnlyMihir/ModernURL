from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<str:sh_id>',views.shurl,name='shortened urls'),
    path('accounts/', include('accounts.urls')),
    path('services/', include('services.urls'))
]