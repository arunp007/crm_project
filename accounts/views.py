from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from.models import *

def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email_id']
        password = request.POST['password']

        try:
            current_user = Admin.objects.get(email = email, password = password)
            request.session['xyz'] = str(current_user.uid)
            current_user.is_active = 'True'
            current_user.save()

            return redirect('admin_home', uid = current_user.uid)
        
        except Admin.DoesNotExist:
            messages.warning(request, "Invalid credentials.")
            return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/admin_login.html')

def admin_signup(request):
    if request.method == 'POST':
        name = request.POST['full_name']
        address = request.POST['address']
        email = request.POST['email_id']
        phone = request.POST['phone_number']
        password = request.POST['password']
        terms_and_conditions = request.POST['terms_and_conditions']

        user_obj = Admin.objects.filter(email = email)

        if user_obj.exists():
            messages.warning(request, "Email is already exist.")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = Admin(full_name = name, address = address, email = email, phone = phone, password = password, terms_and_conditions = terms_and_conditions)
        user_obj.save()

        messages.success(request, "Successfully registered. Login now")
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'accounts/admin_signup.html')

def customer_login(request):
    if request.method == 'POST':
        email = request.POST['email_id']
        password = request.POST['password']

        try:
            current_user = Customer.objects.get(email = email, password = password)
            request.session['xyz'] = str(current_user.uid)
            current_user.is_active = 'True'
            current_user.save()

            return redirect('customer_home', uid = current_user.uid)
        
        except Customer.DoesNotExist:
            messages.warning(request, "Invalid credentials.")
            return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/customer_login.html')

def customer_signup(request):
    if request.method == 'POST':
        name = request.POST['full_name']
        address = request.POST['address']
        email = request.POST['email_id']
        phone = request.POST['phone_number']
        password = request.POST['password']
        terms_and_conditions = request.POST['terms_and_conditions']

        user_obj = Customer.objects.filter(email = email)

        if user_obj.exists():
            messages.warning(request, "Email is already exist.")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = Customer(full_name = name, address = address, email = email, phone = phone, password = password, terms_and_conditions = terms_and_conditions)
        user_obj.save()

        messages.success(request, "Successfully registered. Login now")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/customer_signup.html')

def technician_login(request):
    if request.method == 'POST':
        email = request.POST['email_id']
        password = request.POST['password']

        try:
            current_user = Technician.objects.get(email_id = email, password = password)
            request.session['xyz'] = str(current_user.uid)
            current_user.is_active = 'True'
            current_user.save()
            
            return redirect('technician_home', uid = current_user.uid)
        
        except Technician.DoesNotExist:
            messages.warning(request, "Invalid credentials.")
            return HttpResponseRedirect(request.path_info)
        
    return render(request, 'accounts/technician_login.html')

def technician_signup(request):
    if request.method == 'POST':
        name = request.POST['full_name']
        address = request.POST['address']
        email = request.POST['email_id']
        phone = request.POST['phone_number']
        password = request.POST['password']
        terms_and_conditions = request.POST['terms_and_conditions']

        user_obj = Technician.objects.filter(email_id = email)

        if user_obj.exists():
            messages.warning(request, "Email is already exist.")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = Technician(full_name = name, address = address, email_id = email, phone = phone, password = password, terms_and_conditions = terms_and_conditions)
        user_obj.save()

        messages.success(request, "Successfully registered. Login now")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/technician_signup.html')
