from django.urls import path
from.import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('homebutton',views.homebutton,name= 'homebutton'),
    path('contacts',views.contacts,name='contacts'),
]
