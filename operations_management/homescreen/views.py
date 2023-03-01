from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import values

# Create your views here.

# Displaying Home screen after Log in
def home(request):
    result = values.objects.all()
    return render(request,'index.html')
    
# Home Button RETURN TO home
def homebutton(request):
    return redirect('home')

def contacts(request):
    return render(request,'contacts.html')