from django.urls import path
from.import views 

urlpatterns = [
    
    path('hradmin',views.hradmin,name='hradmin'),
    path('employee',views.employee,name ='employee'),
    path('add_emp_screen',views.add_emp_screen ,name= 'add_emp_screen'),
    path('Add_employee',views.Add_employee,name='Add_employee'),
    # path('new',views.new,name="new"),

    path('update_employe',views.update_employe_display,name='update_employe'),
    path('update',views.update_employe,name= 'update'),
    path('update_data',views.update_data,name='update_data'),
    path('delete_emp',views.delete_emp,name='delete_emp'),
    path('delete_employe',views.delete_employe,name='delete_employe'),

    path('employee_leave',views.employee_leave,name = 'employee_leave'),
    path('apply_leave',views.apply_leave,name='apply_leave'),
    path('Add_leave',views.Add_leave,name='Add_leave'),

    path('hr_newsletters',views.hr_newsletters,name= 'hr_newsletters'),
    path('add_message',views.add_message,name='add_message'),
    path('delete_msg/<int:pk>',views.delete_msg,name='delete_msg'),

    path('dashboard',views.dashboard,name='dashboard')


]

