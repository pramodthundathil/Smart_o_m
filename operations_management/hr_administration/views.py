from django.contrib.messages.api import info
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import HttpResponse
from django.contrib import messages
from login import models,views



# Create your views here.

# Hr admin screen----------------------------------------------------------------- 

def hradmin(request):
    # name = request.session['user_name']
    # password = request.session['password']
    
    # if models.employee.objects.filter(user_name = name, password= password,department = 'Admin'):
    return render(request,'hr_admin.html')
        
    # elif models.employee.objects.filter(user_name = name, password= password,department = 'HR'):
        
    #     return render(request,'hr_admin.html')
    # else:
    #     messages.info(request,"No access")
    #     return redirect('home')

# employee administration----------------------------------------------------------
# display screens====================
def employee(request):
    name = request.session['user_name']
    password = request.session['password']

    if models.employee.objects.filter(user_name = name, password= password,department = 'Admin'):
        return render(request,'employee.html')

    elif models.employee.objects.filter(user_name = name, password= password,department = 'HR'):
        return render(request,'employee.html')
    else:
        messages.info(request,"No access")
        return redirect('hradmin')

# adding new employe screen display

def add_emp_screen(request):

    return render(request,'add_employee.html')


def update_employe_display(request):
    result = models.staff.objects.all()
    return render(request,"update_employe.html",{"result":result})

def update_employe(request):
    global emid
    emid = request.POST['em_id']
    employe_list = models.staff.objects.filter(emp_id = emid)

    return render(request,'emp_update.html',{'employe':employe_list})

def delete_emp(request):
    result = models.staff.objects.all()
    return render(request,"emp_delete.html",{"result":result})

def employee_leave(request):
    return render(request,'leave_manage.html')

#newsletter screen--------------------------------------------------------------------

def hr_newsletters(request):
    
    msgs = models.dashboard.objects.all()

    return render(request,'hr_news_letter.html',{'msgs':msgs})




# Addin a new employe------------------------------------------------------------------

def Add_employee(request):

    if request.method =='POST':
        name = request.POST['sname']
        emptitle = request.POST['etitle']
        doj = request.POST['doj']
        pnumber = request.POST['phonenumber']
        department = request.POST['department']
        dob = request.POST['dob']
       
        employ = models.staff.objects.create(staff_name = name, emp_title=emptitle,department_id = department, phone = pnumber,date_of_join=doj,DOB = dob)
        employ.save()
        messages.info(request,"Employe Added Successfully")
        return redirect('employee')
    else:
        messages.info(request,"Not allowed")
        return redirect('employee')

# Update employes-------------------------------------------------------------------------
def update_data(request):
    # empid = request.session['emp_id ']
    updated_employe = models.staff.objects.get(emp_id = emid)
    updated_employe.emp_title = request.POST['etitle']
    updated_employe.department_id = request.POST['department']
    updated_employe.DOB = request.POST['dob']
    updated_employe.date_of_join = request.POST['doj']
    updated_employe.phone = request.POST['phone']
    updated_employe.save()

    messages.info(request,'Employee Details Updated')
    return redirect('update_employe')

def delete_employe(request):
    empl_id = request.POST['em_id']
    delete_empl = models.staff.objects.get(emp_id = empl_id)
    delete_empl.delete()
    messages.info(request,'Employe Deleted Successfully')
    return redirect('employee')

# Leave apply----------------------------------------------------------------------------------

def apply_leave(request):
    name = request.session['user_name']
    password = request.session['password']

    if models.employee.objects.filter(user_name = name, password= password,department = 'Admin'):
        employe = models.employee.objects.filter(user_name = name)
        return render(request,'leave_apply.html',{'employe':employe})
    else:
        employe = models.employee.objects.filter(user_name = name)
        return render(request,'leave_apply.html',{'employe':employe})


def Add_leave(request):
    
    em_id = request.POST['e_id']
    first_name = request.POST['fname']
    title = request.POST['etitle']
    l_start = request.POST['leave_s_date']
    l_end  = request.POST['leave_e_date']
    department = request.POST['department']

    if models.leave.objects.filter(emp_id = em_id).exists():
        messages.info(request,'Leave already applied for Approvel')
        return redirect('apply_leave')

    else:
        leave_date = models.leave.objects.create(staff_name = first_name,employee_title = title, emp_id = em_id, department = department, leave_start = l_start, leave_end = l_end)
        leave_date.save()
        messages.info(request,'Leave Submitted for Approvel')
        return redirect('employee_leave')

 #sendin message database and dashboard-----------------------------------------       

def add_message(request):

    text = request.POST['textarea']

    message = models.dashboard.objects.create(message= text)
    message.save()

    messages.info(request,'message has been sent to dash board')
    return redirect('hradmin')

def delete_msg(request):

    mesg = request.POST['messag']
    msg_del = models.dashboard.objects.get(msg_id=mesg)
    msg_del.delete()

    messages,info(request,'message deleted')
    return redirect('hr_newsletters')

#dash doard screen-------------------------------------------------------------------

def dashboard(request):

    msgs = models.dashboard.objects.all()

    return render(request,'dashboard.html',{'msgs':msgs})




    

    






    



 

     



