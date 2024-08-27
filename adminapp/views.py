from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import Admin
from accounts.models import Customer, Technician
from customer.forms import SalesOrderForm, ComplaintForm
from customer.models import BillingItem, Complaint, SalesOrder
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.contrib import messages
from adminapp.forms import AdminForm
from technician.models import Receipt
from home.models import Contact


def home(request, uid):
    admin = get_object_or_404(Admin, uid = uid)

    if admin.is_active == True:

        #data
        customer = Customer.objects.count()
        technician = Technician.objects.count()
        complaint = Complaint.objects.count()
        resolved = Complaint.objects.filter(is_resolve=True).count()
        sales_order = SalesOrder.objects.count()
        receipt_report = Receipt.objects.count()
        contact = Contact.objects.count()

        #is_active members
        customer_is_active = Customer.objects.filter(is_active = True).count()
        technician_is_active = Technician.objects.filter(is_active = True).count()

        # Create a plot
        plt.figure(figsize=(6, 4))
        categories = ['Customers', 'Technicians', 'Complaints', 'Sales Order']
        counts = [customer, technician, complaint, sales_order]
    
        plt.bar(categories, counts, color=['blue', 'green','red', 'purple'])
        plt.title('Statistics')
        plt.ylabel('Count')

        # Add annotations
        for i, count in enumerate(counts):
            plt.text(i, count, str(count), fontsize=12, ha='center', va='bottom')

        # Save it to a buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        image_base64 = base64.b64encode(image_png)
        image_base64 = image_base64.decode('utf-8')

        return render(request, 'admin/home.html', {'admin': admin, 'customer': customer, 'technician': technician, 'complaint': complaint, 'resolved': resolved, 'sales_order': sales_order, 'receipt_report': receipt_report, 'graph': image_base64, 'customer_is_active': customer_is_active, 'technician_is_active': technician_is_active, 'contact': contact})

    else:
        return redirect('admin_login')


def admin_logout(request):
    try:
        uid = request.session.get('xyz')
        if uid:
            current_user = Admin.objects.get(uid=uid)
            current_user.is_active = False
            current_user.save()

        request.session.flush()

    except Admin.DoesNotExist:
        pass
    
    return redirect('admin_login')

def customers(request, uid):
    admin = get_object_or_404(Admin, uid = uid)

    if admin.is_active == True:
        customers_data = Customer.objects.all()
        return render(request, 'admin/customers.html', {'customers_data': customers_data, 'admin': admin})

    else:
        return redirect('admin_login')


