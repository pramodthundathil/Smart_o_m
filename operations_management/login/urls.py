from django.urls import path
from.import views

urlpatterns = [

    path('',views.logindisplay,name= 'logindisplay'),
    path('registration',views.registration,name='registration'),
    path('register',views.register, name= 'register'),
    path('login',views.login_main, name='login'),
    path('logout',views.logout, name='logout'),

    # path('hradmin',views.hradmin,name='hradmin'),
    
]
