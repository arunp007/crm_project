import base64
import io
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from matplotlib import pyplot as plt
from customer.forms import SalesOrderForm, ComplaintForm
from customer.models import BillingItem, Complaint
from accounts.models import Technician
from technician.forms import TechnicianForm, ReceiptForm
from django.contrib import messages
from customer.models import SalesOrder
from django.contrib.auth.decorators import login_required
from technician.models import ComplaintBilling, Receipt


def home(request, uid):

    technician = get_object_or_404(Technician, uid=uid)
    
    if technician.is_active == True:
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

        complaint = Complaint.objects.all()

        return render(request, 'technician/home.html', {'graph': image_base64, 'technician': technician, 'complaints': complaints, 'resolved': resolved})

    else:
        return redirect('technician_login')
    

def technician_logout(request):
    try:
        uid = request.session.get('xyz')
        if uid:
            current_user = Technician.objects.get(uid=uid)
            current_user.is_active = False
            current_user.save()

        request.session.flush()

    except Technician.DoesNotExist:
        pass
    
    return redirect('technician_login')


def technician_profile(request, uid):
    technician = get_object_or_404(Technician, uid=uid)
    if request.method == 'POST':
        form = TechnicianForm(request.POST, instance = technician)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Updated...")

    else:
        form = TechnicianForm(instance=technician)

    return render(request, 'technician/profile.html', {'form': form, 'technician': technician})


def delete_profile(request, uid):
    Technician.objects.get(uid = uid).delete()
    messages.warning(request, "Account Deleted!")
    return redirect('technician_login')

def add_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, complaint_id = complaint_id)

    if request.method == 'POST':
        bill = ''
        form = ComplaintForm(request.POST, show_fields={'technician': True, 'token': True, 'token_number': True, 'machine_type': True, 'machine_model': True, 'machine_no': True, 'payment_status': True, 'payment_type': True, 'collected_amount': True, 'ticket_status': True, 'is_resolve': True}, instance = complaint)
        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        rate = request.POST['rate']

        complaint_bill = ComplaintBilling(complaint = complaint, item_name = item_name, quantity = quantity, rate = rate)
        complaint_bill.save()
        
        messages.success(request, "Bill Created!")

        
        
        if form.is_valid():
            form.save()
            messages.success(request, "Complaint Created!")


    else:
        form = ComplaintForm(instance = complaint, show_fields={'technician': True, 'token': True, 'token_number': True, 'machine_type': True, 'machine_model': True, 'machine_no': True, 'payment_status': True, 'payment_type': True, 'collected_amount': True, 'ticket_status': True, 'is_resolve': True}) 

    bill = ComplaintBilling.objects.filter(complaint_id = complaint)

    total_price = sum(b.rate for b in bill)
    

    return render(request, 'technician/add_complaint.html', {'form': form, 'complaint': complaint, 'bill': bill, 'total_price': total_price}) 

def delete_complaint_bill(request, billing_id):
    complaint_bill = get_object_or_404(ComplaintBilling, billing_id = billing_id)
    bill = ComplaintBilling.objects.get(billing_id = billing_id)
    bill.delete()
    messages.warning(request, "Bill Deleted!")
    return redirect('creating_complaint', complaint_bill.complaint.complaint_id)

def complaints(request, uid):
    technician = get_object_or_404(Technician, uid = uid)
    
    if technician.is_active == True:

        complaint_data = Complaint.objects.all()
        return render(request, 'technician/complaints.html', {'complaint_data': complaint_data, 'technician': technician})

    else:
        return redirect('technician_login')
    

def receipt(request, complaint_id):
    complaint = get_object_or_404(Complaint, complaint_id = complaint_id)
    
    if request.method == 'POST':

        form = ReceiptForm(request.POST)

        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.complaint = complaint
            receipt.save()
            messages.success(request, "Receipt Added!")


    else:
        form = ReceiptForm()

    return render(request, 'technician/receipt.html', {'form': form, 'complaint': complaint })

def add_sales_order(request, uid):
    technician = get_object_or_404(Technician, uid=uid)

    if request.method == 'POST':
        form = SalesOrderForm(request.POST)
        sales_executive = request.POST['sales_executive']
        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        rate = request.POST['rate']

        if form.is_valid():
            sales_order = form.save(commit=False)
            sales_order.technician = technician
            sales_order.save()
            billing_item = BillingItem(sales_order=sales_order, sales_executive=sales_executive, item_name=item_name, quantity=quantity, rate=rate)
            
            billing_item.save()


            messages.success(request, "Sales Order And Billing Item Created!")

            

    else:
        form = SalesOrderForm()


    #fetching billing item and filter by uid

    item = BillingItem.objects.all()

    return render(request, 'technician/add_sales_order.html', {'form': form, 'technician': technician, 'item': item})


def delete_bill(request, uid):
    bill = BillingItem.objects.get(uid = uid)
    bill.delete()
    return redirect('creating_sales_order', bill.sales_order)



def sales_order(request, uid):
    technician = get_object_or_404(Technician, uid = uid)

    if technician.is_active == True: 

        sales_order_data = SalesOrder.objects.all()
        return render(request, 'technician/sales_order.html', {'sales_order': sales_order_data, 'technician': technician})

    else:
        return redirect('technician_login')


def receipt(request, uid):
    technician = get_object_or_404(Technician, uid = uid)

    if technician.is_active == True:
        receipts = Receipt.objects.all()
        return render(request, 'technician/receipt.html', {'technician': technician, 'receipts': receipts})
    
    else:
        return redirect('technician_login')