def add_customers(request, uid):
    admin = get_object_or_404(Admin, uid = uid)
    if request.method == 'POST':
        name = request.POST['full_name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        terms_and_conditions = request.POST['terms_and_conditions']

        user_obj = Customer.objects.filter(email = email)

        if user_obj.exists():
            messages.warning(request, "Email Already Exists!")
            return HttpResponseRedirect(request.path_info)


        user_obj = Customer(full_name = name, address = address, email = email, phone = phone, password = password, terms_and_conditions = terms_and_conditions)
        user_obj.save()   

        messages.success(request, "Customer Created Successfully!")

    return render(request, 'admin/add_customer.html', {'admin': admin})


def technicians(request, uid):
    admin = get_object_or_404(Admin, uid = uid)
    
    if admin.is_active == True:
        technicians_data = Technician.objects.all()
        return render(request, 'admin/technicians.html', {'technicians_data': technicians_data, 'admin': admin})

    else:
        return redirect('admin_login')


def add_technicians(request, uid):
    admin = get_object_or_404(Admin, uid = uid)

    if request.method == 'POST':
        name = request.POST['full_name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        terms_and_conditions = request.POST['terms_and_conditions']

        user_obj = Technician.objects.filter(email_id = email)

        if user_obj.exists():
            messages.warning(request, "Email Already Exists!")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = Technician(full_name = name, address = address, email_id = email, phone = phone, password = password, terms_and_conditions = terms_and_conditions)
        user_obj.save()

        messages.success(request, "Technician Created Successfully!")

    return render(request, 'admin/add_technician.html', {'admin': admin})


def admin_profile(request, uid):
    admin = get_object_or_404(Admin, uid=uid)
    if request.method == 'POST':
        form = AdminForm(request.POST, instance = admin)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Updated...")

    else:
        form = AdminForm(instance=admin)

    return render(request, 'admin/profile.html', {'form': form, 'admin': admin})


def delete_admin(request, uid):
    Admin.objects.get(uid = uid).delete()
    messages.warning(request, "Account Deleted!")
    return redirect('admin_login')

def sales_orders(request, uid):
    admin = get_object_or_404(Admin, uid = uid)
    
    if admin.is_active == True:
        sales_order = SalesOrder.objects.all()
        return render(request, 'admin/sales_order.html', {'sales_order': sales_order, 'admin': admin})

    else:
        return redirect('admin_login')

def add_sales_order(request, uid):
    admin = get_object_or_404(Admin, uid=uid)

    if request.method == 'POST':
        form = SalesOrderForm(request.POST)
        sales_executive = request.POST['sales_executive']
        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        rate = request.POST['rate']

        if form.is_valid():
            sales_order = form.save(commit=False)
            sales_order.admin = admin 
            sales_order.save()
            billing_item = BillingItem(sales_order=sales_order, sales_executive=sales_executive, item_name=item_name, quantity=quantity, rate=rate)
            
            billing_item.save()


            messages.success(request, "Sales Order And Billing Item Created!")

            

    else:
        form = SalesOrderForm()


    #fetching billing item and filter by uid

    item = BillingItem.objects.filter()

    return render(request, 'admin/add_sales_order.html', {'form': form, 'admin': admin, 'item': item})


def complaint(request, uid):
    admin = get_object_or_404(Admin, uid = uid)

    if admin.is_active == True:

        complaint_details = Complaint.objects.all()
        return render(request, 'admin/complaint.html', {'complaint': complaint_details, 'admin': admin})
    
    else:
        return redirect('admin_login')


def add_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, complaint_id = complaint_id)
    if request.method == 'POST':
        
        form = ComplaintForm(request.POST, show_fields={'technician': True, 'token': True, 'token_number': True, 'machine_type': False, 'machine_model': False, 'machine_no': False, 'payment_status': False, 'payment_type': False, 'collected_amount': False, 'ticket_status': False,}, instance = complaint)
        if form.is_valid():
            form.save()
            messages.success(request, "Token Added Successfully!")

    else:
        form = ComplaintForm(instance = complaint, show_fields={'technician': True, 'token': True, 'token_number': True, 'machine_type': False, 'machine_model': False, 'machine_no': False, 'payment_status': False, 'payment_type': False, 'collected_amount': False, 'ticket_status': False,}) 


    return render(request, 'admin/add_complaint.html', {'form': form, 'complaint': complaint})   


def receipt_report(request, uid):
    admin = get_object_or_404(Admin, uid = uid)
    current_date = request.GET.get('current_date')
    last_date = request.GET.get('last_date')
    total = float

    receipts = Receipt.objects.all()  

    

    if admin.is_active == True:

        if current_date and last_date:
            current_date = datetime.strptime(current_date, '%Y-%m-%d' ).date()
            last_date = datetime.strptime(last_date, '%Y-%m-%d').date()
            receipts = receipts.filter(receipt_date__range=[current_date, last_date])
            
            total = sum(i.receipt_amount for i in receipts)  
        
        return render(request, 'admin/receipt_report.html', {'admin': admin, 'receipts': receipts, 'current_date': current_date, 'last_date': last_date, 'total': total})
    
    else:
        return redirect('admin_login')
    

def contact(request, uid):
    admin = get_object_or_404(Admin, uid = uid)
    contact = Contact.objects.all()
    return render(request, 'admin/contact_us.html', {'admin': admin, 'contact': contact})

