import uuid
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import matplotlib.pyplot as plt
import io
import urllib, base64
from accounts.models import Customer
from django.contrib import messages
from customer.forms import CustomerForm
from customer.forms import ComplaintForm, SalesOrderForm
from customer.models import Complaint, SalesOrder, BillingItem
from django.core.paginator import Paginator
from technician.models import Receipt


def home(request, uid):
    customer_id = get_object_or_404(Customer, uid=uid)

    if customer_id.is_active == True:
    
        #data
        complaints = Complaint.objects.count()
        resolved = Complaint.objects.filter(is_resolve=True).count()

        # Create a plot
        plt.figure(figsize=(6, 4))
        categories = ['Total Complaints', 'Resolved Complaints']
        counts = [complaints, resolved]
    
        plt.bar(categories, counts, color=['blue', 'green'])
        plt.title('Total Complaints vs Resolved Complaints')
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
        return render(request, 'customer/home.html', {'graph': image_base64, 'customer_id': customer_id, 'complaints': complaints, 'resolved': resolved})
    
    else:
        return redirect('customer_login')

    
    


def customer_logout(request):
    try:
        uid = request.session.get('xyz')
        if uid:
            current_user = Customer.objects.get(uid=uid)
            current_user.is_active = False
            current_user.save()

        request.session.flush()

    except Customer.DoesNotExist:
        pass
    
    return redirect('customer_login')


def customer_profile(request, uid):
    customer = get_object_or_404(Customer, uid=uid)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance = customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Updated...")

    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customer/profile.html', {'form': form, 'customer': customer})


def delete_profile(request, uid):
    Customer.objects.get(uid = uid).delete()
    messages.warning(request, "Account Deleted!")
    return redirect('customer_login')
    



def create_complaint(request, uid):
    customer = get_object_or_404(Customer, uid = uid)
    if request.method == 'POST':
        show_fields = {
        'technician': False,  # False to hide and not required
        'token': False,  # False to hide and not required
        'token_number': False,
        'machine_type': False,
        'machine_model': False,
        'machine_no': False,
        'payment_status': False,
        'payment_type': False,
        'collected_amount': False,
        'ticket_status': False,
    

        }
        form = ComplaintForm(request.POST, show_fields = show_fields)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.customer = customer
            complaint.save()
            messages.success(request, "Complaint Created!")

    else:
        form = ComplaintForm()

    return render(request, 'customer/create_complaint.html',{'form': form, 'customer': customer})


def complaints(request, uid):
    customer_id = get_object_or_404(Customer, uid = uid)
    
    if customer_id.is_active == True:

        complaint_data = Complaint.objects.all()
        return render(request, 'customer/complaints.html', {'complaint_data': complaint_data, 'customer_id': customer_id})

    else:
        return redirect('customer_login')


def create_sales_order(request, uid):
    customer = get_object_or_404(Customer, uid=uid)

    if request.method == 'POST':
        form = SalesOrderForm(request.POST)
        sales_executive = request.POST['sales_executive']
        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        rate = request.POST['rate']

        if form.is_valid():
            sales_order = form.save(commit=False)
            sales_order.customer = customer 
            sales_order.save()
            billing_item = BillingItem(sales_order=sales_order, sales_executive=sales_executive, item_name=item_name, quantity=quantity, rate=rate)
            
            billing_item.save()


            messages.success(request, "Sales Order And Billing Item Created!")

            

    else:
        form = SalesOrderForm()


    item = BillingItem.objects.all()

    return render(request, 'customer/create_sales_order.html', {'form': form, 'customer': customer, 'item': item})


def sales_order(request, uid):
    customer_id = get_object_or_404(Customer, uid = uid)

    if customer_id.is_active == True:

        sales_order = SalesOrder.objects.all()
        customer = Customer.objects.all()
        return render(request, 'customer/sales_order.html', {'sales_order': sales_order, 'customer_id': customer_id, 'customer': customer})

    else:
        return redirect('customer_login')
    

def receipt(request, uid):
    customer_id = get_object_or_404(Customer, uid = uid)

    if customer_id.is_active == True:
        receipts = Receipt.objects.all()
        return render(request, 'customer/receipt.html', {'customer_id': customer_id, 'receipts': receipts})
    
    else:
        return redirect('customer_login')