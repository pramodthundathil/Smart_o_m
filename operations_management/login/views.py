from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http.response import HttpResponse
# from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import employee


# Create your views here.

# login screen display-------------------------------------------------

def logindisplay(request):

    return render(request,'login.html')
    
# Registration screen display-------------------------------------------

def registration(request):
    name = request.session['user_name']
    password = request.session['password']

    if employee.objects.filter(user_name = name, password= password,department = 'Admin'):
        return render(request,'registration.html')

    else:
        messages.info(request,'No access!!!!!')
        return redirect('home')

# registration submission-------------------------------------------------
def register(request):
    
    if request.method == 'POST':
        
        user_name = request.POST['uname']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        em_title = request.POST['etitle']
        password1 = request.POST['password']
        password2 = request.POST['password_c']
        email = request.POST['email']
        phone_number = request.POST['phonenumber']
        department = request.POST['Department']

        if password1==password2 and password1 != "":
            if employee.objects.filter(user_name=user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif employee.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = employee.objects.create(user_name = user_name, password = password1, email = email,first_name = first_name,last_name=last_name,department = department,phone_number=phone_number,emp_title= em_title)
                user.save();
                print('user created')
                return redirect('logindisplay')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
    
    else:
        return render(request,'registration.html')


# LogIN-------------------------------------------------------------------------

def login_main(request):

    global username
    global password
    
    
    if request.method=='POST':

        result = employee.objects.all()
        username=request.POST['username']
        password=request.POST['password']
        useragent = employee.objects.filter(user_name = username,password= password).exists()
        if useragent is True:
            request.session['user_name'] = username
            request.session['password'] = password
            request.session['useragent'] = useragent 
            user_id = employee.objects.get(user_name = username, password = password)
            request.session['user_id'] = user_id.id

        if employee.objects.filter(user_name = username,password= password):
            messages.info(request,'Welcome '+ username)
            return redirect('home')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')
             
# logOut----------------------------------------------------------------------------

def logout(request):
    return redirect('/')

