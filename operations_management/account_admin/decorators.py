from django.shortcuts import redirect
from django.http import HttpResponse
from login.models import employee

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            name = request.session['user_name']
            password = request.session['password']
            emp = employee.objects.get(user_name = name, password= password)
            department = emp.department
            if department in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def notallowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            name = request.session['user_name']
            password = request.session['password']
            emp = employee.objects.get(user_name = name, password= password)
            department = emp.department
            if department in allowed_roles:
                return HttpResponse('You can not apply leave....')

            else:
                return view_func(request, *args, **kwargs)

        return wrapper_func
    return decorator