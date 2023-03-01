from django.contrib import messages
from django.shortcuts import render,redirect 
from django.http import HttpResponse
from login import models, views
from .forms import ConveyanceaddForm, WorkAddForm
from .models import Conveyane,Works
from .decorators import allowed_users


# Create your views here.

# Admin screen Display-------------------------------------------------------------

def accountadmin(request):
    
    name = request.session['user_name']
    password = request.session['password']

    # if models.employee.objects.filter(user_name= name, password = password, department = 'Account'):
        
    return render(request,'account_admin.html')

    # elif models.employee.objects.filter(user_name= name, password = password, department = 'Admin'):

        # return render(request,'account_admin.html')

    # else:
    #     messages.info(request,'No acces')
    #     return redirect('home')

def conveyance(request):
    return render(request,'Conveyance.html')

def addcoveyance(request):
    form = ConveyanceaddForm()
    if request.method == "POST":
        name = request.session['user_name']
        form = ConveyanceaddForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.username = name
            data.save()
            messages.info(request,"Coveyanvce added")
            
    return render(request,"addconveyance.html",{"form":form})

@allowed_users(allowed_roles=["Admin","Account"])
def ConveyanceApprove(request):
    convey = Conveyane.objects.all()
    return render(request,"conveyanceapprove.html",{"coveyance":convey})

@allowed_users(allowed_roles=["Admin","Account"])
def conveyancechange(request,pk):
    con = Conveyane.objects.get(id= pk)
    if con.status == False:
        con.status = True
    else:
        con.status = False
    con.save()
    return redirect("ConveyanceApprove")


def WorkReports(request):
    return render(request,"workreports.html")

@allowed_users(allowed_roles=["Admin","Managemant"])
def AddWork(request):
    form = WorkAddForm()
    if request.method == "POST":
        name = request.session['user_name']
        form = WorkAddForm(request.POST)
        if form.is_valid():
            work = form.save()
            work.manager = name
            work.save()
            messages.info(request,"work is assigned")
            return redirect("WorkReports")
    return render(request,"addwork.html",{"form":form})

def AllWorks(request):
    work = Works.objects.all()
    return render(request,"allworks.html",{"work":work})

@allowed_users(allowed_roles=["Admin","Managemant"])
def DeleteWork(request,pk):
    Works.objects.get(id = pk).delete()
    messages.info(request,"work deleted")
    return redirect('AllWorks')

def TakeWork(request,pk):
    work = Works.objects.filter(id = pk)
    if request.method == "POST":
        id = request.POST['id']
        discription = request.POST["work"]
        status = request.POST["status"]
        works = Works.objects.get(id = pk)
        works.WorkDiscription = discription
        works.status = status
        works.save()
        messages.info(request,"Work Updated")
        return redirect('AllWorks')
        
    return render(request,"workupdate.html",{"work":work})
    
    




