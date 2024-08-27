from django.urls import path
from.import views

urlpatterns = [
    path('home/<str:uid>/', views.home, name = 'technician_home'),
    path('logout/', views.technician_logout, name = 'technician_logout'),
    path('profile/<str:uid>/', views.technician_profile, name = 'technician_profile'),
    path('profile/delete/<str:uid>/', views.delete_profile, name = 'delete_technician'),
    path('complaints/<str:uid>/', views.complaints, name = 'technician_complaint'),
    path('complaints/create/<str:complaint_id>/', views.add_complaint, name = 'creating_complaint'),
    path('delete_complaint_bill/<int:billing_id>/', views.delete_complaint_bill, name = 'delete_complaint_bill'),
    path('receipt/<str:complaint_id>/', views.add_receipt, name = 'receipt'),
    path('sales_orders/<str:uid>/', views.sales_order, name = 'technician_sales_order'),
    path('sales_orders/create/<str:uid>/', views.add_sales_order, name = 'creating_sales_order'),
    path('receipts/<str:uid>/', views.receipt, name = 'technician_receipt'),
]