from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import HttpResponse
from django.contrib import messages
from login import models, views

# Create your views here.
# display Approvel screen-----------------------------------------------------
def approvals(request):
    return render (request,'approvels.html')




# leave approvels-------------------------------------------------------------

def leave_approve(request):
    name = request.session['user_name']

    if models.employee.objects.filter(user_name = name, department = 'Admin'):
        leaves = models.leave.objects.all()
        return render(request,'approvels_leaves.html',{'leaves':leaves})

    else:
        messages.info(request,'No acces')
        return redirect('approvals')

def leave_aprv(request):
    emid = request.POST['em_id']

    leave_status = models.leave.objects.get(emp_id = emid)

    if leave_status.approve_status == False:

        leave_status.approve_status = True
        leave_status.save()
        return redirect('leave_approve')

    else:
        leave_status.approve_status = False
        leave_status.save()
        return redirect('leave_approve')

# leave status dispaly--------------------------------------------------------
def leave_status(request):
    name = request.session['user_name']
    employee = models.employee.objects.get(user_name = name)
    staff_id = employee.id
    
    empolye_leave = models.leave.objects.filter(emp_id = staff_id)
    return render(request,'leave_status.html',{"empolye_leave":empolye_leave})






    



