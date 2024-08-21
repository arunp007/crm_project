from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_data = Contact(name = name, email = email, phone = phone, subject = subject, message = message)
        contact_data.save()

        messages.success(request, "Thank you for contacting us. We will get back to you soon.")
        
    return render(request, 'home/contact.html')
